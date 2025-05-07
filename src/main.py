from textnode import TextNode, TextType
from htmlnode import HTMLNode

print('hello world')

def main():
    new_node:TextNode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(new_node)
    new_html_node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank",})
    new_html_node.props_to_html()
    print(new_html_node)

main()