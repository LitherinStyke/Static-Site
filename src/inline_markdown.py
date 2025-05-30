import re
from enum import Enum
from textnode import (
    TextNode, 
    TextType,
    text_node_to_html_node)

from htmlnode import (
    LeafNode,
    ParentNode,
    HTMLNode)


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
        
        splitnodes = []
        text_node = node.text.split(delimiter)

        if len(text_node) % 2 == 0:
            raise Exception(f"Entering or exiting delimiter for '{text_type.value}' not found\n---|{node}")

        for i in range(len(text_node)):
            if text_node[i] == "":
                continue

            if i % 2 == 0:
                splitnodes.append(TextNode(text_node[i], TextType.TEXT))
            else:
                splitnodes.append(TextNode(text_node[i], text_type))

        nodes.extend(splitnodes)

    return nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_link(nodes)

    nodes = split_nodes_image(nodes)

    nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)

    nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)

    nodes = split_nodes_delimiter(nodes, '_', TextType.ITALIC)
    return nodes

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

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    # We need a main parent node for the whole markdown to contain the other parent nodes made from block_to_html

    block_node_list = []
    for block in blocks:
        block_type = block_to_block_type(block)
        html_block = block_to_html(block, block_type)
        block_node_list.append(html_block)

    mega_parent:ParentNode = ParentNode('div', block_node_list)
    return mega_parent

def block_to_html(block, block_type):
    # Turn this shit into HTML nodes. Leaf and Parent
    text_nodes = text_to_textnodes(block)

    hash_count = 0
    if block_type == BlockType.HEADING:
        hash_count = len(block.split(' ', 1)[0])

    block_tag = html_block_tags(block_type, hash_count)

    parent_block:ParentNode = None

    if block_type == BlockType.CODE:
        child_block = LeafNode(block_tag, block)
        parent_block = ParentNode('pre', [child_block])
    else:
        parent_block = get_childeren_of_markdown_block(block, block_tag)

    #if parent_block is not None: print(parent_block.to_html())
    return parent_block

def get_childeren_of_markdown_block(md_block, tag):
    leaf_nodes = []
    text_nodes = text_to_textnodes(md_block)
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        leaf_nodes.append(html_node)

    return ParentNode(tag, leaf_nodes)
        



def block_to_block_type(markdown_block):
    lines = markdown_block.split('\n')

    if markdown_block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    
    if markdown_block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if markdown_block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    
    if markdown_block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    filtered_blocks = []

    for block in blocks:
        if block == "":
            continue

        block = block.strip()
        filtered_blocks.append(block)

    return filtered_blocks
    
def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
    
def html_block_tags(block_type, hash_count=0):
    tags = ''

    match block_type:
        case BlockType.HEADING:
            tags = f'h{hash_count}'

        case BlockType.PARAGRAPH:
            tags = 'p'

        case BlockType.CODE:
            tags = 'code'

        case BlockType.QUOTE:
            tags = 'blockquote'

        case BlockType.ORDERED_LIST:
            tags = 'ol'

        case BlockType.UNORDERED_LIST:
            tags = 'ul'

        case _:
            raise ValueError(f'{block_type} is not a valid BlockType or is not supported')
    
    return tags