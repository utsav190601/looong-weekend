/**
 * Instagram Content Import Helper
 * 
 * This script helps organize Instagram content for the website.
 * 
 * Usage:
 * 1. Download photos from Instagram manually
 * 2. Place them in the assets/images/ folders
 * 3. Fill in the contentData array below with your Instagram post information
 * 4. Run this script (node import-instagram-content.js)
 * 5. The script will generate updated JSON files
 */

const fs = require('fs');
const path = require('path');

// Instagram content data - Fill this with your Instagram posts
const instagramContent = [
  // Example format - Add your Instagram posts here
  {
    type: 'tour', // or 'destination', 'gallery'
    imageName: 'kerala-tour-1.jpg', // Name of downloaded image
    caption: 'Caption from Instagram post',
    location: 'Kerala',
    title: 'Kerala Backwaters Tour',
    description: 'Full description from Instagram',
    highlights: ['Backwater cruise', 'Local cuisine', 'Traditional houseboat'],
    price: 599, // If applicable
    duration: '3 days',
    category: 'Cultural'
  },
  // Add more posts as needed...
];

/**
 * Updates tours.json with Instagram tour content
 */
function updateTours() {
  const toursFile = path.join(__dirname, 'data', 'tours.json');
  const tours = JSON.parse(fs.readFileSync(toursFile, 'utf8'));
  
  const instagramTours = instagramContent
    .filter(item => item.type === 'tour')
    .map((item, index) => ({
      id: tours.tours.length + index + 1,
      title: item.title || 'Instagram Tour ' + (index + 1),
      subtitle: item.duration || 'Weekend Getaway',
      price: item.price || 499,
      duration: item.duration || '2-3 days',
      difficulty: 'Easy',
      image: `assets/images/tours/${item.imageName}`,
      description: item.description || item.caption,
      highlights: item.highlights || [],
      includes: [
        'Accommodation',
        'Meals',
        'Guided tours',
        'Transportation'
      ],
      category: item.category || 'Cultural'
    }));
  
  tours.tours = [...tours.tours, ...instagramTours];
  fs.writeFileSync(toursFile, JSON.stringify(tours, null, 2));
  console.log(`✅ Updated tours.json with ${instagramTours.length} new tours`);
}

/**
 * Updates destinations.json with Instagram destination content
 */
function updateDestinations() {
  const destFile = path.join(__dirname, 'data', 'destinations.json');
  const destinations = JSON.parse(fs.readFileSync(destFile, 'utf8'));
  
  const instagramDests = instagramContent
    .filter(item => item.type === 'destination')
    .map((item, index) => ({
      id: destinations.destinations.length + index + 1,
      name: item.location || item.title || 'Instagram Destination ' + (index + 1),
      region: item.region || 'Various',
      image: `assets/images/destinations/${item.imageName}`,
      description: item.description || item.caption,
      bestTime: item.bestTime || 'Year-round',
      highlights: item.highlights || []
    }));
  
  destinations.destinations = [...destinations.destinations, ...instagramDests];
  fs.writeFileSync(destFile, JSON.stringify(destinations, null, 2));
  console.log(`✅ Updated destinations.json with ${instagramDests.length} new destinations`);
}

/**
 * Updates gallery in gallery.html
 */
function updateGallery() {
  const galleryFile = path.join(__dirname, 'gallery.html');
  let galleryContent = fs.readFileSync(galleryFile, 'utf8');
  
  const galleryItems = instagramContent
    .filter(item => item.type === 'gallery')
    .map(item => ({
      src: `assets/images/gallery/${item.imageName}`,
      category: item.category || 'tours',
      title: item.title || item.location || 'Instagram Photo'
    }));
  
  // This would require more complex parsing - manual update recommended
  console.log('\n📸 Gallery items to add:');
  galleryItems.forEach(item => {
    console.log(JSON.stringify(item, null, 2) + ',');
  });
  console.log('\n⚠️  Manually add these to gallery.html galleryImages array\n');
}

/**
 * Main function
 */
function main() {
  console.log('🚀 Starting Instagram content import...\n');
  
  if (instagramContent.length === 0) {
    console.log('⚠️  No Instagram content found in instagramContent array.');
    console.log('Please fill in the instagramContent array with your Instagram post data.\n');
    return;
  }
  
  updateTours();
  updateDestinations();
  updateGallery();
  
  console.log('\n✅ Import complete!');
  console.log('📝 Remember to:');
  console.log('   1. Place all images in the correct folders');
  console.log('   2. Verify the generated JSON files');
  console.log('   3. Update gallery.html manually with gallery items');
}

// Run if executed directly
if (require.main === module) {
  main();
}

module.exports = { updateTours, updateDestinations, updateGallery };
