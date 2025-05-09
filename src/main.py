from textnode import (
    TextNode,           
    TextType, 
    split_nodes_delimiter, 
    text_node_to_html_node)

from htmlnode import (
    HTMLNode, 
    LeafNode, 
    ParentNode)

from markdown import extract_markdown_images, extract_markdown_links

print('hello world')

def main():
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))

    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))

main()