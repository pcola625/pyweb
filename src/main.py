from textnode import *
from fyle_copier import *
from generate_page import *

def main():
    print("Hello, Girls!")

#    chuckist_conspiracy = TextNode("This is a text",TextType.LINKS, "https://127.0.0.1"  )
#    print(chuckist_conspiracy)

    fyle_copy_all("static","public")

    #generate_page(from_path="content/index.md", template_path="template.html", dest_path="public")
    generate_pages_r("content","template.html","public")
if __name__ == "__main__":
    main()
