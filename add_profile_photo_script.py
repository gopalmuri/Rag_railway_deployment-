import re

# Read the navbar file
with open(r'e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\components\navbar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# JavaScript code to add
profile_photo_script = '''
<script>
  // Load user profile photo in navbar
  (function() {
    const navAvatarImg = document.getElementById('navAvatarImg');
    const navAvatarInitials = document.getElementById('navAvatarInitials');
    
    if (navAvatarImg && navAvatarInitials) {
      // Fetch user profile data
      fetch('/api/auth/me/')
        .then(res => res.json())
        .then(data => {
          if (data.profile_photo) {
            // Show profile photo
            navAvatarImg.src = data.profile_photo;
            navAvatarImg.style.display = 'block';
            navAvatarInitials.style.display = 'none';
          }
        })
        .catch(err => {
          console.log('Profile photo not available, showing initials');
          // Keep showing initials on error
        });
    }
  })();
</script>
'''

# Add the script before the closing </nav> tag
content = content.replace('</nav>', profile_photo_script + '</nav>')

# Write back
with open(r'e:\AIDocumentAssistantRAG\mainfolder\frontend\templates\ragapp\components\navbar.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Successfully added profile photo loading script to navbar component")
