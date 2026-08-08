---
title: Web import
source_url: https://docs.ada.cx/docs/knowledge/content-ingestion/web-import
slug: knowledge--content-ingestion--web-import
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://docs.ada.cx/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.ada.cx/_mcp/server.

# Web import

## Overview

Web import lets you add website content to your AI Agent's Knowledge base when that content doesn't live in a connected knowledge base integration. The scraper goes through your public-facing website content and saves the text as new articles on your **Knowledge** page.

## Limitations

Web import has the following constraints:

* You can only scrape content on public-facing websites (i.e., you can't require users to log in to see it).
* The website scraper imports articles up to 100KB in size. Articles larger than this limit will be truncated.
* The scraper follows links from your starting URL up to five levels deep (e.g., `www.website.com/level_1/level_2/level_3/level_4/level_5`). It won't import any articles that are deeper into your page hierarchy.
* Your AI Agent can have a maximum of 50,000 articles in it by default, and a web source can have up to 1,000 articles in it. If your AI Agent reaches either number, the import will stop. Higher article limits are available for eligible plans — contact your Ada team.
* It may not be possible to import certain types of websites. Web imports work best with websites that are written in static semantic HTML. Some websites may not import properly:
  * **Websites with web crawlers blocked** - if your website has a blocker for web crawlers, Ada's scraper won't be able to access its content.
  * **Websites that are not written with semantic HTML** - articles scraped from these websites may contain content from things like navigation menus, headers, footers, or other page elements that don't belong in your AI Agent's knowledge.
  * **Websites with complex redirection** - sites that rely on multiple or dynamic redirects (e.g., geo-based routing, authentication gates, or JavaScript-based redirects) may cause the scraper to retrieve unexpected, or incomplete content.
* URLs cannot exceed 1024 characters.
* Multi-language content is not supported – all scraped articles are currently set to English, regardless of the original page language.

## Use cases

Web import is useful when your content is not in a supported knowledge base integration.

* **Marketing and product pages**: Import public-facing website content such as product descriptions, feature pages, or pricing information.
* **Blog and news content**: Add blog posts, announcements, or news articles to your AI Agent's knowledge.
* **Support content outside your help center**: Import FAQ pages, troubleshooting guides, or documentation that lives on your main website rather than a dedicated knowledge base.
* **Supplementary information**: Add content from partner sites, landing pages, or other sources that your AI Agent should reference.

## Capabilities & configuration

Web import can scrape static semantic HTML websites and convert the content into Knowledge articles.

### Ignored HTML elements

Your website likely contains page elements you don't want to have scraped and saved in your AI Agent (e.g., headers and footers). By default, the scraper is programmed to skip the elements that are least likely to contain relevant page information.

The website scraper is programmed to ignore HTML elements that match the following tags:

<ul class="no-spacing">
  <li>
    `button`
  </li>

  <li>
    `iframe`
  </li>

  <li>
    `img`
  </li>

  <li>
    `meta`
  </li>

  <li>
    `nav`
  </li>

  <li>
    `noscript`
  </li>

  <li>
    `picture`
  </li>

  <li>
    `script`
  </li>

  <li>
    `style`
  </li>

  <li>
    `svg`
  </li>

  <li>
    `audio`
  </li>

  <li>
    `video`
  </li>
</ul>

### User agent

When importing website content, Ada's scraper identifies itself with a static `User-Agent` header:

```
AdaWebCrawler
```

If your website restricts crawlers with an allowlist (or you operate a site whose content Ada is importing), allowlist the `AdaWebCrawler` user agent to ensure Ada can continue to access your content.

## Quick start

Import website content to your AI Agent's Knowledge base in a few steps.

**To import a website:**

On the Ada dashboard, go to **Config > AI AGENT > Knowledge**, then click **Import website**.

Enter a **Source name** and select **Every webpage starting from one URL**.

Enter your website's root URL (e.g., `https://mywebsite.com`).

Click **Import**.

For more options, see [Import a website](#import-a-website).

## Implementation & usage

Import, update, and remove website content to control what information your AI Agent uses.

### Import a website

Import your website content to make it available as Knowledge for your AI Agent.

**To import your website's content:**

1. On the Ada dashboard, go to **Config > AI AGENT > Knowledge**, then click **Import website**.

   The **Import website** window opens.
2. Under **Source name**, give your source a name. Each source name in your AI Agent must be unique, so you can identify and filter by the source on your **Knowledge** page.
3. Under **Content to import**, choose the pages you want to import.
   * To import your entire website, where you provide a single URL and your AI Agent follows the links on that website and scrapes those pages too, select **Every webpage starting from one URL**. Then, add the URL you want your AI Agent to start scraping from.

     * For best results, use a root domain, like `https://mywebsite.com`, instead of a section of your website, like `https://mywebsite.com/pages`.
     * Be aware of any redirects in your website. The scraper will import redirected sites, as long as they start with the URL you enter.

   * To import specific pages on your website, where your AI Agent only scrapes the pages you provide, select **A specific list of webpages**. Then, add the list of URLs you want your AI to import, separating the URLs with commas. Your list can be up to 5000 characters long.
4. Under **Sync frequency**, select how often Ada automatically re-syncs this source:
   * **Weekly** (default) — Ada re-syncs the source once per week.
   * **Daily** — Ada re-syncs the source once per day.
   * **Never** — Ada does not automatically re-sync this source.
5. Click **Import**.

   The **Import website** window closes, and your AI Agent saves your page source on the **External sources** tab and starts importing its content.

   Large websites can take up to **24 hours** to finish importing. Feel free to leave the webpage while this is happening, as your AI Agent will email you when your import has finished.

By default, all of your imported articles are set to **Active**, but you can change availability settings as needed for any of your articles. For more information, see [Manage your knowledge content](/generative/docs/knowledge/article-management).

### Re-import a website\[#reimport]

Keep your Knowledge current by re-importing website content after updates.

**Automatic syncs**: Ada automatically re-syncs each source based on its sync frequency — **Daily**, **Weekly** (default), or **Never**. You set the frequency when adding a source.

**Manual refresh**: You can trigger an immediate re-import at any time from the Sources tab without waiting for the next scheduled sync.

Article updates preserve existing references in your coaching and rules, ensuring your automations continue to work seamlessly.

**To re-import your website's content:**

1. On the Ada dashboard, go to **Config > AI AGENT > Knowledge**, then open the **Sources** tab.
2. Find the website you want to re-import, and click **Settings**.

   The **Import website** window opens, with the import settings pre-populated.
3. Click **Import again**.

   The **Import website** window closes and starts re-importing your website. Refresh your page to see updates on your import's progress. Large imports may take a while to fully import.

### Delete a website source\[#delete]

Remove a website source when you no longer need its content in your AI Agent.

Removing a website as a source also deletes all of the articles from that website from your AI Agent.

**To delete a website source:**

1. On the Ada dashboard, go to **Config > AI AGENT > Knowledge**, then open the **Sources** tab.
2. Find the website you want to delete, and click **Settings**.

   The **Import website** window opens, with the import settings pre-populated.
3. Click **Delete source**.

   A confirmation message appears, to remind you that deleting the source also deletes all of the articles from your AI Agent. To proceed, click **Delete**.

## Related features

Expand your AI Agent's Knowledge with these related capabilities:

* **[Knowledge integrations](/generative/docs/knowledge/content-ingestion/knowledge-integration)**: Connect external knowledge bases like Zendesk, Salesforce, or Contentful.
* **[Article management](/generative/docs/knowledge/article-management)**: Create and manage Knowledge articles directly in Ada.

<hr />

<p>
  Have any questions? Contact your Ada team, or email us at 

  <a href="mailto:help@ada.cx?subject=Help%20Docs%20inquiry" class="email">{"help@ada.cx"}</a>

  .
</p>