# GitHub Pages Setup Guide

## ✅ Your Site is GitHub Pages Compatible!

Your website is **100% compatible** with GitHub Pages. The issue you're experiencing locally is actually **NOT a problem** on GitHub Pages.

## 🔍 Why JSON Files Don't Load Locally

When you open `index.html` directly in your browser (using `file://` protocol), browsers block loading JSON files due to **CORS (Cross-Origin Resource Sharing) security restrictions**. This is a browser security feature, not a problem with your code.

**Good News**: GitHub Pages serves your files over **HTTP/HTTPS**, which doesn't have these restrictions. Your JSON files will load perfectly on GitHub Pages!

## 🧪 Test Locally (Before Deploying)

To test your site locally and verify everything works, use a local web server:

### Option 1: Python (Recommended)
```bash
# Python 3
python3 -m http.server 8000

# Then visit: http://localhost:8000
```

### Option 2: Node.js
```bash
# Install serve globally (first time only)
npm install -g serve

# Run server
serve

# Or specify port
serve -p 8000
```

### Option 3: VS Code Live Server Extension
1. Install "Live Server" extension in VS Code
2. Right-click on `index.html`
3. Select "Open with Live Server"

## 🚀 Deploy to GitHub Pages

### Step 1: Create GitHub Repository
1. Go to https://github.com/new
2. Create a new repository (e.g., `thelooongweekend`)
3. **Don't initialize** with README (if your site is already set up)

### Step 2: Upload Your Files
```bash
# Navigate to your project folder
cd /Users/ugoyal3/Desktop/utsav/my/site

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit"

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages
1. Go to your repository on GitHub
2. Click **Settings** tab
3. Scroll down to **Pages** section (left sidebar)
4. Under **Source**, select:
   - **Branch**: `main`
   - **Folder**: `/` (root)
5. Click **Save**

### Step 4: Access Your Site
Your site will be live at:
```
https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/
```

**Note**: It may take a few minutes for the site to be available. GitHub will show the URL once it's ready.

## 📝 Important Notes for GitHub Pages

### ✅ What Works Perfectly
- ✅ All HTML, CSS, JavaScript
- ✅ JSON file loading (`fetch()` API)
- ✅ All relative paths
- ✅ Images and assets
- ✅ Dynamic content loading

### ⚠️ Contact Form
Your contact form currently only validates but doesn't send emails. To enable email sending on GitHub Pages, you'll need to integrate a service:

**Option 1: Formspree** (Easiest)
1. Sign up at https://formspree.io
2. Get your form endpoint URL
3. Update `contact.html` form action:
   ```html
   <form id="contact-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   ```

**Option 2: EmailJS**
- Free tier: 200 emails/month
- See `CONTACT_FORM_SETUP.md` for detailed instructions

### 🗑️ Files Not Needed on GitHub Pages
These development scripts aren't needed for the live site (but you can keep them):
- `import_instagram.py`
- `auto-organize-images.py`
- `analyze-and-organize.py`

You can keep them in your repo, or add them to `.gitignore` if you don't want them deployed.

## 🎯 Quick Start Checklist

- [ ] Test locally with a web server (see above)
- [ ] Create GitHub repository
- [ ] Push code to GitHub
- [ ] Enable GitHub Pages in repository settings
- [ ] Wait 2-5 minutes for deployment
- [ ] Visit your live site URL
- [ ] Verify JSON data loads correctly
- [ ] Test all pages and links
- [ ] (Optional) Set up Formspree for contact form

## 🔧 Troubleshooting

### JSON files still not loading?
- Make sure you're using a web server (not opening file directly)
- Check browser console for errors
- Verify JSON file paths are correct (should be relative: `data/tours.json`)

### Site not updating?
- GitHub Pages can take 1-5 minutes to update after pushing
- Make sure you committed and pushed your changes
- Hard refresh your browser (Ctrl+Shift+R or Cmd+Shift+R)

### 404 errors?
- Make sure all file paths use relative paths (not absolute)
- Verify all files were committed and pushed to GitHub
- Check that `index.html` is in the root directory

## 📚 Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Formspree Setup](https://formspree.io/guides)
- [Contact Form Guide](./CONTACT_FORM_SETUP.md)

Your site will work perfectly on GitHub Pages! The local issue you're seeing is just a browser security feature that won't affect your live site.

