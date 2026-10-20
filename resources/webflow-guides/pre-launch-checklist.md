# Pre-launch checklist

Source: https://university.webflow.com/resources/checklists/pre-launch-checklist

## Design & Content Review

- [ ] **Review layout and visual consistency**

  Check for clean spacing, alignment, and consistent use of styles across all pages. A visually cohesive site looks more professional and builds trust with your visitors.

  **Pro tips:**

  - Use Webflow’s Navigator panel and guides to spot misaligned or overlapping elements
  - Scan for inconsistent button sizes, margins, or font treatments
  - Use global classes, components, and variables where possible to maintain consistency

  [Design system checklist](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Test responsiveness on all breakpoints**

  Make sure your layout adapts smoothly across desktop, tablet, and mobile. A great desktop design doesn’t guarantee a great mobile experience.

  **Pro tips:**

  - Use Webflow’s built-in breakpoints to test across common screen sizes
  - Pay special attention to image scaling, nav behavior, and stacked content
  - Test on real devices with your staging site for final validation

  [Breakpoints in Webflow](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Proofread site copy**

  Clear, polished copy improves your credibility and helps visitors understand your content. Typos and awkward phrasing are easy to miss but leave a lasting impression.

  **Pro tips:**

  - Watch for leftover placeholder content like “lorem ipsum” or dummy links — they’re easy to miss
  - Read content aloud — it’s easier to catch weird phrasing
  - Double-check headings, buttons, nav labels, and form field text
  - Use Webflow Apps, browser extensions, or other grammar tools for a second pass

  [Browse Webflow Apps](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Spot-check CMS content and filters**

  Review your CMS templates and Collections to make sure content renders correctly and filters/sorts behave as expected.

  **Pro tips:**

  - Test several Collection items (not just the first one)
  - Check filters and conditional visibility logic
  - Look for empty states or missing content fields

  [Webflow CMS help articles](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Review your 404 and utility pages**

  Make sure every page — even the ones your visitors *hopefully* never see — is styled and helpful.

  A well-designed 404 error page provides a better user experience for visitors who encounter a broken link and may help them navigate back to relevant content or your homepage.

  **Pro tips:**

  - Style your 404 page to match your site
  - Write a helpful message or include a link to redirect
  - Preview password and search pages (if used)

  [404 pages in Webflow](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

## Functionality & QA

- [ ] **Test all forms**

  Make sure every form submits successfully, displays the right confirmation, and sends data where it needs to go.

  **Pro tips:**

  - Submit test entries to verify submission and confirmation messages
  - Check form notification emails in Site Settings → Forms
  - Review error states and required field indicators

  [Forms in Webflow](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Click through all links and buttons**

  Broken or misdirected links can create confusion, damage trust, and hurt your site’s SEO.

  **Pro tips:**

  - Use your staging site to manually test all nav links, CTAs, footer links, and inline links
  - Make sure external links open in new tabs (if appropriate)
  - Confirm that all images, PDFs, and downloads load correctly — especially dynamic or linked assets
  - Use Webflow Apps, browser extensions, or other link checking tools for a second pass

  [Browse Webflow Apps](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Confirm animations and interactions work as expected**

  Test all scroll, hover, and click-based animations to ensure they feel purposeful and work on all devices.

  **Pro tips:**

  - Hover effects may not apply on mobile — make sure they’re not essential for usability
  - Test animations across breakpoints and on real devices
  - Remove unused interactions from the Interactions panel to reduce file size

  [Interactions & animations in Webflow](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Check mobile tap targets**

  Ensure buttons and links are easy to tap — and not too close together — on mobile devices.

  **Pro tips:**

  - Tap targets should be at least 44x44 pixels
  - Add spacing between interactive elements to prevent accidental taps
  - Test with your fingers, not just your mouse

  [Learn more about mobile tap targets](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Verify custom code and embed behavior**

  If you’ve added custom code snippets, embeds, or third-party scripts, make sure they load properly and don’t break your layout.

  **Pro tips:**

  - Publish to staging and inspect the page for errors in the browser console
  - Make sure embedded content (e.g. maps, videos) loads at all screen sizes
  - Disable unused scripts or integrations that could slow down your site

  [Custom code help articles](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

## SEO, Accessibility & Performance

- [ ] **Check your heading structure**

  A clear heading structure helps screen readers and search engines understand your content. Take a final pass to make sure it follows a logical order.

  **Pro tips:**

  - Each page should have one <h1>
  - Nest headings in order (<h2> under <h1>, and so on)
  - Avoid skipping heading levels

  [Headings in Webflow](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Review alt text for images**

  Alt text improves accessibility and helps screen readers describe your content. Confirm that all meaningful images, especially in CMS items, have descriptive alt text.

  **Pro tips:**

  - Decorative images can use an empty alt attribute
  - Add or update alt text in the Assets panel or directly on the canvas

  [Alt text in Webflow](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Review page titles and meta descriptions**

  Make sure every page has a unique, descriptive title and meta description. These appear in search results and help users understand what your page is about.

  **Pro tips:**

  - Keep titles under 60 characters and descriptions under 160
  - Use CMS fields to dynamically populate SEO metadata on Collection pages
  - Spot-check [Open Graph settings](https://university.webflow.com/resources/checklists/pre-launch-checklist#) for social previews

  [SEO titles & meta descriptions in Webflow](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Check how your site appears in search and browser previews**

  Small site identity details help tie your experience together — and show up in browser tabs, search previews, and social shares.

  **Pro tips:**

  - Add a [favicon](https://university.webflow.com/resources/checklists/pre-launch-checklist#) in your site settings
  - Check your home page’s [meta title and description](https://university.webflow.com/resources/checklists/pre-launch-checklist#)
  - Upload a social preview image for [Open Graph settings](https://university.webflow.com/resources/checklists/pre-launch-checklist#)
  - Use the site [health scan](https://university.webflow.com/resources/checklists/pre-launch-checklist#) to catch common discoverability issues

  [Run a health scan in Webflow](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Check for large or uncompressed assets**

  Large images and background videos can slow your site down. Make sure your media is optimized for fast load times.

  **Pro tips:**

  - Use WebP or AVIF formats for images
  - Compress assets in the Assets panel or CMS
  - Keep background videos under 5MB

  [Compress images in Webflow](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Minify code and remove unused styles**

  Check that code minification is enabled — and that you’ve cleaned up unused classes and interactions to keep your site lean.

  **Pro tips:**

  - Enable [code minification](https://university.webflow.com/resources/checklists/pre-launch-checklist#) in your site publishing settings
  - Use the broom icon in the Style panel to [remove unused classes](https://university.webflow.com/resources/checklists/pre-launch-checklist#)
  - Delete [unused animations or interactions](https://university.webflow.com/resources/checklists/pre-launch-checklist#) in the Interactions panel
  - Run a [health scan](https://university.webflow.com/resources/checklists/pre-launch-checklist#) to check for common performance issues

  [Run a health scan in Webflow](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Run a final accessibility check**

  Make sure your site works well for everyone, including visitors using assistive technologies.

  **Pro tips:**

  - Use Webflow’s Audit panel to catch common accessibility issues
  - Test keyboard navigation (tabbing through the page)
  - Check color contrast for text and background combinations

  [Webflow Accessibility checklist](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Run a final SEO check**

  Even if you’ve checked the big things like SEO titles, meta descriptions, and structure along the way, it’s worth doing one last SEO pass before publishing. This helps catch anything you may have missed.

  **Pro tips:**

  - Scan key pages for common SEO gaps
  - Use the SEO Checklist for a step-by-step review of best practices
  - Consider crawling your site with tools like Google Search Console or Ahrefs for deeper analysis

  [Webflow SEO checklist](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

## External tools & integrations

- [ ] **Create or update your Google Business Profile**

  If your site represents a business with a physical location or service area, make sure your business profile is accurate and linked to your site.

  **Pro tips:**

  - Verify your profile using your business email or postcard
  - Add your Webflow site link to your profile
  - Make sure contact info, hours, and location are accurate

  [Get started with Google Business Profile](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Set up Google Search Console**

  If your site represents a business with a physical location or service area, make sure your business profile is accurate and linked to your site. Follow these steps to set up Google Search Console:

  1. Add your site to your Google Search Console account
  2. Paste the Verification ID in Webflow Site Settings
  3. Finish verifying your site in Google Search Console

  For step by step instructions, visit our [Google site verification Help Center article](https://university.webflow.com/resources/checklists/pre-launch-checklist#).

  [Get started with Google Search Console](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Check analytics and tracking tools**

  Make sure you’ve set up the right tools to track how people interact with your site. Tools like [Google Analytics](https://university.webflow.com/resources/checklists/pre-launch-checklist#) or [Webflow Analyze](https://university.webflow.com/resources/checklists/pre-launch-checklist#) give you valuable insights into traffic, engagement, and user behavior — so you can make informed decisions after launch.

  **Pro tips:**

  - Use [Webflow Analyze](https://university.webflow.com/resources/checklists/pre-launch-checklist#) for real-time insights and a no-code setup — right inside Webflow
  - Check that your tracking tools (like Google Analytics or Tag Manager) are connected to your Webflow site through Webflow Apps, site settings, Site settings, or through custom code embeds
  - Test key events like pageviews, form submissions, or clicks (if you’re tracking them)

  [Connect Google Analytics to your Webflow site](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Test third-party apps & integrations**

  If you’re using external services (like CRMs, email marketing, or Webflow Apps), confirm that they’re connected and passing data correctly.

  **Pro tips:**

  - Submit test forms or trigger test events
  - Check dashboards or logs in your connected services
  - Reauthorize or reauthenticate apps if anything looks disconnected

  [Browse Webflow Apps](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

## Staging & Publishing Readiness

- [ ] **Test your site on staging**

  Your staging site is the safest place to catch issues before launch. Make sure everything looks and works the way you expect on your Webflow.io domain.

  **Pro tips:**

  - Share your staging link with a teammate for fresh feedback
  - Test forms, links, animations, and mobile layouts
  - Use staging to test final performance or code updates before publishing live

  [Staging in Webflow](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Verify your custom domain is connected and ready**

  Before going live, double-check that your custom domain (like www.yourcompany.com) is fully connected, verified, and showing up as a publishing option.

  **Pro tips:**

  - Check DNS settings in your domain provider and in your site publishing settings
  - Make sure your domain is verified — this is required before publishing
  - Set your preferred domain (e.g. www. or root) as the default to keep things consistent

  [Connect a custom domain in Webflow](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Enable SSL and set indexing preferences**

  Make sure your live site is secure and indexable — and that your staging site stays hidden from search engines.

  **Pro tips:**

  - [Enable SSL](https://university.webflow.com/resources/checklists/pre-launch-checklist#) in your site settings to serve your site securely over HTTPS
  - [Disable search engine indexing for your staging domain](https://university.webflow.com/resources/checklists/pre-launch-checklist#) (e.g., yoursite.webflow.io) to prevent causing duplicate content issues
  - Set up [301 redirects](https://university.webflow.com/resources/checklists/pre-launch-checklist#) for any changed or removed URLs to preserve SEO value and avoid broken links
  - Run a [health scan](https://university.webflow.com/resources/checklists/pre-launch-checklist#) to catch common hosting issues

  [Run a health scan in Webflow](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →

- [ ] **Set publishing permissions**

  Control who can publish your site to staging or production — especially useful when collaborating with clients or teams.

  **Pro tips:**

  - Review [roles & permissions](https://university.webflow.com/resources/checklists/pre-launch-checklist#) in your site settings
  - Limit who can publish to production if needed
  - Encourage use of [single-item publishing](https://university.webflow.com/resources/checklists/pre-launch-checklist#) for safe CMS updates

  [Site roles and permissions in Webflow](https://university.webflow.com/resources/checklists/pre-launch-checklist#) →
