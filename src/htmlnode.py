import html

class HtmlNode():

    def __init__(self, 
                 tag = None, 
                 value = None, 
                 children = None, 
                 props = None):
        
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):

        raise NotImplementedError("Not implemented")


    def props_to_html(self):
        
        retstring = ""

        if self.props is None:
            return retstring
        if len(self.props) == 0:
            return retstring
        for prop in self.props:
            retstring += f' {prop}="{self.props[prop]}"'

        return retstring

    def __repr__(self):

        print (f"HtmlNode(\n tag: {self.tag},\n value = {self.value},\n children = {self.children},\n props = {self.props_to_html()}\n)")


