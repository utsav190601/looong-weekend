#!/usr/bin/env python3
"""
Analyze Instagram images and organize them into website structure
"""

import json
import os
from pathlib import Path
import shutil

def organize_images():
    """Organize images from main folder into subfolders and update JSON files"""
    
    images_dir = Path('assets/images')
    tours_dir = images_dir / 'tours'
    destinations_dir = images_dir / 'destinations'
    gallery_dir = images_dir / 'gallery'
    
    # Create folders if they don't exist
    tours_dir.mkdir(exist_ok=True)
    destinations_dir.mkdir(exist_ok=True)
    gallery_dir.mkdir(exist_ok=True)
    
    # Find all images in main folder
    images = sorted([f for f in images_dir.iterdir() 
                     if f.is_file() and f.suffix.lower() in ['.jpg', '.jpeg', '.png']])
    
    if not images:
        print("No images found to organize")
        return
    
    print(f"Found {len(images)} images to organize\n")
    
    # Strategy: Distribute images across tours, destinations, and gallery
    # We'll put most in gallery and some in tours based on count
    total_images = len(images)
    
    tours_images = images[:max(1, total_images // 3)]  # 1/3 for tours
    destinations_images = images[len(tours_images):len(tours_images) + max(1, total_images // 4)]  # 1/4 for destinations
    gallery_images = images[len(tours_images) + len(destinations_images):]  # Rest for gallery
    
    # Move and organize tours
    new_tours = []
    for idx, img in enumerate(tours_images, 1):
        new_name = f"tour-{idx:02d}.jpg"
        dest_path = tours_dir / new_name
        shutil.copy2(img, dest_path)
        print(f"📸 {img.name} → tours/{new_name}")
        
        tour = {
            "id": 100 + idx,  # Start from 100 to avoid conflicts
            "title": f"Amazing Tour Experience {idx}",
            "subtitle": "Weekend Getaway",
            "price": 599,
            "duration": "2-3 days",
            "difficulty": "Easy",
            "image": f"assets/images/tours/{new_name}",
            "description": "Discover breathtaking destinations and create unforgettable memories. This tour offers a perfect blend of adventure, culture, and relaxation for your weekend escape.",
            "highlights": [
                "Scenic views",
                "Cultural experiences",
                "Memorable moments",
                "Photo opportunities"
            ],
            "includes": [
                "Accommodation",
                "Meals",
                "Guided tours",
                "Transportation"
            ],
            "category": "Cultural"
        }
        new_tours.append(tour)
    
    # Move and organize destinations
    new_destinations = []
    for idx, img in enumerate(destinations_images, 1):
        new_name = f"destination-{idx:02d}.jpg"
        dest_path = destinations_dir / new_name
        shutil.copy2(img, dest_path)
        print(f"📸 {img.name} → destinations/{new_name}")
        
        destination = {
            "id": 100 + idx,
            "name": f"Beautiful Destination {idx}",
            "region": "Various",
            "image": f"assets/images/destinations/{new_name}",
            "description": "A stunning destination offering unique experiences and breathtaking scenery. Perfect for travelers seeking adventure and discovery.",
            "bestTime": "Year-round",
            "highlights": [
                "Scenic beauty",
                "Cultural richness",
                "Adventure opportunities",
                "Photography spots"
            ]
        }
        new_destinations.append(destination)
    
    # Move and organize gallery
    new_gallery = []
    for idx, img in enumerate(gallery_images, 1):
        new_name = f"gallery-{idx:02d}.jpg"
        dest_path = gallery_dir / new_name
        shutil.copy2(img, dest_path)
        print(f"📸 {img.name} → gallery/{new_name}")
        
        gallery_item = {
            "src": f"assets/images/gallery/{new_name}",
            "category": "tours",
            "title": f"Gallery Photo {idx}"
        }
        new_gallery.append(gallery_item)
    
    # Update JSON files
    print("\n📝 Updating JSON files...\n")
    
    # Update tours.json
    tours_file = Path('data/tours.json')
    tours_data = json.loads(tours_file.read_text(encoding='utf-8'))
    tours_data['tours'].extend(new_tours)
    tours_file.write_text(json.dumps(tours_data, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"✅ Added {len(new_tours)} tours")
    
    # Update destinations.json
    dest_file = Path('data/destinations.json')
    dest_data = json.loads(dest_file.read_text(encoding='utf-8'))
    dest_data['destinations'].extend(new_destinations)
    dest_file.write_text(json.dumps(dest_data, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"✅ Added {len(new_destinations)} destinations")
    
    # Update gallery.json
    gallery_file = Path('data/gallery.json')
    gallery_data = json.loads(gallery_file.read_text(encoding='utf-8'))
    gallery_data['galleryImages'].extend(new_gallery)
    gallery_file.write_text(json.dumps(gallery_data, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"✅ Added {len(new_gallery)} gallery items")
    
    print("\n" + "="*60)
    print("✅ Organization complete!")
    print(f"\n📊 Summary:")
    print(f"   Tours: {len(new_tours)} images")
    print(f"   Destinations: {len(new_destinations)} images")
    print(f"   Gallery: {len(new_gallery)} images")
    print("\n💡 Tip: You can now update titles and descriptions in the JSON files")

if __name__ == '__main__':
    organize_images()

