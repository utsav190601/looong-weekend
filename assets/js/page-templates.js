/**
 * Page Templates
 * Reusable HTML templates for rendering data
 */

const PageTemplates = {
  /**
   * Render tour card
   */
  renderTourCard(tour, options = {}) {
    const {
      showHighlights = true,
      showIncludes = false,
      showBookButton = false,
      showMeta = false,
      highlightCount = 3
    } = options;

    const placeholder = SharedUtils.createImagePlaceholder(400, 200, tour.title);
    
    return `
      <div class="card" id="${options.id || `tour-${tour.id}`}">
        <img src="${tour.image}" alt="${tour.title}" class="card-image" onerror="this.src='${placeholder}'">
        <div class="card-content">
          <h3 class="card-title">${tour.title}</h3>
          <p class="card-subtitle">${tour.subtitle}${showMeta ? ` • ${tour.difficulty} • ${tour.category}` : ''}</p>
          ${tour.price ? `<div class="card-price">${DataLoader.formatPrice(tour.price)}</div>` : ''}
          <p class="card-description">${tour.description}</p>
          ${showHighlights && tour.highlights ? `
            <ul class="card-highlights">
              ${tour.highlights.slice(0, highlightCount).map(h => `<li>${h}</li>`).join('')}
            </ul>
          ` : ''}
          ${showIncludes && tour.includes ? `
            <div style="margin: 1rem 0; padding: 1rem; background-color: var(--bg-light); border-radius: 0.5rem;">
              <strong style="display: block; margin-bottom: 0.5rem; color: var(--text-dark);">Includes:</strong>
              <ul class="card-highlights" style="margin: 0;">
                ${tour.includes.map(i => `<li>${i}</li>`).join('')}
              </ul>
            </div>
          ` : ''}
          <div class="card-actions">
            <a href="tour-detail.html?id=${tour.id}" class="card-button"${showBookButton ? ' style="margin-bottom: 0.5rem;"' : ''}>View Details</a>
            ${showBookButton ? `<a href="contact.html?tour=${encodeURIComponent(tour.title)}" class="card-button" style="background-color: var(--secondary-color);">Book Now</a>` : ''}
          </div>
        </div>
      </div>
    `;
  },

  /**
   * Render destination card
   */
  renderDestinationCard(dest, options = {}) {
    const { showHighlights = true, showBestTime = true } = options;
    const placeholder = SharedUtils.createImagePlaceholder(400, 200, dest.name);
    
    return `
      <div class="card" id="${options.id || `dest-${dest.id}`}">
        <img src="${dest.image}" alt="${dest.name}" class="card-image" onerror="this.src='${placeholder}'">
        <div class="card-content">
          <h3 class="card-title">${dest.name}</h3>
          <p class="card-subtitle">${dest.region}</p>
          <p class="card-description">${dest.description}</p>
          ${showBestTime ? `
            <div style="margin: 1rem 0;">
              <strong style="color: var(--text-dark);">Best Time to Visit:</strong>
              <p style="margin-top: 0.5rem; color: var(--text-light);">${dest.bestTime}</p>
            </div>
          ` : ''}
          ${showHighlights && dest.highlights ? `
            <div style="margin: 1rem 0;">
              <strong style="color: var(--text-dark);">Highlights:</strong>
              <ul class="card-highlights">
                ${dest.highlights.map(h => `<li>${h}</li>`).join('')}
              </ul>
            </div>
          ` : ''}
          <div class="card-actions">
            <a href="${options.link || `tours.html`}" class="card-button">${options.linkText || 'Explore Tours'}</a>
          </div>
        </div>
      </div>
    `;
  },

  /**
   * Render testimonial card
   */
  renderTestimonialCard(test, options = {}) {
    const { showDate = false, showTour = true } = options;
    const placeholder = SharedUtils.createImagePlaceholder(60, 60, test.customerName.charAt(0));
    
    return `
      <div class="testimonial-card">
        <div class="testimonial-header">
          <img src="${test.image}" alt="${test.customerName}" class="testimonial-image" onerror="this.src='${placeholder}'">
          <div>
            <div class="testimonial-rating">${DataLoader.getStarRating(test.rating)}</div>
            <div class="testimonial-author">${test.customerName}</div>
            ${showTour ? `<div class="testimonial-tour">${test.tourName}</div>` : ''}
            ${showDate ? `<div class="testimonial-tour" style="font-size: 0.75rem; margin-top: 0.25rem;">${DataLoader.formatDate(test.date)}</div>` : ''}
          </div>
        </div>
        <p class="testimonial-text">"${test.review}"</p>
      </div>
    `;
  },

  /**
   * Render gallery item
   */
  renderGalleryItem(img) {
    const placeholder = SharedUtils.createImagePlaceholder(400, 400, img.title);
    
    return `
      <div class="gallery-item">
        <img src="${img.src}" alt="${img.title}" onerror="this.src='${placeholder}'">
        <div class="gallery-overlay">
          <p style="margin: 0; font-weight: 500;">${img.title}</p>
        </div>
      </div>
    `;
  }
};

