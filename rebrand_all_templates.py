import os
import re

# List of template files to update
template_files = [
    r'e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\dashboard.html',
    r'e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\chat.html',
    r'e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\pdf_viewer.html',
    r'e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\profile.html',
    r'e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\history.html',
    r'e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\favorites.html',
    r'e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\components\navbar.html',
]

total_replacements = 0

for file_path in template_files:
    if not os.path.exists(file_path):
        print(f"Skipping {os.path.basename(file_path)} - file not found")
        continue
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count occurrences
    docassistant_ai_count = content.count('DocAssistant.ai')
    docassistant_count = content.count('DocAssistant')
    
    if docassistant_count == 0:
        print(f"Skipping {os.path.basename(file_path)} - no instances found")
        continue
    
    # Replace all occurrences
    content = content.replace('DocAssistant.ai', 'DocQuery.ai')
    content = content.replace('DocAssistant', 'DocQuery')
    
    # Also update any references to "AI Document Assistant"
    content = content.replace('AI Document Assistant', 'DocQuery.ai')
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    file_total = docassistant_count
    total_replacements += file_total
    print(f"✓ {os.path.basename(file_path)}: {file_total} replacements")

print(f"\n✅ Total replacements across all files: {total_replacements}")
