import markdown

def file_converter(inputpath, outputpah):
    with open(inputpath, 'r') as f:
        md =f.read()
    html = markdown.markdown(md)
    with open(outputpah, 'w') as f:
        f.write(html)

