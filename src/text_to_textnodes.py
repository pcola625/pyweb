from split_nodes_delimiter import *
from split_nodes_links_and_images import *

def text_node_to_html_node(text_node):
    if text_node is None:
        return None

def text_to_textnodes(text):
    textnodes_list = []

    if text is not None:
        nodes = [TextNode(text, TextType.TEXT)]
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "_", TextType.ITAL)
        nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        nodes = split_nodes_image(nodes)
        nodes = split_nodes_link(nodes)
        return nodes
    return textnodes_list