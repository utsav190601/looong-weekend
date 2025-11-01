/**
 * Contact Form Handler
 * Currently shows success message but doesn't send emails
 * 
 * To enable email sending, choose one:
 * 1. Formspree - Update form action to your Formspree endpoint
 * 2. EmailJS - Add EmailJS script and send via emailjs.send()
 * 3. Backend API - Send form data to your API endpoint
 */

document.addEventListener('DOMContentLoaded', function() {
  const contactForm = document.getElementById('contact-form');
  
  if (!contactForm) return;

  contactForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // Get form data
    const formData = new FormData(this);
    const data = Object.fromEntries(formData);
    
    // Validation
    if (!data.name || !data.email || !data.message) {
      showMessage('Please fill in all required fields.', 'error');
      return;
    }

    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(data.email)) {
      showMessage('Please enter a valid email address.', 'error');
      return;
    }

    // Show loading state
    const submitButton = this.querySelector('button[type="submit"]');
    const originalText = submitButton.textContent;
    submitButton.disabled = true;
    submitButton.textContent = 'Sending...';

    try {
      // TODO: Add actual form submission here
      // Option 1: Formspree
      // const response = await fetch(this.action, {
      //   method: 'POST',
      //   body: formData,
      //   headers: { 'Accept': 'application/json' }
      // });
      
      // Option 2: EmailJS
      // await emailjs.send('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', data);
      
      // Option 3: Custom API
      // await fetch('/api/contact', {
      //   method: 'POST',
      //   headers: { 'Content-Type': 'application/json' },
      //   body: JSON.stringify(data)
      // });

      // Simulate delay for UX
      await new Promise(resolve => setTimeout(resolve, 500));
      
      // Success - show message
      showMessage('Thank you for your inquiry! We will get back to you soon.', 'success');
      this.reset();
      
    } catch (error) {
      console.error('Form submission error:', error);
      showMessage('Sorry, there was an error sending your message. Please try again or email us directly.', 'error');
    } finally {
      submitButton.disabled = false;
      submitButton.textContent = originalText;
    }
  });

  function showMessage(message, type) {
    // Remove existing messages
    const existingMessage = document.querySelector('.form-message');
    if (existingMessage) {
      existingMessage.remove();
    }

    // Create message element
    const messageEl = document.createElement('div');
    messageEl.className = `form-message ${type}`;
    messageEl.textContent = message;
    messageEl.style.cssText = `
      padding: 1rem;
      margin-top: 1rem;
      border-radius: 0.5rem;
      ${type === 'success' 
        ? 'background-color: #d1fae5; color: #065f46; border: 1px solid #10b981;' 
        : 'background-color: #fee2e2; color: #991b1b; border: 1px solid #ef4444;'}
    `;

    // Insert after form
    contactForm.insertAdjacentElement('afterend', messageEl);

    // Auto-remove success messages after 5 seconds
    if (type === 'success') {
      setTimeout(() => messageEl.remove(), 5000);
    }
  }
});

