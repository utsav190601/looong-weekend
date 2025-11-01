# Contact Form Setup Guide

## Current Status
The contact form currently only validates and shows a success message, but **doesn't actually send emails**.

## ✅ Solutions for Static Websites

### Option 1: Formspree (Recommended - Easiest)

**Free tier**: 50 submissions/month

1. **Sign up**: Go to https://formspree.io
2. **Create a form**: Add your email
3. **Get form endpoint**: You'll get a URL like `https://formspree.io/f/YOUR_FORM_ID`
4. **Update contact form**: Change the form action to your Formspree URL

**Update `contact.html`**:
```html
<form id="contact-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
  <!-- form fields stay the same -->
</form>
```

### Option 2: EmailJS (Free)

**Free tier**: 200 emails/month

1. **Sign up**: Go to https://www.emailjs.com
2. **Create email service**: Connect Gmail/Outlook
3. **Get Service ID, Template ID, Public Key**
4. **Add script to contact.html**:
```html
<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
<script>
  emailjs.init("YOUR_PUBLIC_KEY");
</script>
```

### Option 3: Netlify Forms (If hosting on Netlify)

Just add `netlify` attribute to form:
```html
<form netlify name="contact" method="POST" data-netlify="true">
```

### Option 4: Custom Backend API

Requires:
- Backend server (Node.js, Python, etc.)
- Email service (SendGrid, Mailgun, etc.)
- API endpoint to receive form data

## 🚀 Quick Setup: Formspree (Recommended)

### Step 1: Create Formspree Account
1. Visit: https://formspree.io/register
2. Verify your email
3. Click "New Form"
4. Copy your form endpoint URL

### Step 2: Update Contact Form
Replace the form in `contact.html`:

```html
<form id="contact-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
  <input type="hidden" name="_subject" value="New Contact Form Submission">
  <input type="hidden" name="_replyto" value="">
  
  <!-- Rest of form fields -->
</form>
```

### Step 3: Update JavaScript
Modify `assets/js/main.js` to keep validation but allow form submission:

```javascript
// Remove e.preventDefault() if form action is set
// Or keep it and use fetch() to send to Formspree
```

## 📧 Alternative: Direct Email Link

If you don't want form submissions, you can replace the form with a simple email link:

```html
<a href="mailto:info@thelooongweekend.com?subject=Inquiry&body=Hello..." class="cta-button">
  Email Us Directly
</a>
```

## 🔧 Need Help Setting Up?

I can help you:
1. Set up Formspree integration
2. Set up EmailJS integration  
3. Create a backend endpoint
4. Configure any other email service

Let me know which option you prefer!

