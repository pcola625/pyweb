
import unittest

from textnode import *

class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_bold(self):
        node = TextNode("This node makes bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This node makes bold")

    def test_bold_expanded(self):
        node = TextNode("This node makes bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.to_html(),"<b>This node makes bold</b>")

    def test_italic_expanded(self):
        node = TextNode("This node makes italic", TextType.ITAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.to_html(),"<i>This node makes italic</i>")

    def test_code_block(self):
        node = TextNode("This node makes a code block", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.to_html(),"<code>This node makes a code block</code>")

    def test_href(self):
        node = TextNode("This node makes a link", TextType.LINKS, "http://127.0.0.1:8080")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.to_html(),'<a href="http://127.0.0.1:8080">This node makes a link</a>')

    def test_img(self):
        node = TextNode("This node makes an image link", TextType.IMG, "http://smiley.gov/smiley.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.to_html(),'<img src="http://smiley.gov/smiley.jpg" alt="This node makes an image link"></img>')


if __name__ == "__main__":
    unittest.main()
