import unittest

from htmlnode import HTMLNode


class test_html_node_creates_with_defaults(unittest.TestCase):
    node = HTMLNode()
    assert node.tag is None
    assert node.value is None
    assert node.children is None
    assert node.props is None

class test_props_to_html_with_href(unittest.TestCase):
    node = HTMLNode(props={"href": "https://boot.dev"})
    assert node.props_to_html() == ' href="https://boot.dev"'

class test_props_to_html_with_multiple_props(unittest.TestCase):
    node = HTMLNode(props={"class": "btn", "id": "submit-btn"})
    # Remember, properties can be in any order in the string
    props_html = node.props_to_html()
    assert ' class="btn"' in props_html
    assert ' id="submit-btn"' in props_html


if __name__ == "__main__":
    unittest.main()