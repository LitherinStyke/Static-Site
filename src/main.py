from inline_markdown import (
    markdown_to_html_node)



def main():
    md = """
### Big ol header

There are _many things_ you **may** need to test with a markdown. Lets go list a few.

1. an
2. ordered
3. list

```
#some random ass code
for i in range(5):
    seed1_ticks += 1
    print(f'Seed 1: {random.random()}, Ticks: {seed1_ticks}')
```

- an
- unordered
- list

> sometimes **you** just gotta _quote that shit_
> frfr. _I hate it here_

Maybe with some time we may even be able to post pics with the **best girl**.
![Best girl Meow Skulls](https://fortnite.gg/img/items/8333/bg.jpg?8)
Heres a [link](https://fortnite.fandom.com/wiki/Meow_Skulls) to the wiki!
"""
    full_html = markdown_to_html_node(md)
    print(full_html.to_html())

main()