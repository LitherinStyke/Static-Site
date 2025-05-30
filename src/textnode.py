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

def text_node_to_html_node(node):
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