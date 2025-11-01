# Instagram Content Import - Complete Guide

Follow these steps to import photos and content from your Instagram page (https://www.instagram.com/the.looong.weekend/) into your website.

## 📥 Step 1: Download Instagram Photos

### Manual Download Method:
1. Go to https://www.instagram.com/the.looong.weekend/
2. Open each post you want to use
3. Right-click on the image → "Save Image As..."
4. Save with descriptive names like:
   - `kerala-backwaters-1.jpg`
   - `goa-beach-sunset.jpg`
   - `himachal-mountain-trek.jpg`

### Organize Photos:
Place downloaded images in appropriate folders:
- **Tours**: `assets/images/tours/` - Photos of actual tours/experiences
- **Destinations**: `assets/images/destinations/` - Location photos
- **Gallery**: `assets/images/gallery/` - General photos for gallery page

## 📝 Step 2: Extract Content Information

For each Instagram post, note down:
- **Caption/Description**: Copy the full caption
- **Location**: Where was the photo taken?
- **Tour Name**: If it's a specific tour, note the name
- **Highlights**: What activities/features are shown?
- **Price/Duration**: If mentioned in the post
- **Category**: Beach, Adventure, Cultural, Luxury, or Nature

## 🔧 Step 3: Update Website Content

### Option A: Use the Import Script (Recommended)

1. **Edit `import_instagram.py`**:
   - Fill in the `INSTAGRAM_CONTENT` array with your Instagram posts
   - Use this format for each post:

```python
{
    "type": "tour",  # or "destination" or "gallery"
    "image_name": "kerala-backwaters.jpg",
    "title": "Kerala Backwaters Tour",
    "caption": "Full Instagram caption here...",
    "location": "Kerala, India",
    "description": "Detailed description...",
    "highlights": ["Backwater cruise", "Houseboat stay", "Local cuisine"],
    "price": 599,
    "duration": "3 days",
    "category": "Cultural",
    "best_time": "October to March"
}
```

2. **Run the script**:
```bash
python3 import_instagram.py
```

3. The script will:
   - Update `data/tours.json` with tour posts
   - Update `data/destinations.json` with destination posts
   - Show you gallery items to add

4. **Update Gallery**:
   - The script will show gallery items
   - Add them to `data/gallery.json` manually

### Option B: Manual Update (If you prefer)

#### Update Tours (`data/tours.json`):
Add a new tour object:
```json
{
  "id": 7,
  "title": "Kerala Backwaters Tour",
  "subtitle": "3 Days / 2 Nights",
  "price": 599,
  "duration": "3 days",
  "difficulty": "Easy",
  "image": "assets/images/tours/kerala-backwaters.jpg",
  "description": "Experience the serene backwaters...",
  "highlights": ["Backwater cruise", "Traditional houseboat"],
  "includes": ["Accommodation", "Meals", "Guided tours"],
  "category": "Cultural"
}
```

#### Update Destinations (`data/destinations.json`):
Add a new destination:
```json
{
  "id": 7,
  "name": "Kerala Backwaters",
  "region": "South India",
  "image": "assets/images/destinations/kerala-backwaters.jpg",
  "description": "Serene backwaters with traditional houseboats...",
  "bestTime": "October to March",
  "highlights": ["Backwater cruise", "Traditional culture"]
}
```

#### Update Gallery (`data/gallery.json`):
Add gallery items:
```json
{
  "src": "assets/images/gallery/kerala-backwaters-1.jpg",
  "category": "tours",
  "title": "Kerala Backwaters"
}
```

## ✅ Step 4: Verify Everything Works

1. Start local server: `python3 -m http.server 8000`
2. Open http://localhost:8000
3. Check:
   - Tours page shows your Instagram tours
   - Destinations page shows your locations
   - Gallery shows your Instagram photos
   - Images load correctly

## 💡 Tips

1. **Image Naming**: Use descriptive, consistent names
   - Good: `kerala-backwaters-1.jpg`, `goa-beach-2.jpg`
   - Bad: `IMG_1234.jpg`, `photo.jpg`

2. **Image Optimization**: 
   - Resize large images (max 2000px width)
   - Compress using TinyPNG or similar tools
   - Keep file sizes under 500KB

3. **Content Organization**:
   - Group similar tours together
   - Use consistent categories
   - Keep descriptions clear and engaging

4. **Regular Updates**:
   - Add new Instagram posts monthly
   - Update prices/durations if changed
   - Refresh gallery with latest photos

## 📋 Quick Checklist

- [ ] Downloaded all Instagram photos
- [ ] Organized photos into correct folders
- [ ] Extracted captions and descriptions
- [ ] Filled in `import_instagram.py` with content data
- [ ] Ran import script
- [ ] Updated `data/gallery.json` with gallery items
- [ ] Verified images load correctly
- [ ] Tested website on local server
- [ ] Checked mobile responsiveness

## 🆘 Troubleshooting

**Images don't show:**
- Check file paths in JSON files
- Verify images are in correct folders
- Check image file names match exactly (case-sensitive)

**Content doesn't appear:**
- Verify JSON files are valid (no syntax errors)
- Check browser console for errors (F12)
- Make sure you're using a local server (not opening file directly)

**Import script errors:**
- Make sure Python 3 is installed
- Check that JSON files exist in `data/` folder
- Verify image file names match what's in the script

## 📞 Need Help?

If you encounter issues:
1. Check browser console (F12) for errors
2. Verify all JSON files are valid JSON
3. Ensure image paths match folder structure
4. Test with a single image first before adding all

---

**Remember**: Instagram content is your own content, so you're free to use it on your website. Just make sure you have the rights to any user-generated content if you're using customer photos.
