# Optimize checklist for non-Webflow sites

Source: https://university.webflow.com/resources/checklists/optimize-checklist-for-non-webflow-sites

## Learn the platform

- [ ] **Get familiar with Optimize**

  Webflow Optimize helps you test and personalize site experiences, so you can move from guessing what works to learning from real visitor behavior. That’s what makes the upfront investment worth it: once you understand the core concepts, every optimization becomes easier to plan, build, measure, and improve.

  Start by getting familiar with optimizations, variations, goals, audiences, and results. These are the building blocks you’ll use every time you launch a test or personalization. The clearer they are upfront, the easier it is to create optimizations that answer useful questions.

  **Pro tips:**

  - Block 60–90 minutes of uninterrupted time for this. It’s worth the investment upfront.
  - Share the following resources with your broader team so everyone speaks the same language:- [Intro to Optimize](https://help-optimize.webflow.com/hc/en-us/articles/41215243699091-Intro-to-Webflow-Optimize)
    - [Conversion Rate Optimization (CRO) best practices](https://help-optimize.webflow.com/hc/en-us/articles/42465676267923-Conversion-rate-optimization-CRO-best-practices)
    - [Key concepts for optimizing webpages](https://help-optimize.webflow.com/hc/en-us/articles/43059791440019-Key-concepts-for-optimizing-webpages)

  [Learn how Optimize works for non-Webflow sites](https://university.webflow.com/videos/optimize-for-non-webflow-sites) →

## Prepare your setup

- [ ] **Configure user roles & permissions**

  Optimize works best when the right people have the right access. Giving everyone admin access might seem easier upfront, but it can create risk — especially if someone accidentally changes a live test, edits a variation, or updates settings that affect your data.

  Before you invite teammates, decide who should manage setup, who can create and launch optimizations, who can review results, and who should receive alerts.

  **Pro tips**

  - Map your team structure first before assigning [Optimize site roles](https://help-optimize.webflow.com/hc/en-us/articles/41108662124435-Optimize-site-roles-and-permissions). You’ll likely have admins, editors, and viewers.
  - Give launch and edit permissions only to teammates who are responsible for managing optimizations.
  - Turn on [email alerts](https://help-optimize.webflow.com/hc/en-us/articles/41242003105683-Turn-email-alerts-on-or-off) for key status changes so your team doesn’t have to manually check in.
  - Revisit permissions when your team changes. Access has a way of outlasting the work it was originally granted for.

  [Learn how to configure your team](https://help-optimize.webflow.com/hc/en-us/articles/43244015207699-Webflow-Workspace-overview-help-topics#h_01K0WKW1M6Y1RTP7RRS532M2VC) →

- [ ] **Install the Optimize JavaScript snippet**

  The Optimize JavaScript snippet is what connects Webflow Optimize to your website. Without it, Optimize can’t run variations, track visitor engagement, or collect results. For non-Webflow sites, you’ll need to work with your developer or web team to add the snippet to the pages you want to optimize.

  For best results, add the snippet to every page on your site. At minimum, add it to any page where optimizations will run and any page where conversions happen. The snippet should be placed as high in the page’s <head> as possible so Optimize can initialize quickly.

  **Pro tips**

  - Use the snippet from your Optimize account settings. Each site has a unique snippet.
  - Add the snippet to a base page template when possible, so it’s included consistently across the site.
  - Don’t use a tag manager, lazy loading, custom caching, or deferred loading to inject the snippet.
  - Ask your developer to verify the snippet is firing on all target pages, not just the homepage.
  - If your site uses a single-page app, Content Security Policy, Shopify, or Cloudflare Rocket Loader, review the special setup guidance before launch.

  [Learn how to install the snippet](https://help-optimize.webflow.com/hc/en-us/articles/40681823174547-Install-the-Optimize-JavaScript-snippet) →

- [ ] **Set up relevant integrations**

  Optimize becomes more powerful when it’s connected to your existing marketing stack. Integrations let you share data between Optimize and tools like HubSpot, Marketo, Google Analytics, and more — giving you richer audience targeting, better conversion tracking, and a clearer view of how optimizations affect downstream metrics.

  Identify which integrations matter most for your team before you start running tests.

  **Pro tips**

  - Prioritize the tools your team already uses to measure conversion. Your analytics platform is usually a good place to start.
  - If you use HubSpot or Marketo, set those integrations up early so you can use account-level goal tracking directly in the dashboard.
  - Document which integrations are live and what data they’re passing, so future team members understand your setup.

  [Set up Optimize integrations](https://help-optimize.webflow.com/hc/en-us/categories/40635747472403-Setup-integrations) →

- [ ] **Set up your goals**

  Goals are how Optimize knows whether your experiments are working. Without them, you’re running tests blind. Goals define the conversions you care about most — things like form submissions, button clicks, page views, or custom events — and help you measure success consistently across optimizations.

  Set up a small number of high-value goals before launching your first test, so your results are easier to compare and act on.

  **Pro tips**

  - Don't try to track everything at once. Start with 2–3 goals that map directly to your business KPIs.
  - Choose a single primary goal per optimization so your results have a clear signal.
  - [Click goals](https://help-optimize.webflow.com/hc/en-us/articles/41354139222803-Create-or-edit-a-click-goal) are a good starting point for form buttons, CTA clicks, and key navigation paths.

  **NOTE:** If you have an integration with Hubspot or Marketo you can set up site goals directly within the dashboard. For all other goals, please reach out to you Customer Success Manager or [Customer Support](https://support.webflow.com/resources/optimize-support).

  [Learn how optimization goals work](https://help-optimize.webflow.com/hc/en-us/articles/41334663593107-Optimization-goals-overview) →

- [ ] **Set up audiences for testing & personalization**

  Audiences help you decide who should see each optimization experience. Use them to focus a test on a specific group of visitors, or to personalize content for audiences with different needs, intent, or context. You can start simple like visitors from a campaign, region, device type, or referral source, and then build more advanced audience rules as your program grows.

  **Pro tips**

  - Start with audience segments that map to a clear visitor need, like paid campaign traffic, regional visitors, returning visitors, or high-intent accounts.
  - Use audiences for focused tests when you want to learn how a specific group responds to a change.
  - Use audiences for personalization when you already know different groups should see different messages or experiences.
  - Keep your first audiences simple. Clear audience rules are easier to QA, explain, and learn from.
  - Before publishing, double-check that each audience matches the visitors you want to include or exclude

  [Learn how to build and use optimization audiences](https://help-optimize.webflow.com/hc/en-us/articles/41546786254227-Set-an-optimization-s-audience) →

## Start optimizing

- [ ] **Put together your testing roadmap**

  The biggest mistake teams make is running one-off experiments with no strategy behind them. A testing roadmap gives you a structured backlog of hypotheses, ranked by potential impact and effort, so you’re always running the most valuable test next — not just the first idea someone had.

  It also makes your program predictable. Stakeholders can see what’s coming, why it matters, and how each test supports your site goals.

  **Pro tips**

  - Anchor every test idea to a specific goal. If you can't connect it to a metric, it's not ready to test.
  - Use the ICE framework (Impact, Confidence, Ease) to prioritize your backlog.
  - Start with high-traffic, high-intent pages like your homepage, pricing page, or primary landing pages — you need traffic to reach statistical significance.
  - Share [these optimization ideas](https://help-optimize.webflow.com/hc/en-us/articles/43059794783763-General-optimization-ideas) with your team if you're starting from a blank slate.

  [Read the ultimate guide to website optimization](https://cdn.prod.website-files.com/6220f3e30d60ec3ef9a240d3/679262962f6ea97c1ccf9ed8_Ebook_Ultimate%20guide%20to%20website%20optimization.pdf) →

- [ ] **Set up your first test and publish**

  This is where theory meets practice. Optimize supports multiple experiment types, including traditional A/B tests, redirect tests, and AI-powered optimizations. Your first test doesn’t need to be your boldest one. Pick a clear hypothesis, a high-traffic page, and a variation you can build quickly.

  For non-Webflow sites, you’ll build most simple changes in the [Optimize visual editor](https://help-optimize.webflow.com/hc/en-us/articles/41106757597331-Overview-of-the-visual-editor). Use the [code editor](https://help-optimize.webflow.com/hc/en-us/articles/41741051600659-Writing-custom-code-in-Optimize) when you need more advanced JavaScript or CSS.

  **Pro tips**

  - Start with a manual A/B test if you’re new to Optimize, so you understand the mechanics before using more advanced options.
  - Use [AI Optimize](https://help-optimize.webflow.com/hc/en-us/articles/41687256687251-Create-AI-Optimize-optimizations) when you want the platform to test multiple variations and route traffic based on performance.
  - Use [redirect variations](https://help-optimize.webflow.com/hc/en-us/articles/41717699150867-Set-a-redirect-variation) when you’re testing a completely different page layout or design.

  - QA your variation before going live. Check desktop, tablet, and mobile.

  [Create a test optimization](https://help-optimize.webflow.com/hc/en-us/articles/41676401019667-Create-test-optimizations) →

- [ ] **Review test results**

  Running a test is only half the job. Reading the results correctly is where the value is actually created. Optimize surfaces performance data for each variation, including conversion rates, statistical significance for A/B tests, and Variation Strength for AI Optimize.

  Understanding how to interpret these metrics — and when a test has run long enough to call a winner — is a skill that compounds over time.

  **Pro tips**

  - Don’t call a winner too early. Statistical significance of 95% or higher is the standard threshold for A/B tests.
  - For AI Optimize, use Variation Strength as your signal. It shows which variations the algorithm is favoring based on real visitor behavior.
  - Use result filters to segment performance by device, audience, or traffic source. The top-line numbers don’t always tell the full story.
  - Document what you learned from every test, win or lose. Losing tests are often the most instructive.

  [Learn how to view optimization results](https://help-optimize.webflow.com/hc/en-us/articles/41222262265363-Review-optimization-results) →

- [ ] **Ongoing test maintenance**

  Once your program is running, maintenance keeps it healthy. This means stopping tests that have concluded, adjusting variation status or traffic allocations as needed, cloning high-performing variations for new experiments, and watching for anything that could affect data quality — like site updates that change a page’s layout or break a variation.

  A clean test environment is a faster, more reliable test environment.

  **Pro tips**

  - Stop traditional A/B once you’ve reached a decision. Leaving them running longer doesn’t necessarily improve the result, and it can waste useful traffic.
  - When you publish a site update that touches a page with an active test, check that your variations still render correctly.
  - Clone winning or useful variations before making follow-up changes.
  - Review FAQ and troubleshooting docs when goals aren’t firing, variations aren’t showing, or results look unexpected.

  [Learn how to stop an optimization](https://help-optimize.webflow.com/hc/en-us/articles/41682234952723-Stop-a-test-optimization) →

## Start personalizing

- [ ] **Launch a personalization optimization**

  Personalization is one of the most advanced capabilities in Optimize — and one of the most powerful when done right. Instead of showing every visitor the same experience, you can define audience segments based on rules like UTM parameters, referral source, geolocation, device, or behavior, then serve each segment a tailored version of your page.

  This is especially valuable for paid campaigns, account-based marketing, and high-intent landing pages where relevance can directly influence conversion.

  **Pro tips**

  - Start with a high-signal segment you already understand, like visitors from a specific paid campaign or a key account list.
  - Rules-based audiences are easier to build and maintain. Use code-based audiences when you need to reference custom data attributes or integrate with your CRM.
  - Set variation order carefully, since it controls priority when a visitor qualifies for multiple segments.
  - Personalization should still be tied to a clear goal. Don’t personalize just to personalize — know what conversion you’re trying to move.
  - If you’re setting up ABM-style personalization, align with your Customer Success Manager or account team on the best approach.

  [Create a personalization optimization](https://help-optimize.webflow.com/hc/en-us/articles/41645907766291-Create-personalize-optimizations) →
