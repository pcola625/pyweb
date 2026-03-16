from htmlnode import *

class ParentNode(HtmlNode):

    def __init__(self,
                 tag: object,
                 children: object,
                 props: object = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
	
        if (self.tag is None):
            raise ValueError("Tag needs to be not 'None' on a ParentNode")
        if (self.children is None) or (self.children == ""):
            raise ValueError("Parent node, by definition, needs children and must not be 'None' or empty")
        # begin building the string:
        htmlstring = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children: 
            htmlstring += f"{child.to_html()}"

        htmlstring += f"</{self.tag}>"
	
        return htmlstring

    def __repr__(self):

        print (f"ParentNode(\n tag: {self.tag},\n children: {self.children}\n props: {self.props_to_html()}\n)")
