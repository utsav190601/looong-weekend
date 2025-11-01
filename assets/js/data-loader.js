/**
 * Data Loader Utility
 * Handles loading JSON data files
 */

class DataLoader {
  /**
   * Get the base path for the site (handles GitHub Pages subdirectory)
   */
  static getBasePath() {
    const pathname = window.location.pathname;
    
    // Handle root cases
    if (pathname === '/' || pathname === '/index.html') {
      return '/';
    }
    
    // Find the last slash
    const lastSlash = pathname.lastIndexOf('/');
    
    // If no slash found or only root slash, return root
    if (lastSlash <= 0) {
      return '/';
    }
    
    // Return the path up to and including the last slash
    // This handles both /repo-name/index.html and /repo-name/
    return pathname.substring(0, lastSlash + 1);
  }

  /**
   * Resolve a file path relative to the site root
   */
  static resolvePath(filePath) {
    // If path already starts with /, it's absolute from domain root
    if (filePath.startsWith('/')) {
      return filePath;
    }
    // Otherwise, make it relative to the base path
    const basePath = this.getBasePath();
    // Remove leading ./ if present
    const cleanPath = filePath.replace(/^\.\//, '');
    return basePath + cleanPath;
  }

  static async loadJSON(filePath) {
    try {
      const resolvedPath = this.resolvePath(filePath);
      const response = await fetch(resolvedPath);
      if (!response.ok) {
        throw new Error(`Failed to load ${resolvedPath}: ${response.statusText}`);
      }
      return await response.json();
    } catch (error) {
      console.error(`Error loading ${filePath}:`, error);
      throw error;
    }
  }

  static async loadCompany() {
    return await this.loadJSON('data/company.json');
  }

  static async loadTours() {
    const data = await this.loadJSON('data/tours.json');
    return data.tours;
  }

  static async loadDestinations() {
    const data = await this.loadJSON('data/destinations.json');
    return data.destinations;
  }

  static async loadTestimonials() {
    const data = await this.loadJSON('data/testimonials.json');
    return data.testimonials;
  }

  static async loadGallery() {
    const data = await this.loadJSON('data/gallery.json');
    return data.galleryImages;
  }

  static formatPrice(price) {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 0
    }).format(price);
  }

  static formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  }

  static getStarRating(rating) {
    return '★'.repeat(rating) + '☆'.repeat(5 - rating);
  }
}
