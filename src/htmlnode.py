from enum import Enum

class TagType(Enum):
    PARAGRAPH = 'p'
    ANCHOR = 'a'

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None: return ""

        converted = ''
        for prop in self.props:
            converted += f' {prop}="{self.props[prop]}"'
        return converted

    def __repr__(self):
        child_builder = "\n"
        child_count = 0
        prop_builder = "\n"

        for prop in self.props:
            prop_builder += f"---|'{prop}': '{self.props[prop]}'\n"
        
        if self.children != None:
            for child in self.children:
                child_builder += f'{child_count}: {child}\n'
                child_count += 1
        else: child_builder = f'\nNo children'

        return f'HTML Node({self.tag}, {self.value}){child_builder}{prop_builder}'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None: return ValueError("LeafNode must have a value")
        if self.tag == None: return self.value

        return (f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>')