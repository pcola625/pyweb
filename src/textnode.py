from leafnode import LeafNode
from enum import Enum
#example Enum
class Bender(Enum):
    AIR_BENDER = "air"
    WATER_BENDER = "water"
    EARTH_BENDER = "earth"
    FIRE_BENDER = "fire"

"""
text (plain)
**Bold text**
_Italic text_
`Code text`
Links, in this format: [anchor text](url)
Images, in this format: ![alt text](url)
"""

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITAL = "italic"
    CODE = "code"
    LINKS = "links"
    IMG = "image"

class TextNode():
    def __init__(self, text: object, text_type: object, url: object = None) -> None:
        self.text = text
        self.text_type =text_type
        self.url = url 

    def __eq__(self, other):
        return ((self.text == other.text) and 
           (self.text_type == other.text_type) and
           (self.url == other.url))

    def __repr__(self):
        #TextNode(TEXT, TEXT_TYPE, URL)
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):

    if text_node is None:
        return "Error: text_node is None."
    if text_node.text_type is None or text_node.text_type == "":
        return "Error: text_node.text_type is None or blank...\n I guess I could assume it is unformatted text, but you know what happens when we ASSuME.\n"
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITAL:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINKS:
            return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
        case TextType.IMG:
            return LeafNode(tag="img", value="", props={"src":f"{text_node.url}", "alt":f"{text_node.text}"})
        case _:
            return "Error: unsupported tag.\n I could assume you wanted blank text, but you know what happens when we ASSuME. \n" 
