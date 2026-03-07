import unittest

import blocks
from blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdowns(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_simple(self):
        md = ""
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            None
        )
    def test_b_to_b_heading_1_hash(self):
        md = "# heading1\n"
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockType.heading
        )

    def test_b_to_b_heading_6_hash(self):
        md = "###### heading6\n"
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockType.heading
        )
    def test_b_to_b_heading_hash_but_garbage(self):
        md = "heading6 #####\n"
        blocks = block_to_block_type(md)
        self.assertNotEqual(
            blocks,
            BlockType.heading
        )
    def test_b_to_b_garbage_hash_must_be_paragraph(self):
        md = "heading6 #####\n"
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockType.paragraph
        )
    def test_b_to_b_code_blocks_defa(self):
        md = """```\n
this is a boat load of code\n
I mean it is really going to  go several\n
lines\n
and frankly not sure what it will do\n
```"""
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockType.code
        )

    def test_b_to_b_broken_ordered_list(self):
        md = """
1. chicken\n
2.fish\n
4. no-one expects the you-know-what\n
"""
        blocks = block_to_block_type(md)
        self.assertNotEqual(
            blocks,
            BlockType.ordered_list
        )
    def test_b_to_b_proper_ordered_list(self):
        md = ("""1. fear
2. surprise
3. an almost fanatical devotion to...""")
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockType.ordered_list
        )

    def test_b_to_b_simple_quotes(self):
        md = """> Here is a multiline quote
> Even if there is some that has doubles
>> like a really long bunch between a few 
>> people
> and going back and forth"""
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockType.quote
        )

    def test_b_to_b_simple_uo_list(self):
        md = """- Here is a multiline unordered list
- Like you might see on a powerpoint
- a real long snorer 
- pageturner, white knuckler
- and going back and forth"""
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockType.unordered_list
        )

    def test_b_to_b_broken_uo_list(self):
        md = """- Here is a multiline unordered list
-Like you might see on a powerpoint
- a real long snorer 
- pageturner, white knuckler
- and going back and forth"""
        blocks = block_to_block_type(md)
        self.assertNotEqual(
            blocks,
            BlockType.unordered_list
        )

    def test_b_to_b_one_more_broken_uo_list(self):
        md = """-Here is a multiline unordered list
-Like you might see on a powerpoint
a real long snorer 
- pageturner, white knuckler
- and going back and forth"""
        blocks = block_to_block_type(md)
        self.assertNotEqual(
            blocks,
            BlockType.unordered_list
        )


if __name__ == "__main__":
    unittest.main()