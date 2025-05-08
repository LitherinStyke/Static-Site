class HTMLNode():
    def __init__(self, tag=None, value=None, children:list=None, props:dict=None):
        self.tag = tag
        self.value = value
        self.children:list = children
        self.props:dict = props

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
        
        if self.children is not None:
            for child in self.children:
                child_builder += f'{child_count}: {child}\n'
                child_count += 1
        else: child_builder = f'\nNo children'

        return f'HTML Node({self.tag}, {self.value}){child_builder}{prop_builder}'
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None: raise ValueError("Parent node must have a Tag")
        if self.children is None: raise ValueError("Parent node must have children")
        
        def childeren_to_string(child_list):
            if len(child_list) == 0: return ""
            children_string = child_list[0].to_html()
            children_string += childeren_to_string(child_list[1:])
            return children_string

        return f'<{self.tag}{self.props_to_html()}>{childeren_to_string(self.children)}</{self.tag}>'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None: return ValueError("Leaf node must have a Value")
        if self.tag is None: return self.value

        return (f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>')