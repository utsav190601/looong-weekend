/**
 * Shared Utilities
 * Common functionality used across multiple pages
 */

const SharedUtils = {
  /**
   * Load and populate footer information
   */
  async loadFooterInfo() {
    try {
      const company = await DataLoader.loadCompany();
      
      // Update footer contact info
      const footerEmail = document.getElementById('footer-email');
      const footerPhone = document.getElementById('footer-phone');
      const footerAddress = document.getElementById('footer-address');
      
      if (footerEmail) footerEmail.textContent = company.contact.email;
      if (footerPhone) footerPhone.textContent = company.contact.phone;
      if (footerAddress) footerAddress.textContent = company.contact.address;
      
      // Update social links
      const socialLinks = document.querySelectorAll('.social-links a');
      if (socialLinks.length >= 4) {
        socialLinks[0].href = company.social.facebook;
        socialLinks[1].href = company.social.instagram;
        socialLinks[2].href = company.social.twitter;
        socialLinks[3].href = company.social.linkedin;
      }
      
      return company;
    } catch (error) {
      console.error('Failed to load company info:', error);
      return null;
    }
  },

  /**
   * Set current year in footer
   */
  setCurrentYear() {
    const yearElement = document.getElementById('current-year');
    if (yearElement) {
      yearElement.textContent = new Date().getFullYear();
    }
  },

  /**
   * Initialize footer (load info and set year)
   */
  async initializeFooter() {
    this.setCurrentYear();
    await this.loadFooterInfo();
  },

  /**
   * Generate image placeholder SVG
   * Matches the original format used in the codebase
   * Ensures consistent dimensions for proper card alignment
   */
  createImagePlaceholder(width, height, text) {
    const encodedText = encodeURIComponent(text || 'Image');
    const fontSize = width >= 400 ? '20' : '18';
    
    // For gallery items (square), use gradient. For tours/destinations (rectangular), use solid color
    if (width === height || Math.abs(width - height) < 50) {
      // Square/gallery format with gradient (original format)
      return `data:image/svg+xml,%3Csvg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'${width}\\' height=\\'${height}\\' viewBox=\\'0 0 ${width} ${height}\\' preserveAspectRatio=\\'none\\'%3E%3Cdefs%3E%3ClinearGradient id=\\'grad\\' x1=\\'0%25\\' y1=\\'0%25\\' x2=\\'100%25\\' y2=\\'100%25\\'%3E%3Cstop offset=\\'0%25\\' style=\\'stop-color:%232563eb;stop-opacity:1\\' /%3E%3Cstop offset=\\'100%25\\' style=\\'stop-color:%23f59e0b;stop-opacity:1\\' /%3E%3C/linearGradient%3E%3C/defs%3E%3Crect width=\\'${width}\\' height=\\'${height}\\' fill=\\'url(%23grad)\\'/%3E%3Ctext fill=\\'white\\' font-family=\\'Arial\\' font-size=\\'${fontSize}\\' x=\\'50%25\\' y=\\'50%25\\' text-anchor=\\'middle\\' dominant-baseline=\\'middle\\'%3E${encodedText}%3C/text%3E%3C/svg%3E`;
    } else {
      // Rectangular format with solid color (for tours/destinations) - original format
      // Ensure proper viewBox and preserveAspectRatio for consistent rendering
      return `data:image/svg+xml,%3Csvg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'${width}\\' height=\\'${height}\\' viewBox=\\'0 0 ${width} ${height}\\' preserveAspectRatio=\\'none\\'%3E%3Crect width=\\'${width}\\' height=\\'${height}\\' fill=\\'%232563eb\\'/%3E%3Ctext fill=\\'white\\' font-family=\\'Arial\\' font-size=\\'${fontSize}\\' x=\\'50%25\\' y=\\'50%25\\' text-anchor=\\'middle\\' dominant-baseline=\\'middle\\'%3E${encodedText}%3C/text%3E%3C/svg%3E`;
    }
  },

  /**
   * Sort items prioritizing Instagram items (ID >= 100)
   */
  sortByInstagram(items) {
    return [...items].sort((a, b) => {
      const aIsInstagram = a.id >= 100;
      const bIsInstagram = b.id >= 100;
      if (aIsInstagram && !bIsInstagram) return -1;
      if (!aIsInstagram && bIsInstagram) return 1;
      return a.id - b.id;
    });
  },

  /**
   * Filter Instagram items (ID >= 100) or return first N items
   */
  getPrioritizedItems(items, count = 3) {
    const instagramItems = items.filter(item => item.id >= 100);
    return instagramItems.length > 0 
      ? instagramItems.slice(0, count)
      : items.slice(0, count);
  },

  /**
   * Scroll to anchor if present in URL hash
   */
  scrollToAnchor() {
    const hash = window.location.hash;
    if (hash) {
      setTimeout(() => {
        const element = document.querySelector(hash);
        if (element) {
          element.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }, 100);
    }
  },

  /**
   * Handle anchor scrolling after content loads
   */
  handleAnchorScrolling() {
    window.addEventListener('load', () => {
      this.scrollToAnchor();
    });
    
    // Also check after a delay in case content loads dynamically
    setTimeout(() => {
      this.scrollToAnchor();
    }, 500);
  }
};

