import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq_types(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITAL)
        self.assertNotEqual(node, node2)


    def test_None_same_as_blank(self):
        node = TextNode("This is a text node", TextType.ITAL, None)
        node2 = TextNode("This is a text node", TextType.ITAL)
        self.assertEqual(node, node2)

    def test_inequal_text_nodes_case(self):
        node = TextNode("THIS is a text node", TextType.ITAL)
        node2 = TextNode("This is a text node", TextType.ITAL)
        self.assertNotEqual(node, node2)

    def test_inequal_text_nodes_1(self):
        node = TextNode("That is a text node", TextType.ITAL)
        node2 = TextNode("This is a text node", TextType.ITAL)
        self.assertNotEqual(node, node2)

    def test_inequal_text_nodes_unicode(self):
        node = TextNode("That is a text node 😆", TextType.ITAL)
        node2 = TextNode("This is a text node 🤬", TextType.ITAL)
        self.assertNotEqual(node, node2)

    def test_equal_text_nodes_unicode(self):
        node = TextNode("That is a text node 🤬", TextType.ITAL)
        node2 = TextNode("That is a text node 🤬", TextType.ITAL)
        self.assertEqual(node, node2)

    def test_equal_urls(self):
        node = TextNode("That is a text node 🤬", TextType.ITAL, "https://127.0.0.1")
        node2 = TextNode("That is a text node 🤬", TextType.ITAL, "https://127.0.0.1")
        self.assertEqual(node, node2)
if __name__ == "__main__":
    unittest.main()
