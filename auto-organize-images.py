#!/usr/bin/env python3
"""
Auto-Organize Instagram Images
Automatically categorizes and adds images to the website based on filenames and folder locations.
"""

import json
import os
from pathlib import Path
from datetime import datetime
import re

def extract_info_from_filename(filename):
    """Extract location, tour type, and category from filename"""
    name = Path(filename).stem.lower()  # Remove extension
    
    # Location keywords
    locations = {
        'kerala': 'Kerala, India',
        'goa': 'Goa, India',
        'himachal': 'Himachal Pradesh, India',
        'rajasthan': 'Rajasthan, India',
        'uttarakhand': 'Uttarakhand, India',
        'ladakh': 'Ladakh, India',
        'manali': 'Manali, Himachal Pradesh',
        'mcleod': 'McLeod Ganj, Himachal Pradesh',
        'rishikesh': 'Rishikesh, Uttarakhand',
        'jaipur': 'Jaipur, Rajasthan',
        'udaipur': 'Udaipur, Rajasthan',
        'jaisalmer': 'Jaisalmer, Rajasthan',
        'alleppey': 'Alappuzha, Kerala',
        'kumarakom': 'Kumarakom, Kerala',
        'munnar': 'Munnar, Kerala',
        'coorg': 'Coorg, Karnataka',
        'ooty': 'Ooty, Tamil Nadu',
        'darjeeling': 'Darjeeling, West Bengal',
    }
    
    # Category detection from filename
    categories = {
        'beach': 'Beach',
        'coastal': 'Beach',
        'sea': 'Beach',
        'ocean': 'Beach',
        'mountain': 'Adventure',
        'trek': 'Adventure',
        'hiking': 'Adventure',
        'adventure': 'Adventure',
        'camping': 'Adventure',
        'temple': 'Cultural',
        'heritage': 'Cultural',
        'palace': 'Cultural',
        'fort': 'Cultural',
        'culture': 'Cultural',
        'backwater': 'Cultural',
        'houseboat': 'Cultural',
        'safari': 'Adventure',
        'wildlife': 'Nature',
        'forest': 'Nature',
        'jungle': 'Nature',
        'nature': 'Nature',
        'hill': 'Nature',
        'valley': 'Nature',
        'city': 'Cultural',
        'urban': 'Cultural',
    }
    
    # Activity keywords
    activities = {
        'sunset': 'Sunset views',
        'sunrise': 'Sunrise views',
        'water': 'Water activities',
        'sports': 'Sports activities',
        'cruise': 'Cruise experience',
        'camp': 'Camping',
        'trek': 'Trekking',
    }
    
    detected_location = None
    detected_category = 'Cultural'  # Default
    highlights = []
    
    # Detect location
    for key, location in locations.items():
        if key in name:
            detected_location = location
            break
    
    # Detect category
    for key, category in categories.items():
        if key in name:
            detected_category = category
            highlights.append(key.title())
            break
    
    # Extract numbers for tour identification
    numbers = re.findall(r'\d+', name)
    tour_num = numbers[0] if numbers else ''
    
    return {
        'location': detected_location,
        'category': detected_category,
        'highlights': highlights[:3] if highlights else ['Scenic views', 'Photo opportunities'],
        'tour_number': tour_num
    }


def generate_tour_from_image(image_path, folder_path):
    """Generate tour entry from image"""
    filename = os.path.basename(image_path)
    info = extract_info_from_filename(filename)
    
    # Clean title from filename
    title_parts = Path(filename).stem.replace('-', ' ').replace('_', ' ').title().split()
    # Remove common words
    title_parts = [w for w in title_parts if w.lower() not in ['the', 'of', 'and', 'in', 'at', 'on', 'tour', 'photo', 'image', 'img']]
    title = ' '.join(title_parts[:4]) or filename.replace('.jpg', '').replace('-', ' ').title()
    
    # Default pricing based on category
    prices = {
        'Beach': 499,
        'Adventure': 699,
        'Cultural': 599,
        'Luxury': 899,
        'Nature': 549
    }
    
    # Default duration based on category
    durations = {
        'Beach': '2 days',
        'Adventure': '3-4 days',
        'Cultural': '3 days',
        'Luxury': '2-3 days',
        'Nature': '3 days'
    }
    
    tour = {
        "title": title,
        "subtitle": f"{durations.get(info['category'], '2-3 days')}",
        "price": prices.get(info['category'], 599),
        "duration": durations.get(info['category'], '2-3 days'),
        "difficulty": "Easy" if info['category'] != 'Adventure' else "Moderate",
        "image": str(image_path).replace('\\', '/'),
        "description": f"Experience the beauty of {info['location'] or 'this destination'}. Perfect for a weekend getaway with stunning views and memorable experiences.",
        "highlights": info['highlights'] + ['Accommodation', 'Guided experience'] if len(info['highlights']) < 4 else info['highlights'][:4],
        "includes": [
            "Accommodation",
            "Meals",
            "Guided tours",
            "Transportation"
        ],
        "category": info['category']
    }
    
    return tour


def generate_destination_from_image(image_path, folder_path):
    """Generate destination entry from image"""
    filename = os.path.basename(image_path)
    info = extract_info_from_filename(filename)
    
    if not info['location']:
        return None
    
    # Best time to visit based on location
    best_times = {
        'Kerala': 'October to March',
        'Goa': 'October to May',
        'Himachal': 'April to June, September to November',
        'Rajasthan': 'October to March',
        'Uttarakhand': 'March to June, September to November',
    }
    
    location_name = info['location'].split(',')[0] if info['location'] else 'Destination'
    best_time = next((t for k, t in best_times.items() if k in location_name), 'Year-round')
    
    region_map = {
        'Kerala': 'South India',
        'Goa': 'West India',
        'Himachal': 'North India',
        'Rajasthan': 'Northwest India',
        'Uttarakhand': 'North India',
    }
    region = next((r for k, r in region_map.items() if k in location_name), 'India')
    
    destination = {
        "name": location_name,
        "region": region,
        "image": str(image_path).replace('\\', '/'),
        "description": f"Discover the beauty and culture of {location_name}. A perfect destination for travelers seeking authentic experiences.",
        "bestTime": best_time,
        "highlights": info['highlights'] + ['Local culture', 'Scenic beauty'] if len(info['highlights']) < 4 else info['highlights'][:4]
    }
    
    return destination


def scan_and_organize():
    """Main function to scan images and organize them"""
    base_path = Path('assets/images')
    
    print("🔍 Scanning images and auto-organizing...")
    print("=" * 60)
    
    # Scan tours folder
    tours_folder = base_path / 'tours'
    new_tours = []
    
    if tours_folder.exists():
        print(f"\n📸 Found {len(list(tours_folder.glob('*.jpg')) + list(tours_folder.glob('*.jpeg')) + list(tours_folder.glob('*.png')))} images in tours/")
        for img_file in tours_folder.glob('*.jpg'):
            new_tours.append(generate_tour_from_image(img_file, tours_folder))
        for img_file in tours_folder.glob('*.jpeg'):
            new_tours.append(generate_tour_from_image(img_file, tours_folder))
        for img_file in tours_folder.glob('*.png'):
            new_tours.append(generate_tour_from_image(img_file, tours_folder))
    
    # Scan destinations folder
    destinations_folder = base_path / 'destinations'
    new_destinations = []
    
    if destinations_folder.exists():
        print(f"📸 Found {len(list(destinations_folder.glob('*.jpg')) + list(destinations_folder.glob('*.jpeg')) + list(destinations_folder.glob('*.png')))} images in destinations/")
        for img_file in destinations_folder.glob('*.jpg'):
            dest = generate_destination_from_image(img_file, destinations_folder)
            if dest:
                new_destinations.append(dest)
        for img_file in destinations_folder.glob('*.jpeg'):
            dest = generate_destination_from_image(img_file, destinations_folder)
            if dest:
                new_destinations.append(dest)
        for img_file in destinations_folder.glob('*.png'):
            dest = generate_destination_from_image(img_file, destinations_folder)
            if dest:
                new_destinations.append(dest)
    
    # Scan gallery folder
    gallery_folder = base_path / 'gallery'
    new_gallery_items = []
    
    if gallery_folder.exists():
        print(f"📸 Found {len(list(gallery_folder.glob('*.jpg')) + list(gallery_folder.glob('*.jpeg')) + list(gallery_folder.glob('*.png')))} images in gallery/")
        for img_file in gallery_folder.glob('*.jpg'):
            info = extract_info_from_filename(str(img_file))
            title = Path(img_file).stem.replace('-', ' ').replace('_', ' ').title()
            new_gallery_items.append({
                "src": str(img_file).replace('\\', '/'),
                "category": info['category'].lower() if info['category'] else 'tours',
                "title": title
            })
        for img_file in gallery_folder.glob('*.jpeg'):
            info = extract_info_from_filename(str(img_file))
            title = Path(img_file).stem.replace('-', ' ').replace('_', ' ').title()
            new_gallery_items.append({
                "src": str(img_file).replace('\\', '/'),
                "category": info['category'].lower() if info['category'] else 'tours',
                "title": title
            })
        for img_file in gallery_folder.glob('*.png'):
            info = extract_info_from_filename(str(img_file))
            title = Path(img_file).stem.replace('-', ' ').replace('_', ' ').title()
            new_gallery_items.append({
                "src": str(img_file).replace('\\', '/'),
                "category": info['category'].lower() if info['category'] else 'tours',
                "title": title
            })
    
    # Update JSON files
    print("\n" + "=" * 60)
    print("📝 Updating JSON files...\n")
    
    # Update tours.json
    if new_tours:
        tours_file = Path('data/tours.json')
        tours_data = json.loads(tours_file.read_text(encoding='utf-8'))
        
        # Get max ID
        max_id = max([t.get('id', 0) for t in tours_data['tours']]) if tours_data['tours'] else 0
        
        # Add IDs to new tours
        for idx, tour in enumerate(new_tours):
            tour['id'] = max_id + idx + 1
        
        # Check for duplicates and add new ones
        existing_images = {t['image'] for t in tours_data['tours']}
        unique_tours = [t for t in new_tours if t['image'] not in existing_images]
        
        if unique_tours:
            tours_data['tours'].extend(unique_tours)
            tours_file.write_text(json.dumps(tours_data, indent=2, ensure_ascii=False), encoding='utf-8')
            print(f"✅ Added {len(unique_tours)} new tours to data/tours.json")
        else:
            print("ℹ️  All tours already exist")
    else:
        print("ℹ️  No new tour images found")
    
    # Update destinations.json
    if new_destinations:
        dest_file = Path('data/destinations.json')
        dest_data = json.loads(dest_file.read_text(encoding='utf-8'))
        
        max_id = max([d.get('id', 0) for d in dest_data['destinations']]) if dest_data['destinations'] else 0
        
        for idx, dest in enumerate(new_destinations):
            dest['id'] = max_id + idx + 1
        
        existing_images = {d['image'] for d in dest_data['destinations']}
        unique_dests = [d for d in new_destinations if d['image'] not in existing_images]
        
        if unique_dests:
            dest_data['destinations'].extend(unique_dests)
            dest_file.write_text(json.dumps(dest_data, indent=2, ensure_ascii=False), encoding='utf-8')
            print(f"✅ Added {len(unique_dests)} new destinations to data/destinations.json")
        else:
            print("ℹ️  All destinations already exist")
    else:
        print("ℹ️  No new destination images found")
    
    # Update gallery.json
    if new_gallery_items:
        gallery_file = Path('data/gallery.json')
        gallery_data = json.loads(gallery_file.read_text(encoding='utf-8'))
        
        existing_srcs = {g['src'] for g in gallery_data['galleryImages']}
        unique_gallery = [g for g in new_gallery_items if g['src'] not in existing_srcs]
        
        if unique_gallery:
            gallery_data['galleryImages'].extend(unique_gallery)
            gallery_file.write_text(json.dumps(gallery_data, indent=2, ensure_ascii=False), encoding='utf-8')
            print(f"✅ Added {len(unique_gallery)} new items to data/gallery.json")
        else:
            print("ℹ️  All gallery items already exist")
    else:
        print("ℹ️  No new gallery images found")
    
    print("\n" + "=" * 60)
    print("✅ Auto-organization complete!")
    print("\n📋 Summary:")
    print(f"   Tours added: {len(new_tours)}")
    print(f"   Destinations added: {len(new_destinations)}")
    print(f"   Gallery items added: {len(new_gallery_items)}")
    print("\n💡 Tip: You can now refine the descriptions and details in the JSON files")


if __name__ == '__main__':
    try:
        scan_and_organize()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
