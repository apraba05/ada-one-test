---
title: Content ingestion
source_url: https://docs.ada.cx/docs/knowledge/content-ingestion
slug: knowledge--content-ingestion
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://docs.ada.cx/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.ada.cx/_mcp/server.

# Content ingestion

## Overview

Knowledge allows your AI Agent to tap into multiple sources of information about your business. This helps the AI respond accurately to end user queries. You can configure Ada to read from various sources like Zendesk or Salesforce knowledge bases, or a website, or author articles directly within the Ada dashboard.

## Limitations

* **Content size**: Supports up to 50,000 articles across all knowledge sources by default. Higher limits are available for eligible plans — contact your Ada team.
* **Formatting restrictions**: Some complex HTML elements like nested tables are not supported.

## Use cases

The following scenarios illustrate how you can leverage knowledge sources in Ada:

* **Import Frequently Asked Questions (FAQs)**

  Allow the AI Agent to utilize pre-existing FAQ content to answer common end user queries during conversations.

* **Import a public knowledge base**

  Connect a public knowledge base (e.g., Zendesk or Salesforce) so that the AI agent can provide up-to-date information that you maintain in your original knowledge base.

* **Import scripts and conversation guides**

  Import scripts and conversation guides that were originally intended for human agents to use in live chat or phone support. By enabling the AI Agent to leverage these scripts, you maintain a consistent messaging strategy while also providing end users with reliable information without human intervention.

* **Import industry-specific knowledge**

  Incorporate industry-specific knowledge, for example a FinTech company might import tax regulations documentation enabling the AI Agent to assist end users with queries about financial regulations.

## Capabilities & configuration

Ada’s AI Agent supports various content formats, languages, and import methods.

**Capabilities**

* **Supported content types and formats**:
  * Allows rich text formatting such as bold, italics, and lists, enabling well-structured responses.
  * Supports media elements like images and tables, making responses more comprehensive.
  * Provides hyperlink support to guide users to external resources directly.
* **Multi-language support**:
  * Import knowledge in multiple languages, allowing the AI Agent to deliver localized information based on user language preferences. See the [language support documentation](/generative/docs/setup/languages) for a complete list.

**Import methods**

* **Connect a knowledge base**: Connect a knowledge base to automatically sync and update articles.
* **Website import**: Import publicly available content directly from specified URLs. Ada runs daily syncs to automatically detect and update changes.
* **Direct authoring**: Create and edit knowledge articles manually within Ada's dashboard.
* **Knowledge API**: Use the [Knowledge API](/generative/reference/knowledge/overview) to import knowledge from any sources.

## Quick start

**To add Knowledge to your AI Agent:**

On the Ada dashboard, go to **Config > AI AGENT > Knowledge**. Then, at the top of the page, click one of the following buttons:

* **Add source**, then select the applicable knowledge base. See [Connect your knowledge base](/generative/docs/knowledge/content-ingestion/knowledge-integration) for complete instructions.
* **Add Source** and select **Website**, then provide the website details. See [Import website content](/generative/docs/knowledge/content-ingestion/web-import) for complete instructions.
* **New Article**, then add your article contents. See [Create knowledge articles in Ada](/generative/docs/knowledge/content-ingestion/article-creation) for complete instructions.

After new or updated content is ingested, it may take a few minutes before it appears consistently in generative answers. See [Indexing latency & freshness](/generative/reference/knowledge/overview#indexing-latency-freshness) for more details.

## Best practices

* Tag articles clearly to help Ada retrieve relevant information more effectively.
* Limit article size for faster responses and more accurate searches.

## Related features

* [Webhook integrations](/generative/reference/introduction/webhooks): Trigger automatic actions based on AI responses by combining webhooks with Knowledge.

<hr />

<p>
  Have any questions? Contact your Ada team, or email us at 

  <a href="mailto:help@ada.cx?subject=Help%20Docs%20inquiry" class="email">{"help@ada.cx"}</a>

  .
</p>