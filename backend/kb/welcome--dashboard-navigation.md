---
title: Dashboard navigation
source_url: https://docs.ada.cx/docs/welcome/dashboard-navigation
slug: welcome--dashboard-navigation
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://docs.ada.cx/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.ada.cx/_mcp/server.

# Dashboard navigation

This guide helps you find features in the Ada dashboard. Use it to locate tools by what you want to accomplish, or reference the full navigation structure below.

## Quick reference

Use this table to quickly find where to go based on what you want to do.

| I want to...                                                      | Go to                                                   |
| ----------------------------------------------------------------- | ------------------------------------------------------- |
| See my AI Agent's performance overview                            | **Home**                                                |
| View conversation Topics, Intents, and trends                     | **Analytics** > **Topics & Intents**                    |
| Review automated resolution or CSAT reports                       | **Analytics** > **Reports**                             |
| Explore custom metrics and data                                   | **Analytics** > **Explore**                             |
| Browse or search individual conversations                         | **Convos**                                              |
| Create or run test cases for my AI Agent                          | **Simulations**                                         |
| Add or edit knowledge articles                                    | **Config** > **Knowledge** > **Articles**               |
| Connect external content sources                                  | **Config** > **Knowledge** > **Sources**                |
| Teach the AI Agent preferred terms, translations, and definitions | **Config** > **Glossary**                               |
| Create guided conversation flows                                  | **Config** > **Playbooks**                              |
| Set up API integrations                                           | **Config** > **Actions**                                |
| Build multi-step workflows                                        | **Config** > **Processes**                              |
| Configure agent transfers                                         | **Config** > **Handoffs**                               |
| Set up handoff integrations (Zendesk, Salesforce)                 | **Config** > **Handoffs** > **Integrations**            |
| Configure off-hours behavior                                      | **Config** > **Handoffs** > **Off hours**               |
| Customize my AI Agent's personality                               | **Config** > **Settings** > **Preferences**             |
| Enable additional languages                                       | **Config** > **Settings** > **Languages**               |
| Configure data redaction rules                                    | **Config** > **Settings** > **Redactions** (Admin only) |
| Set up customer satisfaction surveys                              | **Config** > **CSAT**                                   |
| Configure web chat appearance                                     | **Config** > **Chat** > **Appearance**                  |
| Install the chat widget on my website                             | **Config** > **Chat** > **Installation**                |
| Control chat rollout and visibility                               | **Config** > **Chat** > **Launch**                      |
| Manage chat data and privacy settings                             | **Config** > **Chat** > **Data & privacy**              |
| Set up proactive messages                                         | **Config** > **Chat** > **Proactives**                  |
| Set up email channel                                              | **Config** > **Email**                                  |
| Configure voice channel                                           | **Config** > **Voice**                                  |
| Connect social messaging platforms                                | **Config** > **Social**                                 |
| Manage API keys                                                   | **Config** > **API keys**                               |
| Set up webhooks                                                   | **Config** > **Webhooks**                               |
| Manage team members and permissions                               | **Team** (or Profile menu > **Team**)                   |
| Test my AI Agent's responses                                      | **Config** sidebar > **Test AI Agent** button           |
| See product updates and release notes                             | Profile menu > **What's new**                           |
| Get help using the dashboard                                      | Profile menu > **Ask for help**                         |
| Access product documentation                                      | Profile menu > **Documentation**                        |
| Review the history of configuration changes                       | Profile menu > **Audit log**                            |
| Update my profile settings                                        | Profile menu > **Profile**                              |

## Primary navigation

The primary navigation appears on the left side of the dashboard.

### Home

The Home page provides an overview of your AI Agent's performance, including key metrics and recent activity. This is the default landing page when you sign in.

### Analytics

Analytics contains tools for monitoring and understanding your AI Agent's performance.

| Page                 | Description                                                                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Topics & Intents** | View how conversations are classified into Topics and Intents and identify trends. They are ranked by their potential to increase automated resolution. |
| **Reports**          | Access detailed performance reports including Automated Resolution rates, CSAT scores, and usage trends.                                                |
| **Explore**          | Build custom queries to explore your conversation data with flexible filters and groupings.                                                             |

### Convos

The Convos page displays a searchable library of all conversations between customers and your AI Agent. Conversations are organized by customer, with the most recent at the top. Use this page to review how your AI Agent handles interactions and identify opportunities for improvement.

### Testing

Testing enables you to validate your AI Agent's behavior before changes affect customers. Create test cases with expected outcomes, run automated evaluations, and review pass/fail results to catch regressions.

Testing is available to customers with Simulations enabled.

## Config (secondary navigation)

Selecting **Config** in the primary navigation opens a secondary sidebar with configuration options organized into three sections.

### AI Agent

These settings control how your AI Agent understands and responds to customers.

| Page          | Description                                                                                                                                                                                                        |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Knowledge** | Manage knowledge articles and content sources that power your AI Agent's responses. Has two tabs: **Articles** for individual content and **Sources** for external integrations (Zendesk, Salesforce, web import). |
| **Glossary**  | Teach the AI Agent your business's vocabulary — preferred terms, translations, and definitions.                                                                                                                    |
| **Playbooks** | Create step-by-step conversation flows for handling complex customer interactions.                                                                                                                                 |
| **Greeting**  | Customize how your AI Agent greets customers at the start of a conversation.                                                                                                                                       |
| **Actions**   | Configure API integrations that allow your AI Agent to retrieve or update information in external systems.                                                                                                         |
| **Processes** | Build structured multi-step workflows for handling complex requests.                                                                                                                                               |
| **Handoffs**  | Set up rules and integrations for transferring conversations to human agents. Has tabs for **Handoffs** (rules), **Integrations** (Zendesk, Salesforce), and **Off hours** (schedule-based behavior).              |
| **CSAT**      | Configure customer satisfaction surveys that appear after conversations.                                                                                                                                           |
| **Coaching**  | Review and provide feedback on AI Agent responses to improve future interactions.                                                                                                                                  |
| **Settings**  | Configure your AI Agent's persona, languages, variables, and custom instructions.                                                                                                                                  |

#### Settings sub-pages

The Settings section contains additional configuration pages:

| Page                    | Description                                                                     |
| ----------------------- | ------------------------------------------------------------------------------- |
| **Preferences**         | Set your AI Agent's name, personality, voice, and tone.                         |
| **Languages**           | Enable languages and configure multilingual behavior.                           |
| **Variables**           | Define variables to personalize conversations with customer-specific data.      |
| **Custom Instructions** | Create rules that apply to every conversation.                                  |
| **Redactions**          | Configure rules to remove sensitive data from conversations (Owner/Admin only). |

### Channels

These settings control how customers connect with your AI Agent across different platforms.

| Page       | Description                                                                                                                                                               |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Chat**   | Configure the web chat widget. Has tabs for **Appearance**, **Installation**, **Launch** (rollout controls), **Data & privacy**, and **Proactives** (automated messages). |
| **Email**  | Set up email channel integration and customize email formatting.                                                                                                          |
| **Social** | Connect social messaging platforms like WhatsApp, Facebook Messenger, and Instagram.                                                                                      |
| **Voice**  | Configure phone-based AI Agent interactions with contact center platforms.                                                                                                |

### Platform

These settings manage technical integrations and access.

| Page         | Description                                                            |
| ------------ | ---------------------------------------------------------------------- |
| **API keys** | Generate and manage API keys for external system integrations.         |
| **Apps**     | View and manage installed applications.                                |
| **Webhooks** | Configure endpoints to receive real-time event notifications from Ada. |

## Team

The Team page allows you to manage team members, permissions, and security settings.

| Page               | Description                                                        |
| ------------------ | ------------------------------------------------------------------ |
| **Team**           | Add or remove team members and assign roles.                       |
| **SSO**            | Configure Single Sign-On for your organization (Owner/Admin only). |
| **Session limits** | Set session timeout and security policies (Owner/Admin only).      |

## Profile menu

Click your avatar in the bottom-left corner of the sidebar to access the profile menu.

| Item              | Description                                                                   |
| ----------------- | ----------------------------------------------------------------------------- |
| **What's new**    | View recent product updates and release notes.                                |
| **Ask for help**  | Open the Ada assistant to get help using the dashboard.                       |
| **Documentation** | Open the Ada documentation site in a new tab.                                 |
| **Team**          | Go to team management (same as Team in primary navigation).                   |
| **Audit log**     | Review a chronological record of configuration changes made to your AI Agent. |
| **Profile**       | View and edit your personal profile settings.                                 |

## Test AI Agent

The **Test AI Agent** button opens a test conversation with your AI Agent. Use this to preview how your AI Agent responds to customers before publishing changes.

In the refreshed navigation, find this button in the **Config** sidebar. In the original navigation, it appears in the primary sidebar.

## What moved in the navigation refresh

If you're familiar with the previous navigation, use this table to find features in their new locations.

| Feature             | Previous location          | New location                                        |
| ------------------- | -------------------------- | --------------------------------------------------- |
| Knowledge           | Main navigation            | **Config** > **Knowledge**                          |
| Playbooks           | Main navigation            | **Config** > **Playbooks**                          |
| Actions             | Main navigation            | **Config** > **Actions**                            |
| Processes           | Main navigation            | **Config** > **Processes**                          |
| Handoffs            | Main navigation            | **Config** > **Handoffs**                           |
| Settings            | Top navigation             | **Config** > **Settings**                           |
| Persona             | Settings menu              | **Config** > **Settings** > **Preferences**         |
| Languages           | Settings menu              | **Config** > **Settings** > **Languages**           |
| Variables           | Settings menu              | **Config** > **Settings** > **Variables**           |
| Custom Instructions | Settings menu              | **Config** > **Settings** > **Custom Instructions** |
| Team                | Settings menu              | **Team** (primary navigation)                       |
| Conversations       | Insights section           | **Convos** (primary navigation)                     |
| Topics & Intents    | Insights section           | **Analytics** > **Topics & Intents**                |
| Reports             | Insights section           | **Analytics** > **Reports**                         |
| Proactives          | Main navigation (Training) | **Config** > **Chat** > **Proactives**              |
| Redactions          | Settings menu              | **Config** > **Settings** > **Redactions**          |

<hr />

<p>
  Have any questions? Contact your Ada team, or email us at 

  <a href="mailto:help@ada.cx?subject=Help%20Docs%20inquiry" class="email">{"help@ada.cx"}</a>

  .
</p>