from htmlnode import *
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return_list = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            return_list.append(old_node)
            continue
        split_list =[]
        candidates = old_node.text.split(delimiter)
       # print(f"{candidates}")

        """
        If a matching closing delimiter is not found, just raise an exception with a 
        helpful error message, that's invalid Markdown syntax.
        always gonna be odd if there was anything split... 
        
        """
        if  len (candidates)%2 == 0:
            raise ValueError("No matching closing delimiter found - invalid Markdown syntax\n")

        for i in range(len(candidates)):
            if candidates[i] == "":
                continue
            if i % 2 == 0:
                split_list.append(TextNode(candidates[i], TextType.TEXT))
            else:
                split_list.append(TextNode(candidates[i], text_type))
        return_list.extend(split_list)
    return return_list