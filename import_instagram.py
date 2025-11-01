#!/usr/bin/env python3
"""
Instagram Content Import Helper

This script helps you organize and import Instagram content into the website.
Run: python3 import_instagram.py
"""

import json
import os
from pathlib import Path

# Instagram content data - Fill this with your Instagram posts
# Copy this format for each Instagram post you want to add
INSTAGRAM_CONTENT = [
    # Example format - Replace with your actual Instagram content
    {
        "type": "tour",  # Options: "tour", "destination", "gallery"
        "image_name": "kerala-backwaters.jpg",  # Name of image file you downloaded
        "title": "Kerala Backwaters Tour",  # Title from Instagram
        "caption": "Full caption from Instagram post...",  # Instagram caption
        "location": "Kerala, India",  # Location if mentioned
        "description": "Experience the serene backwaters of Kerala...",  # Detailed description
        "highlights": ["Backwater cruise", "Traditional houseboat", "Local cuisine"],
        "price": 599,  # Price if applicable
        "duration": "3 days",
        "category": "Cultural",  # Beach, Adventure, Cultural, Luxury, Nature
        "best_time": "October to March",  # If destination
    },
    # Add more posts here...
]


def load_json_file(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json_file(filepath, data):
    """Save JSON file with pretty formatting"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def update_tours():
    """Update tours.json with Instagram tour content"""
    tours_file = Path('data/tours.json')
    tours_data = load_json_file(tours_file)
    
    instagram_tours = []
    for idx, item in enumerate(INSTAGRAM_CONTENT):
        if item.get('type') == 'tour':
            tour = {
                "id": len(tours_data['tours']) + len(instagram_tours) + 1,
                "title": item.get('title', f'Instagram Tour {len(instagram_tours) + 1}'),
                "subtitle": f"{item.get('duration', '2-3 days')}",
                "price": item.get('price', 499),
                "duration": item.get('duration', '2-3 days'),
                "difficulty": "Easy",
                "image": f"assets/images/tours/{item['image_name']}",
                "description": item.get('description') or item.get('caption', ''),
                "highlights": item.get('highlights', []),
                "includes": [
                    "Accommodation",
                    "Meals",
                    "Guided tours",
                    "Transportation"
                ],
                "category": item.get('category', 'Cultural')
            }
            instagram_tours.append(tour)
    
    if instagram_tours:
        tours_data['tours'].extend(instagram_tours)
        save_json_file(tours_file, tours_data)
        print(f"✅ Added {len(instagram_tours)} tours to data/tours.json")
        return True
    return False


def update_destinations():
    """Update destinations.json with Instagram destination content"""
    dest_file = Path('data/destinations.json')
    dest_data = load_json_file(dest_file)
    
    instagram_dests = []
    for idx, item in enumerate(INSTAGRAM_CONTENT):
        if item.get('type') == 'destination':
            dest = {
                "id": len(dest_data['destinations']) + len(instagram_dests) + 1,
                "name": item.get('title') or item.get('location', f'Instagram Destination {len(instagram_dests) + 1}'),
                "region": item.get('region', 'Various'),
                "image": f"assets/images/destinations/{item['image_name']}",
                "description": item.get('description') or item.get('caption', ''),
                "bestTime": item.get('best_time', 'Year-round'),
                "highlights": item.get('highlights', [])
            }
            instagram_dests.append(dest)
    
    if instagram_dests:
        dest_data['destinations'].extend(instagram_dests)
        save_json_file(dest_file, dest_data)
        print(f"✅ Added {len(instagram_dests)} destinations to data/destinations.json")
        return True
    return False


def generate_gallery_updates():
    """Generate gallery items for manual update"""
    gallery_items = []
    for item in INSTAGRAM_CONTENT:
        if item.get('type') == 'gallery':
            gallery_item = {
                "src": f"assets/images/gallery/{item['image_name']}",
                "category": item.get('category', 'tours').lower(),
                "title": item.get('title') or item.get('location', 'Instagram Photo')
            }
            gallery_items.append(gallery_item)
    
    if gallery_items:
        print("\n📸 Gallery items to add to gallery.html:")
        print("   Add these to the galleryImages array:")
        for item in gallery_items:
            print(f"   {json.dumps(item)},")
        return True
    return False


def main():
    print("🚀 Instagram Content Import Tool\n")
    print("=" * 50)
    
    if not INSTAGRAM_CONTENT or len(INSTAGRAM_CONTENT) == 0:
        print("⚠️  No Instagram content found!")
        print("\nPlease edit this script and fill in INSTAGRAM_CONTENT array with:")
        print("  - Image names of downloaded Instagram photos")
        print("  - Captions and descriptions")
        print("  - Tour/destination details")
        return
    
    print(f"\n📊 Processing {len(INSTAGRAM_CONTENT)} Instagram posts...\n")
    
    tours_updated = update_tours()
    destinations_updated = update_destinations()
    gallery_updated = generate_gallery_updates()
    
    print("\n" + "=" * 50)
    print("✅ Import Summary:")
    print(f"   Tours: {'Updated' if tours_updated else 'No tours found'}")
    print(f"   Destinations: {'Updated' if destinations_updated else 'No destinations found'}")
    print(f"   Gallery: {'See items above' if gallery_updated else 'No gallery items found'}")
    
    print("\n📝 Next Steps:")
    print("   1. Make sure all images are in the correct folders:")
    print("      - assets/images/tours/")
    print("      - assets/images/destinations/")
    print("      - assets/images/gallery/")
    print("   2. If you have gallery items, update gallery.html manually")
    print("   3. Test the website to verify everything displays correctly")


if __name__ == '__main__':
    main()
