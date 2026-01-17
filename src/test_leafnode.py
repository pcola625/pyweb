import unittest

from leafnode import *

class TestHtmlNode(unittest.TestCase):
    def test_create_leafnode(self):
        node = LeafNode("b", "no op") 
        node2 = LeafNode("b", "no op", None)
        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.value, node2.value)
    
    def test_simply(self):
        node = LeafNode("b", "no op")
        self.assertEqual(node.to_html(),"<b>no op</b>")

    def test_with_some_props(self):
        node = LeafNode("i", "this ought be in italics", {"href": "https://www.google.com"}).to_html()
        node2 ='<i href="https://www.google.com">this ought be in italics</i>'
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
