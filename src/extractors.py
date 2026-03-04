import re

def extract_markdown_images(text):
    match_this = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return match_this


def extract_markdown_links(text):
    return_tuple = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return return_tuple

