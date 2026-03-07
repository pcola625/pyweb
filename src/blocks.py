import string
import re
from enum import Enum

BlockType = Enum("BlockType",
                  [ "paragraph"
        ,"heading"
        ,"code"
        ,"quote"
        ,"unordered_list"
        ,"ordered_list"
])

def block_to_block_type(block):
    if block is None or len(block) == 0:
        return None

    #print(f"{block}")
    # regex for 1-6 hash marks ^#{1,6}
    if re.search(r'^#{1,6}.*', block):
        return BlockType.heading
    elif block.startswith("```\n") and block.endswith("```"):
        return BlockType.code
    else:
        lines = block.splitlines()

        if all(line.startswith(">") for line in lines):
            return BlockType.quote
        elif all(line.startswith("- ") for line in lines):
            return BlockType.unordered_list
        else:
            start_at_one = 1
            still_true = True
            for line in lines:
                if line == "\n":
                    continue
                #print(f"Looking at {line}, still true? {still_true}")
                if line.startswith(f"{start_at_one}. ") and still_true:
                    start_at_one += 1
                else:
                    still_true = False
                    break
            if still_true:
                return BlockType.ordered_list

    #and if you got here, there is only one other choice
    return BlockType.paragraph


def markdown_to_blocks(text):
    blocks = []

    if text is None or len(text) == 0:
        return blocks

    tmpBlockos = text.split("\n\n")

    for block in tmpBlockos:
        block = block.strip()
        if len(block) == 0 or block[0] == "\n":
            continue
        blocks.append(block)
    return blocks