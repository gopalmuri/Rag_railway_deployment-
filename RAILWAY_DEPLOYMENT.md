# Railway Deployment Guide for AI Document Assistant RAG

## 🚀 Quick Deploy to Railway

### Prerequisites
1. Railway account (https://railway.app)
2. GitHub account
3. Your Groq API Key

---

## 📋 Step-by-Step Deployment

### Step 1: Push Code to GitHub ✅ (DONE)
Your code is already in: `https://github.com/gopalmuri/Rag_railway_deployment-.git`

### Step 2: Create Railway Project

1. Go to https://railway.app
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose: `gopalmuri/Rag_railway_deployment-`
5. Railway will auto-detect the configuration

### Step 3: Add MySQL Database

1. In your Railway project dashboard, click **"+ New"**
2. Select **"Database"** → **"Add MySQL"**
3. Railway will create a MySQL instance
4. Copy the connection details (they'll appear in the database service)

### Step 4: Configure Environment Variables

In Railway project → **Variables** tab, add these:

```bash
# Required Variables
DEBUG=False
SECRET_KEY=your-super-secret-key-change-this-now
ALLOWED_HOSTS=.railway.app

# Database (Railway MySQL - AUTO-PROVIDED)
# These will be automatically available from Railway MySQL:
# MYSQLHOST, MYSQLDATABASE, MYSQLUSER, MYSQLPASSWORD, MYSQLPORT
# We need to map them:
DB_ENGINE=django.db.backends.mysql
DB_NAME=${{MYSQLDATABASE}}
DB_USER=${{MYSQLUSER}}
DB_PASSWORD=${{MYSQLPASSWORD}}
DB_HOST=${{MYSQLHOST}}
DB_PORT=${{MYSQLPORT}}

# API Keys (REQUIRED)
GROQ_API_KEY=your-groq-api-key-here
GOOGLE_API_KEY=your-google-gemini-key-optional

# Security
CSRF_TRUSTED_ORIGINS=https://${{RAILWAY_PUBLIC_DOMAIN}}
```

### Step 5: Deploy!

1. Railway will automatically deploy after you set variables
2. First deploy takes ~5-10 minutes (downloads ML models)
3. Check logs for any errors
4. Once deployed, click **"Open App"** to view your site

---

## 🔧 Important Notes

### Memory Configuration
Your app needs **at least 2GB RAM** due to ML models:
- Sentence Transformers: ~150MB
- spaCy: ~50MB
- ChromaDB: ~100-200MB
- Django + Runtime: ~200-300MB

**Railway Plan Recommendation**: Hobby ($5/month) or higher

### Storage
- ChromaDB vector database persists in `/mainfolder/chroma_db`
- Uploaded PDFs in `/mainfolder/uploaded_pdfs`
- Railway provides persistent volumes

### First Time Setup
After deployment, run migrations:
```bash
# Railway will auto-run this via railway.json config
python manage.py migrate
python manage.py collectstatic --noinput
```

---

## 🐛 Troubleshooting

### Build Fails
- **Check**: Python version (should be 3.10)
- **Check**: All requirements installing correctly
- **Fix**: Look at Railway build logs

### Database Connection Error
- **Check**: Environment variables are set correctly
- **Check**: MySQL service is running
- **Fix**: Use Railway's auto-provided MySQL variables

### Static Files Not Loading
- **Check**: `STATIC_ROOT` is set
- **Check**: WhiteNoise middleware is active
- **Fix**: Run `python manage.py collectstatic`

### Memory Issues
- **Upgrade to Hobby plan** (2GB RAM minimum)
- **Or optimize**: Remove unused models

---

## 💰 Expected Costs

**Starter Setup**:
- Web Service: ~$5-10/month
- MySQL Database: ~$5/month
- **Total: ~$10-15/month**

**With Optimizations** (pgvector instead of ChromaDB):
- Could reduce to ~$5-8/month

---

## 🎯 Post-Deployment

1. **Test the app**: Upload a PDF and ask questions
2. **Monitor logs**: Check for any errors
3. **Set up domain** (optional): Railway provides custom domains
4. **Enable metrics**: Monitor memory and CPU usage

---

## 📞 Need Help?

- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- Project Issues: https://github.com/gopalmuri/Rag_railway_deployment-/issues

---

## ✅ Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] Railway project created
- [ ] MySQL database added
- [ ] Environment variables configured
- [ ] GROQ_API_KEY added
- [ ] First deployment successful
- [ ] Tested PDF upload
- [ ] Tested question answering

---

**Ready to Deploy!** 🚀
