from textnode import *

print('hello world')

def main():
    new_node:TextNode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(new_node)

main()