# SEO Checklist

Source: https://university.webflow.com/resources/checklists/seo-checklist

## Design and build with SEO in mind

- [ ] **Plan a clear site structure and navigation**

  Site structure refers to how your website’s pages are organized and linked together. A clear, logical navigation system helps users find content easily and improves how search engines crawl and index your pages.

  A well-structured site improves user experience, reduces bounce rates, and boosts SEO by ensuring search engines can efficiently crawl and index all your pages. It also helps distribute link equity across your site, strengthening important pages.

  **Pro tips:**

  - Keep your site’s structure shallow (no more than three clicks from the homepage to any page).
  - Use Webflow’s navigation components to create a consistent and accessible menu.
  - Include a clear hierarchy with categories and subcategories.
  - Implement internal linking to guide users to related content.

  [Learn more about site structure and SEO](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Ensure site is responsive for desktop and mobile**

  Responsive web design ensures that a website adapts to different screen sizes and devices, providing an optimal user experience across desktops, tablets, and mobile phones. Webflow’s breakpoints feature allows you to customize styles for different screen sizes, ensuring a smooth design across devices.

  Google prioritizes mobile-friendly websites in search rankings. A responsive design improves usability, reduces bounce rates, and ensures accessibility for a broader audience. Websites that aren't mobile-friendly may experience lower rankings and higher bounce rates.

  **Pro tips:**

  - Use Webflow’s breakpoints to adjust layouts for various screen sizes.
  - Implement flexible grid layouts, responsive images, and media queries.
  - Optimize text sizes, button spacing, and navigation for touchscreens.
  - Use Webflow’s built-in preview tools to test your design across different devices.

  [Breakpoints in Webflow](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Keyword research and optimization**

  Keyword research is the process of identifying the words and phrases that people use in search engines to find content related to your website. Optimizing for these keywords helps your site appear in relevant search results.

  Targeting the right keywords — both branded and non-branded — ensures your content reaches the right audience. Strong keyword optimization can increase organic traffic, improve rankings, and help search engines understand your content.

  Using tools like Google Keyword Planner can help you find high-impact keywords. Focus on long-tail keywords (more specific phrases) for better targeting. Naturally integrate keywords into page titles, headers, and content.

  [Learn more about keywords](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Use a logical header hierarchy (H1-H6) for clear content structure**

  Headings organize content, making it easier for users and search engines to read and understand.

  Styling text to look like a heading without setting the correct tag won’t help SEO. Proper headings improve SEO, readability, and accessibility. They help search engines understand the hierarchy and structure of your content, which improves your SEO.

  There are 6 tag options for Headings ranging from largest to smallest: H1, H2, H3, H4, H5, and H6.

  **Pro tips:**

  - Use H1 for the main page title (only one per page), H2 for sections, and H3-H6 for subsections.
  - Keep them clear, concise, and keyword-friendly.
  - Include relevant keywords in your headings.

  [Headings in Webflow](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Use HTML5 Semantic Tags to define page structure**

  HTML5 semantic tags (e.g., <header>, <nav>, <article>, <section>, <footer>) help define the structure of a webpage, making it more understandable for both users and search engines.

  Semantic tags improve SEO by helping search engines better interpret page content. They also enhance accessibility, as screen readers and assistive technologies rely on them for navigation. Properly structured content is more user-friendly and ranks better in search results.

  Webflow provides built-in semantic elements that allow you to set proper tags for sections, headers, and navigation without writing code. When adding a Section, Container, or Div Block, use the Tag dropdown in the Element Settings panel to specify the correct HTML5 tag. This ensures your design is SEO-friendly while maintaining accessibility best practices.

  [Semantic HTML5 tags in Webflow](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Design a logical and user-friendly navigation menu**

  A navigation menu is a set of links that helps users move through a website. A well-organized menu improves user experience and helps search engines understand site structure.

  Clear navigation keeps visitors engaged, reduces bounce rates, and improves SEO by helping search engines crawl and index pages efficiently.

  **Pro tips:**

  - Keep menus simple and prioritize key pages.
  - Use Webflow’s Navbar element to create a structured menu.
  - Ensure dropdowns are easy to use, and link to important internal pages.

  [Navbar element in Webflow](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Create clear and intuitive page URLs**

  URL structure refers to the way web addresses are formatted. A well-structured URL is short, descriptive, and includes relevant keywords, making it easier for users and search engines to understand page content. Webflow allows you to customize URL slugs for each page.

  Clean, keyword-rich URLs improve SEO by helping search engines determine page relevance. User-friendly URLs also increase click-through rates (CTR) and enhance the overall user experience. In Webflow, go to the Page Settings to edit the slug (your URL) for each page.

  **Pro tips:**

  - Keep URLs short (under 75 characters).
  - Use hyphens instead of underscores.
  - Make them descriptive, but simple.
  - Ensure consistency in naming conventions across the site.
  - Be sure to set up a 301 redirect if you ever change one of your URLs.

  [Page URLs in Webflow](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Create meta titles and meta descriptions for each page**

  Meta titles and descriptions are HTML elements that summarize a page’s content for search engines and users. They appear in search results and help determine whether users click on your link. Webflow allows you to easily set and edit these in the page settings.

  Well-optimized meta titles and descriptions improve click-through rates (CTR) and help search engines understand your page’s relevance. A compelling description can encourage more clicks, driving traffic to your site.

  **Pro tips:**

  - Keep meta titles under 60 characters and descriptions under 160 characters.
  - Use primary keywords naturally, write engaging copy, and make sure each page has a unique meta title and description.

  [SEO titles and meta descriptions in Webflow](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Set up Open Graph settings for social sharing**

  Open Graph (OG) is a technology that social networks like Facebook, LinkedIn, X (Twitter), etc., use to pull data from your site when you share the URL of your site on those services. You can specify the information shared in your site’s link previews with Open Graph settings.

  Proper Open Graph settings improve click-through rates (CTR) by ensuring your shared links look polished and engaging. You can view and set the Open Graph settings for each page in your page settings.

  Open Graph content works best when it’s specific to the page being shared. For example, your home page’s Open Graph content should be different from your pricing page’s Open Graph content. You can’t set Open Graph tags globally, and Open Graph tags apply only to the page on which you’ve set the settings — so it’s best practice to set Open Graph tags for each of your pages.

  [Open Graph settings in Webflow](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Add descriptive alt text to images**

  Alt text (alternative text) is a written description of an image that helps search engines and screen readers understand its content. It improves website accessibility for visually impaired users and helps search engines index images for relevant searches. It also provides context when images fail to load.

  **Pro tips:**

  - Describe the image’s purpose, not just its appearance. Instead of "blue button," say "blue ‘Sign Up’ button."
  - Keep it concise but meaningful—aim for 125 characters or less.
  - Include important keywords naturally. For example, "Webflow dashboard with CMS collection settings" instead of "screenshot of Webflow."
  - Avoid redundancy—no need to say "image of" or "picture of," since screen readers already announce it’s an image.

  [Alt text in Webflow](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Ensure you are creating quality content (E-E-A-T)**

  Google aims to surface the most reliable, trustworthy, and valuable content for any query. Content that demonstrates expertise and credibility is more likely to rank higher in search results. Well-written content also improves user engagement, reduces bounce rates, and builds trust with your audience.

  A good rule of thumb is to follow [E-E-A-T](https://university.webflow.com/resources/checklists/seo-checklist#), Google's guideline for evaluating content quality. E-E-A-T stands for Experience, Expertise, Authority, and Trustworthiness.

  Create high-quality content that is well-researched, informative, and valuable to the user, and make sure your content is unique and matches your audience’s search intent.

  [Learn more about Google's content criteria](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Enable SSL Certificate for secure HTTPS**

  An SSL certificate encrypts data transferred between a website and its visitors, ensuring secure communication. Websites with SSL use HTTPS instead of HTTP.

  Google prioritizes HTTPS websites in search rankings, and unsecured sites may display a warning in browsers. SSL protects user data, builds trust, and improves SEO.

  When you host with Webflow, you automatically get a free SSL certificate, eliminating the need for manual setup. Be sure to enable SSL in Webflow’s Site Settings before launching your site.

  Webflow customers on Enterprise plans can also upload custom SSL certificates for increased flexibility in site hosting.

  [SSL Certificates in Webflow](https://university.webflow.com/resources/checklists/seo-checklist#) →

## Set up & track SEO performance

- [ ] **Set up Google Search Console**

  Google Search Console is a free tool from Google that helps you monitor and optimize your website’s presence in search results. It provides insights into indexing, performance, and any issues affecting your site’s visibility.

  Follow these steps to set up Google Search Console:

  1. Add your site to your Google Search Console account
  2. Paste the Verification ID in Webflow Site Settings
  3. Finish verifying your site in Google Search Console

  For step by step instructions, visit our [Google site verification Help Center article](https://university.webflow.com/resources/checklists/seo-checklist#).

  [Get started with Google Search Console](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Set up analytics tools**

  Analytics tools like Google Analytics help track visitor behavior, traffic sources, and engagement on your website. These tools provide valuable insights into how users interact with your content.

  Understanding user behavior allows you to optimize your website for better user experience, conversions, and SEO performance. Analytics data helps identify high-performing pages and areas that need improvement.

  **Pro tip:** For a more user-friendly and beginner-friendly option, [Webflow Analyze](https://university.webflow.com/resources/checklists/seo-checklist#) offers real-time insights, effortless setup, and key performance metrics—all without leaving Webflow.

  [Get started with Google Analytics](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Set up your Google Business Profile**

  Google Business Profile is a free tool that allows businesses to manage their online presence on Google Search and Google Maps. It helps people find your business, see your hours, read reviews, and contact you.

  Having a well-optimized profile improves your chances of appearing in local search results, attracting more customers, and building trust with potential clients. Make sure your business name, address, and phone number are accurate and match across all platforms. Add high-quality photos, respond to customer reviews, and update your profile regularly.

  [Get started with Google Business Profile](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Connect SEO Apps from the Webflow Marketplace**

  Webflow’s Marketplace offers third-party SEO apps and integrations that help automate optimizations, track rankings, and improve technical SEO.

  These tools can enhance Webflow’s built-in SEO features by providing deeper insights into site performance, keyword tracking, and backlink analysis.

  **Pro tip:** The [Google site tools for Webflow app](https://university.webflow.com/resources/checklists/seo-checklist#) brings insights from Google Search Console and Google Analytics directly into Webflow. This makes it easier and faster to improve your site's visibility, gain a clear understanding of your customers and make data-informed decisions to grow marketing ROI.

  [Check out SEO apps in Webflow](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Set up Google Tag Manager**

  Google Tag Manager is a tool that allows you to manage marketing, analytics, and tracking scripts without manually editing your site’s code. It helps improve page speed and SEO performance by reducing the number of scripts that load directly on your Webflow site.

  Google Tag Manager also enables better tracking of SEO metrics, like user behavior, engagement, and Core Web Vitals, which influence rankings.

  [Learn more about Google Tag Manager](https://university.webflow.com/resources/checklists/seo-checklist#) →

## Ensure a search-ready launch

- [ ] **Submit your Webflow sitemap to Google Search Console**

  A sitemap (or XML sitemap) is a file that lists all the pages on your website, helping search engines understand your site’s structure and index pages efficiently. Submitting your sitemap to Google Search Console ensures Google can find and crawl all your content.

  When you host your site with Webflow, you can [automatically generate a sitemap](https://university.webflow.com/resources/checklists/seo-checklist#) or [add your own](https://university.webflow.com/resources/checklists/seo-checklist#). Webflow’s [auto-generated sitemap](https://university.webflow.com/resources/checklists/seo-checklist#) feature automatically generates a sitemap.xml for your site and updates it each time you publish any new content to your site.

  **IMPORTANT:** Once you’ve generated your sitemap, you’ll need to tell Google about your sitemap by [submitting it to Google Search Console](https://university.webflow.com/resources/checklists/seo-checklist#).

  [Sitemaps in Webflow](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Disable indexing of your webflow.io subdomain or custom staging subdomain**

  Webflow automatically generates a staging subdomain (e.g., yoursite.webflow.io) to preview and test your site before publishing. However, search engines can index these temporary domains if they’re not blocked, leading to duplicate content issues.

  If Google indexes your staging site, it can compete with your live domain in search results, reducing SEO effectiveness and causing confusion. Preventing indexing ensures that only your published site appears in search rankings.

  Thankfully, you can easily avoid the whole duplicate problem with one click. Just toggle “disable subdomain indexing” from your Site Settings and you’ll be good to go.

  [Disable indexing of your staging subdomain in Webflow](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Set up proper 404 error pages with useful navigation**

  A 404 page appears when a user tries to visit a page that doesn’t exist. Custom 404 pages improve user experience by providing helpful navigation rather than leaving visitors at a dead end.

  A well-designed 404 page reduces bounce rates by guiding users back to relevant content. It also improves SEO by keeping visitors engaged instead of exiting your site.

  The 404 page is located under the Utility Pages section of the Pages panel. You can customize the default 404 page of your site and design it as you like.

  [404 error pages in Webflow](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Minify CSS, JavaScript, and HTML**

  Minification removes unnecessary characters (like spaces, comments, and line breaks) from CSS, JavaScript, and HTML files, making them smaller and improving site speed.

  Smaller files load faster, improving page performance, SEO, and user experience. Search engines prioritize fast-loading sites, and minification helps reduce page load times.

  [Minify code in Webflow](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Compress images to improve load speed**

  Large images slow down page speed, which can negatively impact rankings and increase bounce rates. Faster sites provide a better user experience and are prioritized by search engines.

  Image compression reduces file sizes without sacrificing quality, helping websites load faster. Optimized images improve both user experience and SEO rankings.

  With Webflow's built-in **image conversion tool**, you can compress existing image assets (JPEG, JPG, PNG, and WebP assets) by converting them to AVIF or WebP files. This will convert the asset’s file type in both the Assets panel and any instances of that asset on the canvas.

  The WebP image file format (e.g., “image.webp”) and AVIF image file format (e.g., “image.avif”) retain most of an image’s high quality while compressing it into a smaller file size. This helps web pages load faster and saves website storage space.

  [Compress images in Webflow](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Use 301 redirects when needed**

  A 301 redirect is a permanent redirection from one URL to another. It ensures users and search engines are directed to the correct page when URLs change or old pages are removed.

  Without proper redirects, visitors may land on broken pages (404 errors), hurting SEO and user experience. A 301 redirect preserves link equity (ranking power) from the old URL and helps search engines understand the new page’s location.

  [301 redirects in Webflow](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Set a global canonical tag**

  When there are multiple versions of a page with duplicate content, canonical tags (also known as rel="canonical" tags) tell search engines which webpage is the primary or preferred version to display in search results.

  Duplicate content can impact search rankings. Canonical tags prevent these issues by directing search engines to the intended version of your content you want to appear in search results. They also consolidate ranking signals (e.g., backlinks) to the preferred version, which concentrates SEO efforts on a single URL and increases its chances of ranking higher in search results.

  You can set a global canonical tag to automatically create canonical tags for every page on your site.

  [Global canonical tags in Webflow](https://university.webflow.com/resources/checklists/seo-checklist#) →

## Refine and expand SEO performance

- [ ] **Disable search engine indexing of specific pages**

  You can control which pages search engines crawl on your site by writing a robots.txt file or by adding a noindex tag to certain pages. Then, you can prevent search engines from crawling and indexing specific pages, folders, your entire site, or your webflow.io subdomain. This is useful for hiding pages — like your site’s 404 page — from being indexed and listed in search results.

  [Disable indexing of specific pages in Webflow](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Implement schema markup**

  Search engines can’t interpret everything on their own — sometimes, they need help. Schema markup (structured data) is a type of code that helps search engines understand content better. It enables rich search results like FAQs, breadcrumbs, and product listings.

  Adding schema markup to a page is like sticking labels to your content to identify essential features such as an article title, product price, or business location. Done correctly, schema markup gives search engines the information they need to deliver better search results.

  [Learn more about schema markup](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Implement localized SEO with Webflow Localization**

  Localization is the process of adapting your site to meet the cultural and linguistic needs of visitors worldwide. With Webflow Localization, you can create customized experiences for different audiences based on their language and region, which enhances user engagement and improves SEO.

  **How Webflow Localization supports SEO:**

  - [**Localized URLs**](https://university.webflow.com/resources/checklists/seo-checklist#) **:** Webflow automatically creates language-specific folder structures (e.g., /en/ for English, /es/ for Spanish) to help search engines understand language and regional targeting. On advanced plans, you can also customize page slugs (e.g., /es/localized-slug), an important SEO factor.
  - [**Hreflang tags**](https://university.webflow.com/resources/checklists/seo-checklist#) **:** Webflow automatically adds hreflang annotations in both the sitemap and tags to indicate language and regional variants of each page. This helps search engines deliver the right content to the right users.
  - [**HTML lang attribute**](https://university.webflow.com/resources/checklists/seo-checklist#) **:** Webflow sets the HTML lang attribute for each locale, ensuring that search engines, browsers, and assistive technologies correctly interpret the primary language of your content.
  - [Locale routing](https://university.webflow.com/resources/checklists/seo-checklist#) **:** Webflow directs users to the most relevant language version of your site based on their location or preferences, improving accessibility and engagement.

  **Pro tip:** With Webflow Localization, you can customize SEO settings before launch, ensuring that titles, meta descriptions, and structured data are fully optimized for each locale.

  [Learn more about Webflow Localization](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Optimize for other search engines**

  While Google dominates search traffic, other search engines like Bing, DuckDuckGo, Yahoo, and Yandex still drive traffic, especially in specific regions and industries. Optimizing for them expands your reach and diversifies traffic sources.

  Be sure to research each search engine's SEO requirements — Google's tactics don’t always work the same way for other search engines.

  [Learn more about optimizing for other search engines](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Optimize for AI-driven search (e.g. Google AI Overview, ChatGPT, etc.)**

  AI-driven search results, like Google’s AI Overview, ChatGPT, and Bing Copilot, are changing how users discover information. Instead of traditional search results, AI-generated answers provide summarized responses, often pulling from multiple sources.

  This shift has led to a new SEO focus called Generative Engine Optimization (GEO), where sites that structure content effectively have a better chance of being featured in AI-generated responses, driving more visibility and traffic.

  [Learn more about generative engine optimization](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Optimize for Google Featured Snippets**

  Featured snippets are high-visibility search results that appear at the top of Google’s SERPs, providing quick answers to user queries. They often come in the form of paragraphs, lists, tables, or Q&A formats.

  Being featured in a snippet boosts organic traffic, increases credibility, and improves click-through rates (CTR) by positioning your content above standard search results.

  [Learn more about Google Featured Snippets](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Test and optimize your content**

  Readable, engaging content keeps users on your site longer and improves SEO. Search engines prioritize content that provides a great user experience, which includes clear structure, concise language, and easy-to-read formatting.

  Content optimization is an iterative process you can continually build on over time. Start small with targeted experiments for a subset of your audience, learn from the results, and gradually scale your testing program as you gather insights.

  **Webflow Optimize** makes this easier than ever — it helps you test, experiment, and optimize your content to increase conversions. With Webflow Optimize, you can run A/B tests to compare different versions of headings, CTAs, or formatting to see what resonates most with your audience.

  [Get started with Webflow Optimize](https://university.webflow.com/resources/checklists/seo-checklist#) →

- [ ] **Run regular site audits to maintain SEO health**

  A site audit is a routine check-up for your website’s SEO, performance, security, and accessibility to catch and fix issues before they impact rankings and user experience. Websites change over time—new content, page updates, and technical tweaks can introduce errors. Regular audits help prevent broken links, slow-loading pages, crawl issues, and outdated metadata, ensuring ongoing optimization.

  There are many free and paid site audit tools available to help you perform a thorough website audit. They look for factors that might harm your website’s organic performance, like slow page loads and duplicate content, and offer resources like link-building tools, keyword research tools, and more.

  **Pro tips:**

  - Schedule audits monthly or quarterly to catch issues before they affect traffic and rankings.
  - Automate checks where possible using SEO tools while also performing manual reviews for accuracy.
  - Review [Google Core Web Vitals](https://university.webflow.com/resources/checklists/seo-checklist#) regularly. They focus on loading speed, interactivity, and visual stability, which impact rankings and engagement. Websites that meet Core Web Vitals thresholds are more likely to rank higher in search results and provide a smoother experience for visitors.

  [Learn more about site audits and site audit tools](https://university.webflow.com/resources/checklists/seo-checklist#) →
