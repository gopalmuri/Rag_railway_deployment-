import sys

# Read the file
with open(r'e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\landing.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the line with "</section>" after features (around line 1495)
insert_index = None
for i, line in enumerate(lines):
    if i >= 1494 and '</section>' in line and i < 1500:
        insert_index = i + 1
        break

if insert_index is None:
    print("Could not find insertion point")
    sys.exit(1)

# Content to insert
use_cases_section = '''
    <!-- Use Cases Section -->
    <section class="section-padding" style="background: rgba(255,255,255,0.01);">
        <h2 class="section-title reveal-text">Perfect for <span>Every Use Case</span></h2>
        <div class="features-grid" style="max-width: 1200px; margin: 0 auto;">
            <div class="feature-card reveal-up magnetic-trigger" style="transition-delay: 0.1s">
                <i class="fas fa-graduation-cap feature-icon"></i>
                <div class="feature-title">Students & Researchers</div>
                <p style="color:#94a3b8">Understand textbooks, research papers, and lecture notes instantly. Get precise answers with exact page references for citations.</p>
            </div>
            <div class="feature-card reveal-up magnetic-trigger" style="transition-delay: 0.2s">
                <i class="fas fa-briefcase feature-icon"></i>
                <div class="feature-title">Teams & Businesses</div>
                <p style="color:#94a3b8">Search internal documents, policies, and reports effortlessly. Onboard faster and find answers without asking colleagues.</p>
            </div>
            <div class="feature-card reveal-up magnetic-trigger" style="transition-delay: 0.3s">
                <i class="fas fa-code feature-icon"></i>
                <div class="feature-title">Developers</div>
                <p style="color:#94a3b8">Query technical documentation, API references, and codebases. Navigate complex docs with AI-powered semantic search.</p>
            </div>
        </div>
    </section>

'''

# Insert the content
lines.insert(insert_index, use_cases_section)

# Write back
with open(r'e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\landing.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"Successfully inserted Use Cases section at line {insert_index}")
