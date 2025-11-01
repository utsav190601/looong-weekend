# Image Management Guide

## Quick Start

The website is designed to work with placeholder images until you add your actual photos. All images are referenced in JSON files for easy updates.

## Adding Your Images

### Step 1: Prepare Your Images

1. **Resize images** to recommended dimensions (see `assets/images/README.md`)
2. **Optimize for web** - Use tools like:
   - [TinyPNG](https://tinypng.com/) or [Squoosh](https://squoosh.app/) for compression
   - Keep file sizes under 500KB for fast loading

### Step 2: Organize Images

Place images in the appropriate folders:

```
assets/images/
├── tours/              # Tour images
│   ├── coastal-paradise.jpg
│   ├── mountain-adventure.jpg
│   └── ...
├── destinations/       # Destination images
│   ├── coastal-beaches.jpg
│   └── ...
├── gallery/           # Gallery images
│   ├── coastal-tour-1.jpg
│   └── ...
└── testimonials/      # Customer photos (optional)
    └── ...
```

### Step 3: Update JSON Files

#### For Tours (`data/tours.json`):

```json
{
  "image": "assets/images/tours/your-tour-image.jpg"
}
```

#### For Destinations (`data/destinations.json`):

```json
{
  "image": "assets/images/destinations/your-destination-image.jpg"
}
```

#### For Testimonials (`data/testimonials.json`):

```json
{
  "image": "assets/images/testimonials/customer-photo.jpg"
}
```

#### For Gallery (`gallery.html`):

Update the `galleryImages` array in the JavaScript section:

```javascript
{ 
  src: 'assets/images/gallery/your-image.jpg', 
  category: 'tours', 
  title: 'Image Title' 
}
```

## Image Categories

### Tour Categories
- Beach
- Adventure
- Cultural
- Luxury
- Nature

### Gallery Categories
- tours
- destinations
- activities
- landscapes

## Placeholder Images

Until you add real images, the site uses SVG placeholders that display:
- Gradient backgrounds (blue to orange)
- Image titles/names
- Appropriate dimensions

These placeholders are automatically generated when images fail to load.

## Tips

1. **Consistency**: Keep image dimensions consistent within categories
2. **Quality**: Use high-quality photos that represent your tours well
3. **Naming**: Use descriptive filenames (e.g., `sunset-beach-coast.jpg`)
4. **Alt Text**: Always include descriptive alt text for accessibility
5. **File Size**: Optimize images to keep the site fast

## Testing

After adding images:
1. Refresh your browser
2. Check all pages where images appear
3. Test on mobile devices
4. Verify images load correctly

## Need Help?

If an image doesn't display:
1. Check the file path in the JSON file
2. Verify the image exists in the correct folder
3. Check browser console for errors
4. Ensure image file is not corrupted
