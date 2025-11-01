# Image Directory Structure

This directory contains all images used throughout the website. Images are organized into subdirectories for easy management.

## Directory Structure

```
images/
├── tours/              # Tour package images
├── destinations/        # Destination photos
├── gallery/            # Gallery images (mixed categories)
├── testimonials/       # Customer photos (optional)
├── about/              # About page images
└── logo/               # Company logos and branding
```

## Image Guidelines

### Recommended Specifications

- **Tour Images**: 800x500px or 1200x750px (16:10 aspect ratio)
- **Destination Images**: 800x600px or 1200x900px (4:3 aspect ratio)
- **Gallery Images**: Square (800x800px or 1200x1200px)
- **Testimonial Photos**: Square (200x200px minimum)
- **About Images**: 800x600px or larger

### File Naming Convention

- Use lowercase letters and hyphens
- Be descriptive: `coastal-paradise-beach.jpg` not `img1.jpg`
- Examples:
  - Tours: `coastal-paradise.jpg`, `mountain-adventure.jpg`
  - Destinations: `coastal-beaches.jpg`, `mountain-peaks.jpg`
  - Gallery: `coastal-tour-1.jpg`, `activity-hiking.jpg`

### Format Recommendations

- **Format**: JPG for photos, PNG for graphics/logos
- **Quality**: Optimize images for web (reduce file size while maintaining quality)
- **Alt Text**: Always update alt text in HTML/JSON when adding new images

## Adding New Images

1. Place images in the appropriate subdirectory
2. Update the corresponding JSON file in `/data/` with the new image path
3. Ensure images are optimized for web use
4. Update alt text for accessibility

## Image Paths in Code

Images are referenced in:
- `data/tours.json` - Tour images
- `data/destinations.json` - Destination images
- `data/testimonials.json` - Customer photos
- `gallery.html` - Gallery image array in JavaScript

## Quick Reference

When adding a new tour:
1. Add image to `tours/` folder
2. Update `data/tours.json` with image path: `assets/images/tours/your-image.jpg`

When adding a new destination:
1. Add image to `destinations/` folder
2. Update `data/destinations.json` with image path: `assets/images/destinations/your-image.jpg`

When adding gallery images:
1. Add image to `gallery/` folder
2. Update the `galleryImages` array in `gallery.html`
