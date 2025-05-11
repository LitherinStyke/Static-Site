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
    text_to_textnodes,
    block_to_block_type,
    markdown_to_blocks)

from htmlnode import (
    HTMLNode, 
    LeafNode, 
    ParentNode)



def main():
    print('hello world')

    test = """
# Header test

## Header test2
#test

> quote 1
> quote 2

> quote 3
>quote 4

- ordered 1
- ordered 2

- ordered 3
-ordered 4

1. unordered 1
2. unordered 2

1. unordered 3
4. unordered 4
3. unordered 5

```
They holy code
var var
other var
```

tihoteioheshoifeohisef
"""
    text_test = markdown_to_blocks(test)

    for block in text_test:
        print(block)
        print(f'{block_to_block_type(block)}\n')

main()