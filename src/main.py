from textnode import (
    TextNode,           
    TextType,
    text_node_to_html_node,)

from inline_markdown import ( 
    split_nodes_delimiter, 
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_link,
    split_nodes_image,
    text_to_textnodes)

from htmlnode import (
    HTMLNode, 
    LeafNode, 
    ParentNode)


print('hello world')

def main():
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"



main()