import re

def extract_markdown_images(text):
    match_this = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return match_this


def extract_markdown_links(text):
    return_tuple = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return return_tuple

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
        raise ValueError("no title found")
