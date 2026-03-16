from htmlnode import HtmlNode
from blocks import *
from leafnode import LeafNode
from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


def format_heading_block(text):

    return
def markdown_to_html_node(markdown):

    blocks = markdown_to_blocks(markdown)
    childrens_blocks = []
    #print(f'blocks: {blocks}')
    for block in blocks:
        #fixed_block = ParentNode("div", [],None)
        match block_to_block_type(block):
            case BlockType.heading:
                level = 0
                for char in block:
                    if char == "#":
                        level += 1
                    else:
                        break
                if level + 1 >= len(block):
                    raise ValueError(f"invalid heading level: {level}")
                text = block[level + 1:]
                children = text_to_children(text)
                childrens_blocks.append(ParentNode(f"h{level}", children))
            case BlockType.paragraph:
                #print(f'in the paragraph type')
                tag = "p"
                block = block.split("\n")
                junk = " ".join(block)
                #print(f'junk: {junk}')
                children = text_to_children(junk)
#                print(f'block: {junk}, children: {children}')
                childrens_blocks.append(ParentNode(tag,children))
            case BlockType.code:
                tag = "code"
                children = block[4:-3]
                child_node = text_node_to_html_node(TextNode(children, TextType.TEXT))
                childrens_blocks.append(ParentNode("pre", [ParentNode(tag, [child_node], None)]))
            case BlockType.quote:
                tag = "blockquote"
                block = block.split("\n")
                new_lines = []
                for line in block:
                    if not line.startswith(">"):
                        raise ValueError("invalid quote block")
                    new_lines.append(line.lstrip(">").strip())
                quote = " ".join(new_lines)
                quote_nodes = text_to_children(quote)
                childrens_blocks.append(ParentNode(tag,quote_nodes, None))

            case BlockType.unordered_list:
                tag = "ul"
                block = block.split("\n")
                new_lines = []
                grandchildren = []
                for line in block:
                    if not line.startswith("-"):
                        raise ValueError("invalid unordered list block")
                    new_lines.append(line.lstrip("- ").strip())
                for line in new_lines:
                    grandchildren.append(ParentNode("li",text_to_children(line),None))
                childrens_blocks.append(ParentNode(tag,grandchildren,None))
            case BlockType.ordered_list:
                tag = "ol"
                block = block.split("\n")
                new_lines = []
                grandchildren = []
                x = 1
                #print(f"Debug, what is {block}")
                for line in block:
                    if not line.startswith(f"{x}. "):
                        raise ValueError("invalid ordered list block")
                    new_lines.append(line.lstrip(f"{x}. ").strip())
                    x +=1
                #print(f"Debug, what is new_lines {new_lines}")
                for line in new_lines:
                    grandchildren.append(ParentNode("li", text_to_children(line), None))
                    #print(f"Debug, added to grandchildren {line}")


                childrens_blocks.append(ParentNode(tag,grandchildren))
                #print(f"Debug, what is childrens_blocks rn {childrens_blocks[0]}")
            case _:
                #print(f'I guess it went to the default')
                break

        #childrens_blocks.append(fixed_block)
       # print(f'new_blocks: {childrens_blocks}')

    return ParentNode("div", childrens_blocks,None)

def text_to_children(text):
    children = text_to_textnodes(text)
    html_list = []
    #print(f'children: {children}')
    for child in children:
        html_list.append(text_node_to_html_node(child))
    return html_list

