# Auto-Organize Images - Quick Guide

## 🚀 How It Works

Just drop your Instagram photos into the folders, and the script will automatically:
- **Categorize** them based on filename and location
- **Generate** tour/destination descriptions
- **Add** them to the appropriate JSON files
- **Organize** gallery images

## 📁 Folder Structure

Place your photos in these folders:

```
assets/images/
├── tours/          # Photos of tours → Auto-added to tours.json
├── destinations/   # Location photos → Auto-added to destinations.json
└── gallery/        # General photos → Auto-added to gallery.json
```

## 📝 Naming Your Images

The script is smart! It reads your filenames to categorize. Examples:

### Good Names (Auto-detected):
- `kerala-backwaters-tour.jpg` → Kerala tour, Cultural category
- `goa-beach-weekend.jpg` → Goa tour, Beach category
- `himachal-mountain-trek.jpg` → Himachal tour, Adventure category
- `rajasthan-palace-heritage.jpg` → Rajasthan tour, Cultural category

### Location Detection:
The script recognizes these locations:
- **Kerala** (Alleppey, Kumarakom, Munnar)
- **Goa** 
- **Himachal** (Manali, McLeod Ganj)
- **Rajasthan** (Jaipur, Udaipur, Jaisalmer)
- **Uttarakhand** (Rishikesh)
- **And more...**

### Category Detection:
Based on keywords in filename:
- **Beach**: beach, coastal, sea, ocean
- **Adventure**: mountain, trek, hiking, camping, safari
- **Cultural**: temple, heritage, palace, fort, backwater
- **Nature**: forest, jungle, wildlife, valley

## 🎯 Usage

### Step 1: Add Your Photos
1. Download photos from Instagram
2. Place them in the appropriate folders:
   - Tour photos → `assets/images/tours/`
   - Destination photos → `assets/images/destinations/`
   - Gallery photos → `assets/images/gallery/`

### Step 2: Run the Script
```bash
python3 auto-organize-images.py
```

### Step 3: Review & Refine
The script creates entries automatically, but you can refine:
- Edit `data/tours.json` - Update descriptions, prices, highlights
- Edit `data/destinations.json` - Adjust details
- Edit `data/gallery.json` - Update titles/categories

## ✨ What Gets Auto-Generated

### For Tours:
- ✅ Title (from filename)
- ✅ Category (Beach, Adventure, Cultural, etc.)
- ✅ Price (based on category)
- ✅ Duration (based on category)
- ✅ Highlights (from filename keywords)
- ✅ Location (if detected)
- ✅ Description (auto-generated)

### For Destinations:
- ✅ Name (from location)
- ✅ Region (North/South/West India)
- ✅ Best time to visit
- ✅ Highlights
- ✅ Description

### For Gallery:
- ✅ Title (from filename)
- ✅ Category (auto-detected)
- ✅ Image path

## 💡 Tips

1. **Use descriptive filenames**:
   - ✅ Good: `kerala-backwaters-houseboat-1.jpg`
   - ❌ Bad: `IMG_1234.jpg`

2. **Include location in filename**:
   - `kerala-...` → Detects Kerala
   - `goa-...` → Detects Goa
   - `himachal-...` → Detects Himachal

3. **Include activity keywords**:
   - `beach`, `trek`, `palace`, `temple`, etc.

4. **Run script after adding photos**:
   - Script avoids duplicates
   - Safe to run multiple times
   - Only adds new images

## 🔄 Workflow

1. Download Instagram photos
2. Rename with descriptive names (optional but recommended)
3. Drop into appropriate folders
4. Run: `python3 auto-organize-images.py`
5. Check the website - photos should appear!
6. Refine descriptions in JSON files if needed

## 🎨 Customization

After auto-organization, you can:
- Update prices in `data/tours.json`
- Refine descriptions with your actual Instagram captions
- Add more highlights
- Adjust categories
- Update durations

The auto-organization is just a starting point - customize as needed!

## 📋 Example

**Before:**
- Photo: `assets/images/tours/kerala-backwaters-1.jpg`

**After running script:**
- Automatically added to `tours.json` as:
```json
{
  "id": 7,
  "title": "Kerala Backwaters 1",
  "category": "Cultural",
  "price": 599,
  "duration": "3 days",
  "description": "Experience the beauty of Kerala, India...",
  "highlights": ["Backwater", "Scenic views", "Accommodation"]
}
```

**You can then refine it:**
```json
{
  "title": "Kerala Backwaters Experience",
  "description": "Float through serene backwaters on traditional houseboat...",
  "highlights": ["Houseboat stay", "Backwater cruise", "Local cuisine"]
}
```

---

**That's it!** Just add photos and run the script. No manual JSON editing needed! 🎉
