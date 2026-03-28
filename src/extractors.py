import re

def extract_markdown_images(text):
    match_this = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return match_this


def extract_markdown_links(text):
    return_tuple = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return return_tuple

def extract_title(markdown):
    title = ""
    pattern = r"^#([^#\n]|$)"

    matches = re.findall(pattern, markdown, re.MULTILINE)
    if not matches:
        raise ValueError(f"Could not extract title from {markdown}")

    title = markdown.split("#")[1].strip()
    return title