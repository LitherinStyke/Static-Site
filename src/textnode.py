from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = 'text'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

class TextNode():
    def __init__(self, text, text_type:TextType, url=None):
        self.text = text
        self.text_type:TextType = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text and 
                self.text_type.value == other.text_type.value and
                self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
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

def text_node_to_html_node(node:TextNode):
    new_leaf = None

    match node.text_type:
        case TextType.TEXT:
            new_leaf = LeafNode(None, node.text)

        case TextType.BOLD:
            new_leaf = LeafNode('b', node.text)

        case TextType.ITALIC:
            new_leaf = LeafNode('i', node.text)

        case TextType.CODE:
            new_leaf = LeafNode('code', node.text)

        case TextType.LINK:
            new_leaf = LeafNode('a', node.text, {'href': node.url})

        case TextType.IMAGE:
            new_leaf = LeafNode('img', '', {"src": node.url, "alt": node.text})

        case _:
            raise Exception()

    return new_leaf
    