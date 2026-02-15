import re

# Read the file
with open(r'e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\landing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the RAG animation JavaScript to add rotating queries
# Pattern to find the query typing section
old_query_pattern = r'(// Type query\s+const query = )"[^"]+";'
new_query_code = r'''\1[
                    "Explain renewable energy benefits",
                    "What are the key findings in this research?",
                    "Summarize the API documentation",
                    "How do I implement authentication?"
                ][Math.floor(Math.random() * 4)];'''

content = re.sub(old_query_pattern, new_query_code, content, count=1)

# Improve the typing animation by adding proper spacing
# Find the typing loop and update it
old_typing_pattern = r'(for \(let i = 0; i < query\.length; i\+\+\) \{\s+ragTypeTarget\.innerText \+= query\[i\];\s+await wait\()(\d+)(\);)'
new_typing_code = r'\g<1>40\g<3>  // Natural typing speed'

content = re.sub(old_typing_pattern, new_typing_code, content, count=1)

# Write back
with open(r'e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\landing.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully improved RAG animation:")
print("1. Added rotating example queries")
print("2. Adjusted typing speed for natural rhythm")
