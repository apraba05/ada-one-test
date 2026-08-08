---
title: Key concepts
source_url: https://docs.ada.cx/docs/welcome/key-concepts
slug: welcome--key-concepts
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://docs.ada.cx/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.ada.cx/_mcp/server.

# Key concepts

Ada is built on a set of foundational concepts and features that work together to power your AI agent. This topic outlines the key components that empower Agent Managers to create, manage, and enhance customer experiences.

## Knowledge

The AI Agent in Ada uses ingested **knowledge** to answer customer questions accurately. It compiles information from multiple sources, including existing knowledge bases (such as Zendesk or Salesforce), relevant websites, articles created within Ada, and custom sources imported using Ada’s Knowledge API.

Once connected to these sources, the AI Agent ingests content and makes it searchable. In the Ada dashboard, you can manage these sources by reviewing, enabling, or disabling specific articles. For details, see [this section](/generative/docs/knowledge).

## Automation

Automation allows the AI Agent to complete tasks independently by connecting to external systems and following defined steps. This reduces the need for manual effort.

### Actions

The AI Agent enhances its capabilities by interacting with external systems through API calls. These automated processes, called **Actions**, allow it to retrieve or process information, enabling tasks such as checking order statuses, updating accounts, or verifying user details. The AI Agent automatically determines when to use an Action and how to process the response.

To ensure security, some Actions require authentication through an API token, which Ada stores securely. This token can either be a shared static value or dynamically generated during customer login. For sensitive tasks like accessing private information or making purchases, users must sign in, generating a login token that authenticates their interactions throughout the session. Once securely stored, these tokens allow secure integration with external systems. For details, see [this section](/generative/docs/automation/actions).

### Processes

Structured workflows enable automation for multi-step customer inquiries, ensuring tasks are completed in the right order. Known as **Processes**, these workflows define how the AI Agent gathers information, applies logic, and executes actions to resolve specific requests. Some inquiries require precise wording, while others involve pulling data from multiple business systems before making a decision.

Each Process consists of specific operations that determine the AI Agent’s path in handling an inquiry. For example, when processing a refund, the AI Agent can first verify the return policy, confirm item eligibility, and then trigger an Action to complete the refund.

[Actions](#actions) and Processes work together: while an Action handles a single API request, a Process links multiple Actions into a structured workflow. This allows for more complex tasks, such as verifying customer identity before retrieving account details or completing multiple API calls in sequence. For details, see [this section](/generative/docs/automation/actions).

### Playbooks

Playbooks provide step-by-step guidance for handling complex customer interactions, ensuring that conversations follow a clear and consistent structure. Similar to standard operating procedures (SOPs) used by human agents, Playbooks define how the AI Agent communicates with customers, asks questions, and responds based on user input or system state. Some scenarios require gathering specific details from the customer, while others involve branching logic or coordinating with other systems through [Actions](#actions) and [Handoffs](#handoffs).

Each Playbook consists of structured instructions that guide the AI Agent through a specific conversational flow. For example, when troubleshooting a service issue, the Playbook can direct the Agent to collect relevant context, run diagnostic Actions, and escalate to a human agent if needed.

Playbooks work in concert with Actions and Variables: while an Action performs a single system task, a Playbook organizes these tasks into a customer-facing script. This allows the AI Agent to manage multi-step conversations—such as verifying identity, checking service eligibility, and updating account settings—all in a coherent and user-friendly way. For details, see [this section](/generative/docs/automation/playbooks).

### Proactives

**Proactives** are proactive messages that the AI Agent sends to customers before they ask based on their actions, such as visiting a webpage or logging in for the first time. For example, an AI Agent can ask if a customer needs help checking an order status, notify users of a system outage, or introduce new customers to available services. Businesses can also customize Proactive Conversations using message templates for a more personalized experience. For details, see [this section](/generative/docs/automation/proactives).

### Greetings

The way an AI Agent greets users sets the tone for the conversation. Businesses can customize **greetings** by adjusting content, pacing, and tone to create the right first impression. Using modular input elements, greetings can be tailored to meet specific needs. Variables can also personalize interactions by adding customer-specific details, such as names or account information.  For details, see [this section](/generative/docs/automation/greetings).

### Custom Instructions

**Custom Instructions** define how the AI Agent responds in *every* conversation, ensuring interactions follow specific guidelines. They take effect immediately once published and help improve the AI Agent’s accuracy and consistency. To guide specific use cases, you can use [Coaching](#coaching).

If needed, businesses can apply restrictions based on user data, ensuring certain instructions only apply to specific customers. The Ada dashboard provides insights by showing which Custom Instructions were active during conversations, allowing businesses to fine-tune the AI Agent's responses. For details, see [this section](/generative/docs/automation/custom-instructions).

## Setup

Setup lets you define how the AI Agent communicates with users and handles sensitive information, helping it communicate in a way that fits your brand.

### Persona

The **persona** sets how the AI Agent interacts with users, including its tone, style, and behavior. It ensures responses align with the company’s brand and values. Businesses can customize how the AI Agent refers to the company and ensure its communication matches the applicable brand values. For details, see [this section](/generative/docs/setup/persona).

### Languages

**Languages** determine how the AI Agent communicates with customers. It can understand questions in any supported language but will only respond in the languages enabled in its settings. English is the default language for all AI Agents and cannot be disabled. However, businesses can enable additional languages based on their needs. By default, the AI Agent starts conversations in English, but this can be customized to suit different audiences. For details, see [this section](/generative/docs/setup/languages).

### Redactions

Redactions allow AI Agents to remove customers’ personally identifiable information from conversations. You can define and test a regular expression to identify and redact specific data or remove values received from an Action’s output, such as customer names. For details, see [this section](/generative/docs/setup/redactions).

## Handoffs

If the AI Agent encounters a request it cannot handle, it escalates the conversation to a human agent. This process, called a **handoff**, ensures customers get the right assistance without disruption.

The AI Agent determines when to transfer a conversation based on predefined rules and triggers. It can route customers to the appropriate support team. Businesses can customize these handoffs by setting up specific transfer conditions, such as prioritizing specific customers or routing issues to the applicable departments. For details, see [this section](/generative/docs/handoffs).

### Handoff integrations

**Handoff integrations** enable customers to transition from AI-driven support to integrated support systems like Zendesk or Salesforce. Live chat integrations allow customers to start with an AI Agent and connect with a human agent when needed while ticketing integrations submit support requests directly to a help desk. Some handoff integrations also automate tasks such as case creation and lead management. For details, see [this section](/generative/docs/handoffs/handoff-management/handoff-integrations).

## Channels

**Channels** define how customers communicate with the AI Agent across different platforms such as websites, mobile apps, email systems, phone support, and social channels. By offering multiple channels, businesses ensure customers receive fast, consistent, and personalized support wherever they prefer to connect. For details, see [this section](/generative/docs/channels).

### Chat

Web **chat** enables businesses to embed the AI Agent into their website or mobile app, allowing customers to interact with automated support in real time. Setup is simple—connect a knowledge base, add a chat widget with a code snippet, and customize its appearance and behavior to align with the brand.

Businesses can control how the AI Agent interacts with users, manage its visibility for testing or phased rollout, and adjust its functionality based on platform-specific needs. Security and privacy are built-in, with domain authorization preventing unauthorized access and configurable settings for data retention and customer privacy. For details, see [this section](/generative/docs/channels/chat).

### Voice

The **voice** channel enables the AI Agent to handle customer support calls by integrating with contact center platforms like Twilio, Amazon Connect, and Aircall. It uses speech recognition and customizable voices to accurately interpret and respond to customer inquiries in multiple languages.

Businesses can fine-tune voice settings, optimize call handling, and improve recognition of industry-specific terms for better accuracy. The AI Agent can guide callers through structured workflows, process inputs via speech or SMS, and connect with APIs to retrieve information. Features like Smart Capture and customizable prompts enhance understanding, while call routing enables handoffs to human agents. For details, see [this section](/generative/docs/channels/voice).

### Email

The **email** channel enables customers to interact with the AI Agent by sending messages to a designated support email. The AI Agent processes these inquiries, provides detailed responses, and forwards unresolved cases to human agents for further support.

Businesses can integrate the email channel using direct email forwarding or Ada’s Email APIs. Customization options allow adjustments to sender details, headers, footers, and branding. Additional features include attachment management, customer feedback surveys (CSAT), and Launch controls to balance AI and human-assisted responses. For details, see [this section](/generative/docs/channels/email).

### Social

Zendesk Messaging allows businesses to automate customer support across multiple **social** channels, including WhatsApp, Facebook Messenger, Instagram Direct, Twitter DM, and Twilio SMS. It uses Sunshine Conversations as the messaging infrastructure, enabling interactions through these popular platforms.

By customizing responses and using channel-specific variables, businesses can tailor conversations to fit each platform’s style. The AI Agent can manage media uploads and adjust its responses. For details, see [this section](/generative/docs/channels/social).

## Optimization

### Testing

**Interactive Testing** lets businesses experience their AI Agent’s responses as a customer would. Once the Agent is connected to a knowledge base, testing can begin to replicate real interactions. This feature allows you to simulate different user types by setting variables in the test chat, so you can verify that your Agent responds correctly in each scenario. Chats can be reset to test multiple interactions, following the configured persistence settings.

**Simulations** enable AI Managers to understand how configuration changes impact AI Agent behavior. By creating test cases with defined expected outcomes, businesses can run automated evaluations against the AI Agent and review pass/fail results. This approach helps identify regressions and ensure coverage across different end-user scenarios.

For details, see [this section](/generative/docs/optimization/testing).

### Conversations

A **Conversation** in Ada is any exchange between a customer and the AI Agent, capturing all messages, responses, and relevant customer details. These interactions are stored in a searchable library, organized by customer, with the most recent conversations at the top. Reviewing conversations helps businesses understand how the AI Agent interacts with customers, detect potential issues, and refine its responses. For details, see [this section](/generative/docs/optimization/conversations).

### Coaching

**Coaching** allows the AI Agent to refine its responses and improve decision-making based on feedback. By learning from past interactions, recognizing patterns, and adjusting its approach, the AI Agent becomes more effective at handling similar situations in the future.

Unlike general guidance provided through [Custom Instructions](#custom-instructions), Coaching is always context-specific, focusing on unique scenarios. While Custom Instructions consist of rules that apply to all conversations, Coaching targets specific situations. For details, see [this section](/generative/docs/optimization/coaching).

### Intent Intelligence

**Intent Intelligence** organizes conversations into a two-level taxonomy. A **Topic** groups conversations by subject, and each Topic contains **Intents** that capture the specific reason an end user reached out. The AI Agent classifies conversations automatically, helping you understand trends, measure automation effectiveness, and find areas for improvement.

Topics and Intents are ranked by their potential to increase automated resolution, so you can focus on high-impact areas. Each provides insights such as conversation volume and customer satisfaction trends, and you can refine the taxonomy by editing Topics and Intents or approving AI-recommended Intents. For details, see [this section](/generative/docs/optimization/performance/intent-intelligence).

### Reports

**Reports** provides detailed data on how the AI Agent is performing, tracking key metrics such as resolution rates, customer satisfaction, and usage trends. Businesses can use filters to focus on specific time periods or insights.

Reports update approximately every hour, though some changes may take up to three hours to fully reflect. They follow the time zone set in the user’s profile and are best viewed in the dashboard. If needed, reports can be printed or saved as a PDF with adjusted margins and scale for better formatting.  For details, see [this section](/generative/docs/optimization/performance/reports).

### CSAT

**Customer Satisfaction (CSAT)** surveys measure how customers feel about their interaction with the AI Agent. These surveys provide real-time feedback, appearing when a customer closes a chat (after sending at least one message) or when a human agent leaves the conversation. By gathering feedback at these critical moments, businesses can analyze customer opinions and identify areas for improvement. For details, see [this section](/generative/docs/optimization/performance/csat-survey).

## API keys

**API keys** allow external systems to securely connect with Ada’s platform. They authenticate requests and provide read and write access to all available APIs. Organizations can generate multiple active keys, making it easier to rotate them for security. API keys do not expire unless manually revoked.

To use an API key, it must be included in the Authorization header of a request; otherwise, the request will fail. Businesses can create and manage API keys from the Ada Dashboard, deleting old keys when no longer needed. This ensures secure and controlled access to Ada's APIs. For details, see [Authentication](/generative/reference/introduction/authentication) in the [API Reference documentation](/generative/reference/introduction/overview).

## Webhooks

**Webhooks** allow Ada to send real-time event updates to external systems, enabling automation and seamless integration. They use secure HTTPS communication and automatically retry failed messages for up to a week. If a system doesn’t confirm receipt within 15 seconds, retries follow an exponential backoff schedule to prevent overload.

To receive webhooks, businesses must configure an endpoint in their system. During testing, all event types can be enabled, then refined for production to avoid unnecessary messages.  For details, see [Webhooks](/generative/reference/introduction/webhooks) in the [API Reference documentation](/generative/reference/introduction/overview).

## Team access

**Team access** settings allow AI Agent Managers to manage personal and team-related configurations within Ada. It provides options to update personal information, adjust login preferences, and set security measures such as two-factor authentication. Users can manage team access by adding or removing members and assigning permissions based on roles. Additionally, organizations can enable Single Sign-On (SSO) to streamline login access through their authentication system. For details, see [this section](/generative/docs/other/team-access).

<hr />

<p>
  Have any questions? Contact your Ada team, or email us at 

  <a href="mailto:help@ada.cx?subject=Help%20Docs%20inquiry" class="email">{"help@ada.cx"}</a>

  .
</p>