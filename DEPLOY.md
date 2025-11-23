# DataSense - Deployment Guide

## Quick Deploy to Render (Free)

1. **Push to GitHub**
   ```bash
   cd datasense_ap
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Deploy on Render**
   - Go to [render.com](https://render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Settings:
     - **Name**: datasense-ap
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
   - Click "Create Web Service"

3. **Done!** Your app will be live at `https://datasense-ap.onrender.com`

## Alternative: Railway

```bash
npm i -g @railway/cli
railway login
railway init
railway up
```

## Alternative: Heroku

```bash
heroku create datasense-ap
git push heroku main
```

## Environment Variables

No environment variables required - uses PORT from platform.

## Files for Deployment

- ✅ `Procfile` - Heroku deployment config
- ✅ `runtime.txt` - Python version
- ✅ `requirements.txt` - Dependencies (includes gunicorn)
- ✅ `.gitignore` - Ignore cache files

## Test Deployed App

```bash
curl https://your-app.onrender.com/
curl https://your-app.onrender.com/json-params
curl https://your-app.onrender.com/analytics-list
```

## Cost

All three platforms offer **free tiers**:
- Render: Free (sleeps after 15min inactivity)
- Railway: $5 free credit/month
- Heroku: Limited free dyno hours
