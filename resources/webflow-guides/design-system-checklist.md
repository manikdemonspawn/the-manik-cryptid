# Design system checklist

Source: https://university.webflow.com/resources/checklists/design-system-checklist

## 1. Set up your foundation

- [ ] **Define your design system goals**

  Before diving in, figure out what you're trying to solve. Are you aiming for consistent branding? Faster site building? Easier collaboration? Clear goals not only shape what you build, but also guide decisions about governance, component design, and how your system should evolve as your team or projects grow.

  For instance, if you build multiple sites for clients, creating reusable elements might be your top goal. If you work on a large brand team, it might be consistency and governance.

  **Pro tips:**

  - Get input from your whole team — leaders, designers, developers, marketers, and other stakeholders — to align your goals early.
  - Revisit your goals as your system evolves to ensure they still reflect your needs.

  [Learn how to build effective enterprise design systems](https://webflow.com/blog/enterprise-design-systems#governance-at-scale) →

- [ ] **Choose how you'll organize things**

  Decide how to structure your components and styles so they’re easy to find and reuse. You could organize by layout (e.g. Hero, Footer), function (e.g. Button, Card), or use [Atomic Design](https://atomicdesign.bradfrost.com/) principles (e.g. Atoms > Molecules > Organisms).

  For instance, a site might group components by layout type (e.g. Headers, Footers) while styling elements like text and colors are grouped by purpose (e.g. Typography, Color, Spacing).

  **Pro tips:**

  - Pick a structure that matches how your team thinks and builds.
  - Stick with it. Inconsistent structure can cause confusion and slowdowns.

  [Learn more about creating design systems](https://webflow.com/blog/design-systems) →

- [ ] **Set naming rules and document them**

  Consistent names help everyone stay on the same page. Use a naming pattern for classes, components, and variables. And make a quick guide that explains your system for new teammates.

  For instance, a class named **btn-primary-large** is easier to understand than **button2** — and it’s easier to reuse consistently.

  **Pro tips:**

  - Keep names brief but clear to support maintainability and performance.
  - Use shared language your whole team (and clients) will understand.
  - Share your naming rules somewhere everyone can find them (like a style guide).
  - Document any abbreviations that are part of your system.
  - Prioritize consistency in casing, separators, and naming structure — and stick with your chosen system.
  - Prefix each class type to signal its purpose (e.g. u- for utility, cc- or is- for combo).

  [Learn more about class naming](https://webflow.com/blog/class-naming-101-bem) →

- [ ] **Create a style guide page or site**

  While a design system is more than just a style guide, creating one can provide a helpful, living reference for some of its key parts. It also helps you preview and test global styles, variables, components, layouts, and templates all in one place. This makes it easier to spot inconsistencies, test changes, and onboard new team members.

  For instance, a style guide might include your brand colors, heading and paragraph styles, common components like buttons and cards, and layout spacing guidelines.

  **Pro tips:**

  - Organize your style guide by categories like typography, color, spacing, and components.
  - Include text labels for each style so it’s easy to reference.
  - Keep the style guide updated as your system evolves.
  - Use your style guide site as the source for your Shared [Library](https://help.webflow.com/hc/en-us/articles/33961343551763-Libraries).
  - Use your style guide to test accessibility, spacing, and responsive behavior.

  [Learn more about creating a style guide in Webflow](https://webflow.com/blog/website-style-guide) →

- [ ] **Build accessibility into your system**

  Designing for accessibility means ensuring everyone can navigate and use your site without barriers — including people who are Blind, low vision, visually disabled, Deaf, hard of hearing, or who have cognitive, learning, or mobility disabilities, to name a few. It’s not just the most inclusive way to build, it also helps your brand connect with a wider audience.

  Build accessible patterns into your system from the start by setting clear standards for color contrast, heading levels, alt text, and keyboard navigation. Doing this early prevents rework and ensures your entire team builds inclusively by default. It also makes your system more adaptable and future-friendly.

  For instance, use semantically correct headings inside your components, and create color variables that meet WCAG standards by default.

  **Pro tips:**

  - Use the [Webflow Accessibility checklist](https://webflow.com/accessibility/checklist) and [Webflow Audit panel](https://help.webflow.com/hc/en-us/articles/33961313088531-Intro-to-the-Audit-panel) when designing, updating, and quality checking your system.
  - Document accessibility expectations alongside visual and structural rules.
  - Test your system elements and components with assistive technologies like screen readers, browser zoom and font-size settings, and keyboard-only navigation.

  **Optional starter resource:**

  [Responsive Webflow Style Guide](https://webflow.com/made-in-webflow/website/Responsive-Webflow-Style-Guide-Clone-Remove-unwanted-Webflow-styles) — starts with semantic, accessible structures and includes tips for removing default styles that could interfere with accessibility.

  [Learn more about accessibility](https://university.webflow.com/courses/web-accessibility) →

- [ ] **Get a head start with Marketplace resources**

  Before building your system from scratch, explore free and cloneable design system resources in the Webflow Marketplace. You'll find prebuilt templates, component libraries, and styling frameworks built by Webflow, partners, and trusted community creators. These can help you learn naming strategies, layout conventions, and styling systems — or serve as a strong starting point for your own.

  For instance, [Lumos](https://webflow.com/made-in-webflow/website/lumos-v2-beta), by Timothy Ricks, offers a cloneable style guide and a framework for building Webflow sites designed with efficiency, scaleability, and accessibility at its core.

  **Pro tips:**

  - Browse the [Made in Webflow](https://webflow.com/made-in-webflow) showcase for cloneables tagged with "style guide," "template," or "framework."
  - Use starter frameworks like [Mast](https://webflow.com/made-in-webflow/website/mast-framework) or [Hatch](https://webflow.com/made-in-webflow/website/Hatch-A-Utility-Framework-for-Webflow) to learn scalable patterns.
  - Always customize cloneables to fit your own styles, naming conventions, and content needs.

  [Visit the Webflow Marketplace](https://webflow.com/made-in-webflow) →

## 2. Create reusable styles & components

- [ ] **Add and organize variables**

  Variables (sometimes referred to as “design tokens”) store reusable values like colors, spacing, font sizes, and more. They can be applied to global styles and components alike, helping keep your design consistent and preventing issues like uneven spacing or many similar shades of gray ending up on your site. When you update a variable, changes cascade through your design system automatically.

  Webflow lets you group variables into collections and groups. Collections cover broad categories like primitives or themes, while groups organize related variables like spacing, typography, or components. Use primitives for raw values like **Blue 400** or **1 rem**, and semantics to apply those values in context, like **Card Background** or **Error Border**.

  For instance, you might define a light blue color variable as **Brand Palette / Primaries / Light blue 1**, and reuse that color on multiple text styles and backgrounds.

  **Pro tips:**

  - Start small by creating variables for brand colors, font styles, and base spacing.
  - Use consistent naming conventions like Typography / Heading or Spacing / Section / XL.
  - Preview your variables in use before applying them everywhere.
  - Consider creating a reference section in your documentation to explain how and where each Variable should be used.

  **Optional starter resource:**

  [Lumos](https://webflow.com/made-in-webflow/website/lumos-v2-beta) — by Timothy Ricks, offers a cloneable style guide and a framework for building Webflow sites designed with efficiency, scaleability, and accessibility at its core.

  [Learn more about variables](https://help.webflow.com/hc/en-us/articles/33961268146323-Variables) →

- [ ] **Set up global styles**

  Style selectors control how elements look across your site — from base HTML tags to reusable class and combo class styles. Global styles apply to HTML tags like "All H1 Headings" and are great for setting default typography and spacing. Class selectors offer more specific styling, while combo classes let you layer variations.

  Start with tag styles for your site-wide defaults, then use classes and combo classes to customize. This approach keeps your styling clean, consistent, and scalable.

  For instance, set base styles for all H1s using "All H1 Headings" — like font, size, and color — then apply a class like “Hero-Heading” to layer on specific styles as needed.

  **Pro tips:**

  - Use tag selectors as your starting point for base type styles (H1, Paragraph, List, etc.).
  - Reserve classes for design patterns you'd like to reuse across different element types, like **section-heading** or **highlight-box**.
  - Use combo classes to apply slight variations (like **is-primary** and **is-secondary**).
  - Use [utility classes](https://finsweet.com/client-first/docs/utility-class-systems) like **max-width** or **margin-bottom-small** alongside tag styles to quickly adjust layout without creating new custom classes.

  [Learn more about Style selectors](https://help.webflow.com/hc/en-us/articles/33961365722899-Style-selectors-panel) →

- [ ] **Create components for reusable building blocks**

  There are core parts of a site that you’ll use often, such as navigation, sections, cards, and buttons. Instead of building them from scratch each time, it’s recommended that you start out by turning them into components. Components are reusable building blocks that can make building and updating pages faster and simpler. They are also a powerful way to bring consistency to your designs, especially when multiple people are working on different pages or sites.

  For instance, a Card or Testimonial component might include a quote, avatar, and author name. By standardizing this as a component, anyone on your team can add it to a page, whether they’re working in Design or Build mode, without needing to worry about styling or spacing.

  **Pro tips:**

  - When possible, create components before you start building your site to maximize consistency from the start.
  - If adding components over time, start with the components you use most frequently across pages or projects.
  - Use component Properties, Slots, and style Variants to increase the flexibility of your components (learn more about these options below).
  - Use nested components (like buttons inside cards) to avoid duplication.
  - Lay out and define your components in your style guide so teammates know what’s available.

  **Optional starter resource:**

  [Untitled UI Library](https://webflow.com/made-in-webflow/website/untitled-ui-library) — a robust system featuring reusable and modular components for layouts, cards, navbars, and more (uses the Client-first Webflow Style system).

  [Learn more about components](https://help.webflow.com/hc/en-us/articles/33961303934611-Components-overview) →

- [ ] **Use component properties**

  Component properties let you adjust content, layout, or styling options without detaching or duplicating a component. They can be used to toggle visibility, change text, switch icons, or apply different style variants. This helps teams move faster and reduces the need for multiple components that serve the same core purpose.

  For instance, in a testimonial card component, you could use a text property to set the author name and a property to toggle whether their avatar appears.

  **Pro tips:**

  - Use text properties for headlines, captions, or labels that often change.
  - Use booleans for toggles like “Show image” or “Reverse layout.”
  - Use dropdowns when you want to limit choices and preserve design consistency.
  - Preview each property’s effect before publishing components for others.

  [Learn more about component properties](https://help.webflow.com/hc/en-us/articles/33961219350547-Component-properties) →

- [ ] **Add component Slots for flexible content**

  Slots are placeholders in a component that let you swap out entire blocks of content, such as headlines, images, or CTAs. They allow content editors and marketers to make customizations while keeping the design consistent. These changes can be made without altering the layout or structure of the original component.

  They’re especially useful in components that repeat across a site but need unique content on each page. They’re also helpful when the number of elements within a single component are unknown, such as client testimonials within a component made for a testimonials section.

  For instance, a “Hero” component might include Slots for an optional subheading, background image, and CTA button.

  **Pro tips:**

  - Use Slots for parts of a component that may change, such as whether or not it will include a button, image, or block of text.
  - Lock certain parts of the layout structure to prevent unintended changes or spacing issues.
  - Test Slot behavior with real content to be sure everything flows well visually.
  - Document where and how each slot is meant to be used.

  [Learn more about component Slots](https://help.webflow.com/hc/en-us/articles/33961195339923-Slots) →

- [ ] **Add style Variants to components**

  Variants let you create different stylistic treatments for a single component without duplicating it — all while keeping the core structure the same. They’re perfect for things like theme variations (light/dark), sizing changes, or different visual emphases (primary/secondary). Variants make your components more flexible while keeping updates efficient and centralized.

  For instance, a Button component might have a solid variant and an outline variant to suit different page contexts or visual hierarchies.

  **Pro tips:**

  - Don’t overdo it — start with 2–3 purposeful variants and build from there.
  - Use naming conventions like Primary and Secondary to make them easy to find.
  - Test variants across devices and breakpoints to ensure they’re flexible.
  - Use documentation or preview states to show what each variant is for.

  **Optional starter resource:**

  [Relume Library Style Guide](https://webflow.com/made-in-webflow/website/relume-library-styleguide) — a great resource for exploring button and section variants managed in a central system (and much more!

  [Learn more about style Variants](https://help.webflow.com/hc/en-us/articles/33961303934611-Components-overview#01JD1X768QTS0DH4WG2TJQ78WF) →

- [ ] **Name components and groups clearly**

  Clear, consistent naming makes it easier for teammates to find and use components — especially at scale. A good name clearly communicates the component’s primary purpose. This not only supports collaboration, but also helps your libraries stay organized and searchable over time.

  For instance, you could use names like “Sections,” “Cards,” or “Utilities.”

  **Pro tips:**

  - Use a simple, clear, and recognizable name that describes the component group’s purpose on your sites.
  - Avoid abbreviations that new team members won’t understand.
  - Document your naming conventions in your style guide.

  **Optional starter resource:**

  [Client-First Cloneable](https://webflow.com/made-in-webflow/website/client-first-cloneable) — showcases a consistent naming system that supports collaboration and scale.

  [Learn more about grouping components](https://help.webflow.com/hc/en-us/articles/33961303934611-Components-overview#01JD1X76A2ZE4Q0P17P5R31J6Y) →

- [ ] **Create templates for repeatable page types**

  Use static page templates to speed up design work and maintain consistency when building unique but common marketing pages — like landing pages, event registration pages, or promotional microsites. These templates offer a visual starting point your team can quickly duplicate and adapt, reducing the need to rebuild layouts from scratch.

  For example, a “Case Study” static page template might include a predefined hero, rich content section, and testimonial strip — all styled using your design system. Anyone on your team can duplicate and adjust the layout without needing to rewire spacing, styles, or components.

  If you're working with repeatable content types like blog posts, product listings, or team profiles, consider using CMS [Collection pages](https://help.webflow.com/hc/en-us/articles/33961277976467-Structure-and-style-Collection-pages) instead. These allow you to design a single template and automatically apply that layout to every item in the Collection.

  **Pro tips:**

  - Add guidance text or placeholder content directly inside templates to make them easier to use.
  - Base templates on the components already in your design system for full consistency.
  - Reuse layout patterns across templates to make your system feel familiar from page to page.
  - Set up CMS bindings if your template will power dynamic content.

  **Optional starter resource:**

  [The style guide template](https://webflow.com/made-in-webflow/website/the-style-guide-template) — includes page layout templates with flexible structure and helpful guidance baked in.

  [Learn more about static page templates](https://help.webflow.com/hc/en-us/articles/33961218842387-Create-static-page-templates) →

## 3. Use interactions thoughtfully

- [ ] **Elevate the experience with interactions**

  Interactions can bring your design system to life — not just visually, but in how users experience your site. Add subtle animations like hover effects, click states, or scroll-triggered reveals to create feedback and flow. These details not only add a polished look and strengthen your brand identity. They also help guide users as they navigate through your site and move between different contexts. Start small and purposeful to ensure motion adds clarity, not distraction.

  For instance, a card that fades in as you scroll helps guide attention, while a button with a hover animation gives a reassuring cue that it's clickable.

  **Pro tips:**

  - Use scroll-in animations to create visual rhythm as users move down the page.
  - Apply hover states to buttons, links, and interactive cards to reinforce expected behavior.
  - Keep durations short (under 300ms) to improve site performance and present a fast and snappy interface to your visitors.
  - Follow Webflow’s Accessibility checklist [Animation guidance](https://webflow.com/accessibility/checklist#:~:text=Clear%20checked-,Animation,-Content%20that%20moves) to avoid excessive motion or flashing and include motion warnings where appropriate.

  **Optional starter resource:**

  [Create Award-Winning Animation and Interaction Design in Webflow](https://webflow.com/made-in-webflow/website/Create-Award-Winning-Animation-And-Interaction-Design-In-Webflow) — offers thoughtful motion design with usability in mind.

  [Learn more about interactions in Webflow](https://webflow.com/interactions-animations) →

- [ ] **Keep motion consistent**

  A shared motion system ensures your site feels polished and cohesive. Define standard durations, easing curves, and types of effects — and stick with them across interactions and components. This consistency builds user trust and reduces cognitive load.

  For instance, you could use a standard ease-out for all hover states and fade-ins, and apply the same delay patterns across sections.

  **Pro tips:**

  - Document your motion system alongside your visual styles.
  - Reuse animations via components or interactions presets.
  - Consider the balance between site performance and user delight when using motion.
  - Follow [W3’s WCAG guidance](https://www.w3.org/WAI/standards-guidelines/wcag/) for accessible animations.

  [Learn more about creating interactions](https://help.webflow.com/hc/en-us/articles/33961310025107-Intro-to-Interactions) →

## 4. Share & scale across sites

- [ ] **Create a shared library**

  Shared Libraries let you reuse components, variables, and assets across multiple Webflow sites in the same Workspace. This ensures that updates and improvements to your design system flow across projects — reducing duplication and creating a single source of truth. Libraries can be managed from a single dashboard and be installed wherever they’re needed.

  For instance, a shared Library called “Brand Design System” could include your team’s variables, components, and assets, and be ready for use in all your new microsites.

  **Pro tips:**

  - While Libraries can be managed from your Workspace Dashboard, consider creating a style guide on its own site to serve as the source of your Library.
  - Include a short welcome page or document to help new users get started.
  - Use consistent naming across libraries and projects to simplify syncing — especially when working with multiple libraries.

  [Learn more about shared Libraries](https://help.webflow.com/hc/en-us/articles/33961343551763-Libraries) →

- [ ] **Install and update your Library on other sites**

  Once your shared Library is built, you can install it on any other site in your Webflow Workspace, giving your team instant access to the same variables, components, and brand assets. And when you update a shared Library item, you can push the changes to every site where the library is installed. This helps you roll out brand refreshes, spacing adjustments, or bug fixes without manually updating each project.

  For instance, a team working on a new landing page installs a shared Library and immediately gains access to brand colors, typography, logos, and approved navigation and footer components.

  **Pro tips:**

  - Install your Library as a first step in designing a new site, to bring a consistent experience to market quickly.
  - Regularly review installed libraries across projects to ensure brand consistency.
  - Use Webflow’s built-in update [Design approvals](https://help.webflow.com/hc/en-us/articles/33961229501971-Design-approvals) process to review and approve changes before applying.
  - Communicate major changes with your team before publishing library updates.
  - Keep a change log in your style guide documentation to track what’s changed and when.

  [Learn more about installing shared Libraries](https://help.webflow.com/hc/en-us/articles/33961343551763-Libraries#h_01JRZBAW068P08WMDM189PJ7E8) →

- [ ] **Create a shared template from your site**

  If you want to reuse the entire structure of your site — including your library, page layout, CMS setup, and documentation — consider turning it into a site template. This gives you or your team a consistent starting point for future builds. It’s especially useful for agency teams, internal product teams, or distributed collaborators.

  For instance, a “Starter Site” template might include your design system, key layouts, component structure, and built-in documentation — all ready to duplicate.

  **Pro tips:**

  - Create a visual homepage that explains the purpose of the template and how to get started.
  - Include CMS collections with dummy content so teammates can see how everything works.
  - Add clear callouts or notes in the template to highlight editable or required sections.
  - Use folders and symbols to make the site structure easy to explore.

  **Optional starter resources:**

  - [Flux Starter Project + Style Guide](https://webflow.com/made-in-webflow/website/flux-starter-project-style-guide) — a polished, flexible starting point with built-in design system components.
  - [NSIDE CMS Template](https://webflow.com/made-in-webflow/website/NSIDE-or-Cloneable-CMS-Template) — demonstrates how to structure a reusable CMS-driven design system.

  [Learn more about shared Workspace templates](https://help.webflow.com/hc/en-us/articles/33961390607507-Save-your-site-as-a-shared-Workspace-template) →

## 5. Document & maintain

- [ ] **Document how your system works**

  Good documentation helps your team use the design system the right way — and keeps everyone aligned as the system evolves. It also makes onboarding easier by giving new team members a clear guide to follow. Include details like naming conventions, component usage, layout rules, and accessibility considerations. The more guidance you provide up front, the less confusion and inconsistency you’ll need to clean up later.

  For instance, a “Start Here” page could include your naming system, rules for when to use each layout type, and short walkthroughs for setting up common components. You might also link to your shared Library or embed demo videos to make things even more accessible.

  **Pro tips:**

  - Include real examples and screenshots to make documentation easier to follow.
  - Use headings and simple structure so teammates can skim or search quickly.
  - Create a versioning system or changelog to keep track of updates.
  - Host your guide where it's easy to find — like a webpage, site, or knowledge management tool.

  [Learn more about documenting your design system](https://webflow.com/blog/enterprise-design-systems#document-your-design-system) →

- [ ] **Define who can update the system**

  Design systems work best when they’re actively maintained — but not by everyone. Assign roles or permissions so that only certain people can update the source library, components, or style rules. This protects the integrity of the system and ensures updates go through review or collaboration when needed.

  For instance, you might limit editing rights to your lead designer and developer, while letting others use and install components freely.

  **Pro tips:**

  - Use [Webflow roles and permissions](https://help.webflow.com/hc/en-us/articles/33961273067411-Roles-and-permissions-overview) to control who can modify Libraries, components, and other parts of your system.
  - Set up a lightweight approval process for proposed updates.
  - Keep an open channel (like Slack or Notion) for teammates to suggest ideas or report issues.
  - Make a habit of reviewing update requests at regular intervals.

  [Learn more about design system governance](https://webflow.com/blog/enterprise-design-systems#governance-at-scale) →

- [ ] **Audit and update regularly**

  Design systems are living tools — they evolve as your brand, team, and content needs grow. Schedule regular reviews to identify outdated styles, clean up unused components, and align your system with current standards. Ongoing maintenance prevents clutter and makes sure your system continues to support high-quality work.

  For instance, during a quarterly audit, you might remove outdated style selectors, streamline spacing variables, and update documentation to reflect new naming rules.

  **Pro tips:**

  - Keep a “Deprecated” folder or to store items you’re phasing out (instead of deleting them right away).
  - Use analytics or feedback from your team to spot pain points or unused patterns.
  - Align reviews with key company milestones like product launches or rebrands.
  - Pair audits with a cleanup sprint so changes happen quickly.

  [Learn more about managing design system changes](https://webflow.com/blog/enterprise-design-systems#change-management) →
