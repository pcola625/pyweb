from extractors import *
from fyle_copier import *
from markdown_to_html_node import markdown_to_html_node

def generate_pages_r(from_path, template_path, dest_path):

    for file in os.listdir(from_path):
        if not os.path.isfile(os.path.join(from_path, file)):
            print(f"File {file} is directory, we need to go deeper")
            generate_pages_r(os.path.join(from_path, file), template_path, os.path.join(dest_path, file))
        if file.endswith(".md"):
            from_path = from_path + "/" + file
            generate_page(from_path, template_path, dest_path)

    return
def generate_page(from_path: object, template_path: object, dest_path: object) -> None:

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    try:
        md_file_handle = open(from_path, "r")
        md_content = md_file_handle.read()
        md_file_handle.close()

        print(f"Read  {from_path}")

        template_file_handle = open(template_path, "r")
        template_content = template_file_handle.read()
        template_file_handle.close()

        print(f"Read  {template_path}")

        le_content = markdown_to_html_node(md_content).to_html()
        print(f" {le_content}")
        le_title = extract_title(md_content)

        template_content = template_content.replace("{{ Title }}", le_title)
        template_content = template_content.replace("{{ Content }}", le_content)

        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

        new_index_file = open(dest_path + "/index.html", "w")
        new_index_file.write(template_content)
        new_index_file.close()
    
    except Exception as e:
        print(f"Something bad happened in generate_page {e}")

    return