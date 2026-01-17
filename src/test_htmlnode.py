import unittest

from htmlnode import *

"""
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

"""

class TestHtmlNode(unittest.TestCase):
    def test_create_html_obj_default(self):
        node = HtmlNode() 
        self.assertEqual(node.value, None)

    def test_props(self):
        node = HtmlNode(None, None, None,
               {
                "href": "https://www.google.com",
                "target": "_blank",
               })
        node1 = node.props_to_html()
        node2 = ' href="https://www.google.com" target="_blank"' 
        self.assertEqual(node1, node2)        

    def test_props(self):
        node = HtmlNode(None, None, None,
               {
                "href": "https://www.google.com",
                "target": "_blank",
               })
        node1 = node.props_to_html()
        node2 = ' href=https://www.google.com target="_blank"' 
        self.assertNotEqual(node1, node2)        

    def test_tags_equal(self):
        node1 = HtmlNode("<b>")
        self.assertEqual(node1.tag, "<b>")


    def test_tags_neq(self):
        node1 = HtmlNode("<b>")
        node2 = HtmlNode("<i>", None, None)
        self.assertNotEqual(node1.tag, node2.tag)


if __name__ == "__main__":
    unittest.main()
