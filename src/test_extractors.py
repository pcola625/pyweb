import unittest

from extractors import *
class TestExtractor(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_extract_title_simple(self):
        example = "# This is a title"
        title = extract_title(example)
        self.assertEqual("This is a title", title)

    def test_extract_title_too_many_hash(self):
        example = "### This is a title"
        try:
            title = extract_title(example)
        except ValueError as e:
            self.assertIsInstance(e, ValueError)

    def test_extract_title_too_few_hash(self):
        example = "This is a title"
        try:
            title = extract_title(example)
        except ValueError as e:
            self.assertIsInstance(e, ValueError)

if __name__ == "__main__":
    unittest.main()
