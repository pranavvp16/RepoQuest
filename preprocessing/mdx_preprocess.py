import markdown
from unstructured.partition import html

def process_mdx(filepath):
    with open(filepath, "r") as mdx_file:
        mdx_content = mdx_file.read()
        html_content = markdown.markdown(mdx_content)

    with open("output.html", "w") as html_file:
        html_file.write(html_content)

