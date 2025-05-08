from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

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
    new_leaf_image = new_leaf_image.text_node_to_html_node()
    print(new_leaf_image.to_html())

main()