import re
from enum import Enum
from textnode import TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT: 
            nodes.append(node)
            continue
        
        text_node = node.text.split(delimiter)

        if len(text_node) % 2 == 0:
            raise Exception(f"Entering or exiting delimiter for '{text_type.value}' not found\n---|{node}")

        for i in range(len(text_node)):
            if text_node[i] == "":
                continue

            if i % 2 == 0:
                nodes.append(TextNode(text_node[i], TextType.TEXT))
            else:
                nodes.append(TextNode(text_node[i], text_type))

    return nodes

def text_to_textnodes(text):
    new_node = TextNode(text, TextType.TEXT)

    bolden = split_nodes_delimiter([new_node], '**', TextType.BOLD)

    slanten = split_nodes_delimiter(bolden, '_', TextType.ITALIC)

    codin = split_nodes_delimiter(slanten, '`', TextType.CODE)

    linkin = split_nodes_link(codin)

    imgin = split_nodes_image(linkin)

    return imgin

def split_nodes_image(old_nodes):
    node_list = []

    for old in old_nodes:

        if old.text_type != TextType.TEXT:
            node_list.append(old)
            continue

        original_text:str = old.text
        extraction_list = extract_markdown_images(original_text)

        if not extraction_list:
            node_list.append(old)
            continue

        for extract in extraction_list:
            text_split = original_text.split(f'![{extract[0]}]({extract[1]})', 1)

            if text_split[0] != '':
                node_list.append(TextNode(text_split[0], TextType.TEXT))
            node_list.append(TextNode(extract[0], TextType.IMAGE, extract[1]))

            original_text = text_split[1]

        if original_text != "":
            node_list.append(TextNode(original_text, TextType.TEXT))
        
    return node_list

def split_nodes_link(old_nodes):
    node_list = []
    for old in old_nodes:

        if old.text_type != TextType.TEXT:
            node_list.append(old)
            continue

        original_text:str = old.text
        extraction_list = extract_markdown_links(original_text)

        if not extraction_list:
            node_list.append(old)
            continue

        for extract in extraction_list:
            text_split = original_text.split(f'[{extract[0]}]({extract[1]})', 1)

            if text_split[0] != '':
                node_list.append(TextNode(text_split[0], TextType.TEXT))
            node_list.append(TextNode(extract[0], TextType.LINK, extract[1]))

            original_text = text_split[1]

        if original_text != "":
            node_list.append(TextNode(original_text, TextType.TEXT))

    return node_list

def block_to_block_type(markdown_block):
    found_block = None

    if match_markdown_header(markdown_block):
        found_block = BlockType.HEADING
    elif match_markdown_code(markdown_block):
        found_block = BlockType.CODE
    elif match_markdown_quote(markdown_block):
        found_block = BlockType.QUOTE
    elif match_markdown_ordered(markdown_block):
        found_block = BlockType.ORDERED_LIST
    elif match_markdown_unordered(markdown_block):
        found_block = BlockType.UNORDERED_LIST
    else:
        found_block = BlockType.PARAGRAPH
    
    return found_block

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    filtered_blocks = []

    for block in blocks:
        if block == "":
            continue

        block = block.strip()
        filtered_blocks.append(block)

    print(filtered_blocks)
    return filtered_blocks
    
def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def match_markdown_header(text):
    if '\n' in text: return False
    pattern = r'^\#{1,6}\s'
    matches = re.match(pattern, text)
    return matches is not None

def match_markdown_code(text):
    pattern = r'^\`{3}.*\`{3}$'
    matches = re.search(pattern, text, re.DOTALL)
    return matches is not None

def match_markdown_quote(text):
    pattern = r'^\>\s'
    lines = text.split('\n')
    for quote in lines:
        if not re.match(pattern, quote): return False
    return True

def match_markdown_unordered(text):
    pattern = r'^\-\s'
    lines = text.split('\n')
    for quote in lines:
        if not re.match(pattern, quote): return False
    return True

def match_markdown_ordered(text):
    lines = text.split('\n')
    for i, line in enumerate(lines, 1):
        pattern = f'^{i}\\.\s'
        if not re.match(pattern, line): return False
    return True