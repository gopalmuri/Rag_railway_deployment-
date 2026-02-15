import re

file_path = r"C:\Users\gopal\.gemini\antigravity\brain\40977b7a-6a32-4b4f-90e9-1bec31d5b1d0\walkthrough.md"
# Using forward slashes for the path in markdown usually works best or file URI
base_dir = "/C:/Users/gopal/.gemini/antigravity/brain/40977b7a-6a32-4b4f-90e9-1bec31d5b1d0/"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

def replace_link(match):
    alt = match.group(1)
    url = match.group(2)
    # If it is just a filename (no slash), prepend base_dir
    if "/" not in url and "\\" not in url:
        return f"![{alt}]({base_dir}{url})"
    return match.group(0)

new_content = re.sub(r"!\[(.*?)\]\((.*?)\)", replace_link, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)
