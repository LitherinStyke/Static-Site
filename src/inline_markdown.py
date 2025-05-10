import re
from textnode import TextNode, TextType
    
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

    for node in nodes:
        print(node)

    return nodes

def text_to_textnodes(text):
    pass

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
    
def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches