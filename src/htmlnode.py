class HTMLNode():
    def __init__(self, tag:str=None, value:str=None, children:list=None, props:dict=None):
        self.tag:str = tag
        self.value:str = value
        self.children:list[HTMLNode] = children
        self.props:dict = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
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