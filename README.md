# The Looong Weekend - Travel Company Website

A modern, responsive static website for "The Looong Weekend" travel company.

## 📁 Project Structure

```
site/
├── index.html              # Homepage
├── about.html              # About Us page
├── tours.html              # Tour Packages listing
├── destinations.html        # Destinations overview
├── gallery.html            # Photo Gallery
├── testimonials.html       # Customer Reviews
├── contact.html            # Contact Information & Form
├── assets/
│   ├── css/
│   │   ├── style.css       # Main stylesheet
│   │   └── responsive.css  # Responsive breakpoints
│   ├── js/
│   │   ├── main.js         # Main JavaScript functionality
│   │   └── data-loader.js  # Data loading utilities
│   ├── images/
│   │   ├── tours/          # Tour-specific images
│   │   ├── destinations/   # Destination photos
│   │   ├── gallery/        # Gallery images
│   │   └── logo/           # Company logo
│   └── icons/              # SVG icons
├── data/
│   ├── tours.json          # Tour packages data
│   ├── destinations.json   # Destinations data
│   ├── testimonials.json   # Customer testimonials
│   └── company.json        # Company information
└── README.md
```

## 🚀 Getting Started

Simply open `index.html` in a web browser, or use a local server:

```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx serve
```

## ✏️ Easy Content Updates

### Adding/Editing Tours
Edit `data/tours.json` - Add or modify tour objects with:
- Title, description, duration, price
- Image paths
- Highlights and itinerary

### Adding/Editing Destinations
Edit `data/destinations.json` - Add destination details with:
- Name, description, location
- Best time to visit
- Image paths

### Adding Testimonials
Edit `data/testimonials.json` - Add customer reviews with:
- Customer name, rating, review text
- Tour name and photo (optional)

### Updating Images
1. Place images in appropriate folders under `assets/images/`
2. Update image paths in corresponding JSON files

### Company Information
Edit `data/company.json` for:
- Company name, tagline, description
- Contact details
- Social media links

## 🎨 Features & Enhancements

### Design & User Experience
- ✅ **Fully Responsive Design** - Optimized for mobile, tablet, and desktop devices
- ✅ **Modern UI/UX** - Clean, professional design with smooth animations and transitions
- ✅ **Hero Sections** - Eye-catching hero banners on every page
- ✅ **Card-Based Layout** - Beautiful card designs for tours, destinations, and testimonials
- ✅ **Mobile Menu** - Hamburger menu for mobile navigation
- ✅ **Smooth Scrolling** - Enhanced navigation experience
- ✅ **Loading States** - User-friendly loading indicators

### Functionality
- ✅ **Dynamic Content Loading** - Content loaded from JSON files via JavaScript
- ✅ **Tour Filtering** - Filter tours by category (Beach, Adventure, Cultural, etc.)
- ✅ **Gallery Filtering** - Filter gallery images by category
- ✅ **Contact Form** - Functional contact form with validation
- ✅ **URL Parameters** - Pre-fill contact form with tour selection
- ✅ **Star Ratings** - Visual star rating system for testimonials
- ✅ **Price Formatting** - Automatic currency formatting

### Content Management
- ✅ **JSON-Based Content** - All content in easy-to-edit JSON files
- ✅ **Centralized Data** - Single source of truth for company info, tours, destinations
- ✅ **Image Management** - Organized folder structure for images
- ✅ **SEO Optimization** - Meta tags, semantic HTML, proper headings
- ✅ **Accessibility** - ARIA labels, alt text support, keyboard navigation

### Technical Features
- ✅ **No Build Process** - Pure HTML, CSS, and JavaScript - no compilation needed
- ✅ **Fast Performance** - Optimized for quick loading
- ✅ **Browser Compatible** - Works on all modern browsers
- ✅ **Error Handling** - Graceful fallbacks for missing images/data
- ✅ **Placeholder Images** - SVG placeholders until real images are added

### Pages Included
1. **Homepage** - Featured tours, destinations, testimonials, and company overview
2. **About** - Company story, mission, values, and differentiators
3. **Tours** - Complete tour listing with filtering and detailed information
4. **Destinations** - All destinations with highlights and best times to visit
5. **Gallery** - Photo gallery with category filtering
6. **Testimonials** - Customer reviews and ratings
7. **Contact** - Contact information and inquiry form

## 🔧 Customization

### Colors & Branding
Edit CSS variables in `assets/css/style.css`:
```css
:root {
  --primary-color: #2563eb;    /* Main brand color */
  --secondary-color: #f59e0b;  /* Accent color */
  --accent-color: #10b981;      /* Success/highlight color */
}
```

### Content
- **Tours**: Edit `data/tours.json`
- **Destinations**: Edit `data/destinations.json`
- **Testimonials**: Edit `data/testimonials.json`
- **Company Info**: Edit `data/company.json`

### Images
See `IMAGES_GUIDE.md` for detailed instructions on adding and managing images.

## 📝 Next Steps

1. **Add Real Images**: Replace placeholder images with your actual tour photos
   - See `IMAGES_GUIDE.md` for detailed instructions
   
2. **Update Content**: 
   - Edit JSON files with your actual tour information
   - Update contact details in `data/company.json`
   - Add your social media links

3. **Customize Branding**:
   - Update colors in CSS variables
   - Add your logo to `assets/images/logo/`
   - Customize fonts if desired

4. **Test Everything**:
   - Test on different devices and browsers
   - Verify all links work correctly
   - Test contact form functionality

5. **Deploy**:
   - Upload to any static hosting service (Netlify, Vercel, GitHub Pages, etc.)
   - No special configuration needed - just upload all files

## 🌟 Additional Enhancements You Can Add

- **Booking Integration** - Connect to a booking system API
- **Blog Section** - Add travel tips and stories
- **Newsletter Signup** - Email subscription form
- **Live Chat** - Customer support chat widget
- **Multi-language Support** - Add translation files
- **Payment Integration** - Add payment processing for bookings

## 📞 Support

For questions or issues:
- Check the `IMAGES_GUIDE.md` for image-related help
- Review JSON file structure in `/data/` folder
- Check browser console for JavaScript errors
