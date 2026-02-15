import os
import re

files_to_update = [
    r"e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\upload.html",
    r"e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\profile.html",
    r"e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\pdf_viewer.html",
    r"e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\password_change.html",
    r"e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\history.html",
    r"e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\favorites.html",
    r"e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\dashboard.html",
    r"e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\chat.html"
]

new_version = "?v=20251217"

for file_path in files_to_update:
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Regex to find main.js import with any query parameter
    # e.g. src="{% static 'ragapp/main.js' %}?v=26"
    # or src="{% static 'ragapp/main.js' %}"
    
    # We want to replace whatever follows the static block ending until the closing quote
    # Pattern: ({% static 'ragapp/main.js' %})(\?v=[0-9]+)?
    
    pattern = r"({% static 'ragapp/main.js' %})(\?v=[a-zA-Z0-9_]+)?"
    
    def replacement(match):
        return f"{match.group(1)}{new_version}"
    
    new_content, count = re.subn(pattern, replacement, content)
    
    if count > 0:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {file_path} (Replaced {count} instances)")
    else:
        print(f"No match found in {file_path}")
