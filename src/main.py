from textnode import (
    TextNode,           
    TextType, 
    split_nodes_delimiter, 
    text_node_to_html_node)

from htmlnode import (
    HTMLNode, 
    LeafNode, 
    ParentNode)

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

    new_parentNode = ParentNode(
        "p", 
        [LeafNode("b", "Bold text"), 
         LeafNode(None, "Normal text"), 
         LeafNode("i", "italic text"), 
         LeafNode(None, "Normal text"),
         ],)
    
    print(new_parentNode.to_html())

    new_leaf_image = TextNode(
        "A cool gal!", 
        TextType.IMAGE, 
        "https://static.wikia.nocookie.net/fortnite/images/7/79/Meow_Skulls_-_Outfit_-_Fortnite.png/revision/latest?cb=20220918081949"
        )   
    new_leaf_image = text_node_to_html_node(new_leaf_image)
    print(new_leaf_image.to_html())

    new_spliter = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_spliter2 = TextNode("`code block` is another `coder bockly`", TextType.TEXT)
    new_spliter3 = TextNode("Bold and brash", TextType.BOLD)
    new_nodes = split_nodes_delimiter([new_spliter, new_spliter3, new_spliter2], '`', TextType.CODE)
    print(new_nodes)

main()