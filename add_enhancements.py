import re

# Read the file
with open(r'e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\landing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS for hero-micro-line (insert after .hero-char.visible:hover style)
css_insert_pattern = r'(\.hero-char\.visible:hover \{[^}]+\})'
css_to_add = r'''\1

        .hero-micro-line {
            font-size: 16px;
            color: var(--accent-neon);
            font-weight: 500;
            max-width: 600px;
            margin: 20px auto 30px;
            opacity: 0;
            animation: fadeInUp 0.8s forwards 1s;
            text-align: center;
            letter-spacing: 0.5px;
        }'''

content = re.sub(css_insert_pattern, css_to_add, content, count=1)

# 2. Add FAQ question about ChatGPT (find the last FAQ card and add after it)
faq_pattern = r'(</div>\s+</div>\s+</div>\s+</section>\s+<!-- Mid-Page CTA -->)'
faq_to_add = r'''</div>
            </div>
            <div class="faq-card">
                <div class="faq-header">
                    <h3>How is DocAssistant different from ChatGPT?</h3><i class="fas fa-plus faq-icon"></i>
                </div>
                <div class="faq-body">
                    <p>DocAssistant responds strictly from your uploaded documents with exact citations, ensuring accuracy and privacy. Unlike ChatGPT, it doesn't rely on general knowledge or training data—only your files—eliminating hallucinations and providing verifiable, source-grounded answers.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Mid-Page CTA -->'''

content = re.sub(faq_pattern, faq_to_add, content, count=1)

# 3. Update RAG animation step labels
content = content.replace('data-label="Upload"', 'data-label="Upload Document"')
content = content.replace('data-label="Vectorize"', 'data-label="Process & Index"')
content = content.replace('data-label="Retrieve"', 'data-label="Retrieve Context"')
content = content.replace('data-label="Generate"', 'data-label="Generate Answer"')

# Write back
with open(r'e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\landing.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully added:")
print("1. CSS for hero-micro-line")
print("2. FAQ question about ChatGPT")
print("3. Updated RAG animation step labels")
