from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

print('hello world')

def main():
    new_node:TextNode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(new_node)
    new_html_node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank",})
    print(new_html_node)

    new_leafnode = LeafNode("p", "This is a paragraph of text.")
    print(new_leafnode.to_html())
    new_other_leafnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(new_other_leafnode.to_html())


main()