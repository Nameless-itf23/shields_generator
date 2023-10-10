import base64

name = "example"
file_path = "./ico/GitHub.ico"
url = "https://github.com/"

def image_file_to_base64(file_path):
    with open(file_path, "rb") as image_file:
        data = base64.b64encode(image_file.read())
    return data.decode('utf-8')

with open('output.md', 'w') as f:
    f.write(f'[![{name}](https://img.shields.io/badge/--FFFFFF?style=social&logo=data:image/vnd.microsoft.icon;base64,{image_file_to_base64(file_path)}&label={name})]({url})')