import re

# Read the file
with open(r'e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\landing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Count occurrences before replacement
docassistant_count = content.count('DocAssistant')
docassistant_ai_count = content.count('DocAssistant.ai')

# Replace all occurrences
# Replace "DocAssistant.ai" first (more specific)
content = content.replace('DocAssistant.ai', 'DocQuery.ai')

# Then replace standalone "DocAssistant" 
content = content.replace('DocAssistant', 'DocQuery')

# Write back
with open(r'e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\landing.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully rebranded landing page:")
print(f"  - Replaced {docassistant_ai_count} occurrences of 'DocAssistant.ai' with 'DocQuery.ai'")
print(f"  - Replaced {docassistant_count - docassistant_ai_count} occurrences of 'DocAssistant' with 'DocQuery'")
print(f"  - Total replacements: {docassistant_count}")
