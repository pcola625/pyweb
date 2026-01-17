from htmlnode import *

class LeafNode(HtmlNode):

    def __init__(self,
                 tag,
                 value,
                 props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
	
        if (self.value is None):
            raise ValueError("Value needs to be not 'None' on a LeafNode")
        if (self.tag is None):
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


    def __repr__(self):

        print (f"LeafNode(\n tag: {self.tag},\n value = {self.value},\n props = {self.props_to_html()}\n)")
