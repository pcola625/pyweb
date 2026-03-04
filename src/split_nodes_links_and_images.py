from htmlnode import *
from textnode import *
from extractors import *

def split_nodes_image(old_nodes):
    return_list = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            return_list.append(old_node)
            continue
        orig_text = old_node.text
        extract_stuff = extract_markdown_images(orig_text)
        if len(extract_stuff) == 0:
            return_list.append(old_node)
            continue
        else:
            for image in extract_stuff:
                sections = orig_text.split(f"![{image[0]}]({image[1]})", 1)
                if len(sections) != 2:
                    raise ValueError("invalid markdown, image section not closed")
                if sections[0] != "":
                    return_list.append(TextNode(sections[0], TextType.TEXT))
                return_list.append(
                        TextNode(
                            image[0],
                            TextType.IMG,
                            image[1],
                        )
                    )
                orig_text = sections[1]
            if orig_text != "":
                return_list.append(TextNode(orig_text, TextType.TEXT))
    return return_list

def split_nodes_link(old_nodes):
    return_list = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            return_list.append(old_node)
            continue
        orig_text = old_node.text
        extract_stuff = extract_markdown_links(orig_text)
        if len(extract_stuff) == 0:
            return_list.append(old_node)
            continue
        for link in extract_stuff:
            sections = orig_text.split(f"[{link[0]}]({link[1]})", 1)
        if len(sections) != 2:
            raise ValueError("invalid markdown, link section not closed")
        if sections[0] != "":
            return_list.append(TextNode(sections[0], TextType.TEXT))
        return_list.append(TextNode(link[0], TextType.LINKS, link[1]))
        orig_text = sections[1]
        if orig_text != "":
            return_list.append(TextNode(orig_text, TextType.TEXT))

    return return_list