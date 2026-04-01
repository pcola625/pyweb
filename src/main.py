import sys
from textnode import *
from fyle_copier import *
from generate_page import *

def main():
    print("Hello, Girls!")

    static_dir = "./static"
    content_dir = "./content"
    public_dir = "./docs"
    template_path = "./template.html"

    # new bit to get a basepath
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    fyle_copy_all(static_dir, public_dir)

    #generate_page(from_path="content/index.md", template_path="template.html", dest_path="public")
    generate_pages_r(content_dir, template_path, public_dir, basepath)

if __name__ == "__main__":
    main()
