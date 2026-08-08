---
title: Agent logic
source_url: https://docs.ada.cx/docs/welcome/agent-logic
slug: welcome--agent-logic
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://docs.ada.cx/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.ada.cx/_mcp/server.

# Agent logic

When you've used traditional automated support in the past, you've probably found it slow or difficult to use. Most legacy solutions aren't great at understanding what your customers want, or knowing how to respond or take actions like a human agent would.

By combining the information in your knowledge base with advanced AI, you don't just have a chatbot with Ada - you have a generative **AI Agent**, designed to perform tasks that human agents have previously only been able to do.

This topic will take you through Ada's technology that we use to make the customer experience with an AI Agent different from any chatbot you've used before.

## LLMs and generative AI\[#llms-ai]

The secret behind how your AI Agent both understands and writes messages is in the AI, or artificial intelligence, that Ada uses behind the scenes. Broadly, AI is a range of complex computer programs designed to solve problems like humans. It can address a variety of situations and incorporate a variety of types of data; in your AI Agent's case, it focuses on analyzing language to connect customers with answers.

When a customer interacts with your AI Agent, your AI Agent uses **Large Language Models**, or LLMs, which are computer programs trained on large amounts of text, to identify what the customer is asking for. Based on the patterns the LLM identified in the text data, an LLM can analyze a question from a customer and determine the intent behind it. Then, it can analyze information from your knowledge base and determine whether the meaning behind it matches what the customer is looking for.

**Generative AI** is a type of LLM that uses its analysis of existing content to create new content: it builds sentences word by word, based on which words are most likely to follow the ones it has already chosen. Using generative AI, your AI Agent constructs responses based on pieces of your knowledge base that contain the information the customer is looking for, and phrases them in a natural-sounding and conversational way.

### Content filters\[#content-filters]

LLM training data can contain harmful or undesirable content, and generative AI can sometimes generate details that aren't true, which are called hallucinations. To combat these issues, your AI Agent uses an additional set of models to ensure the quality of its responses.

Before sending any generated response to your customer, your AI Agent checks to make sure the response is:

* **Safe**: The response doesn't contain any harmful content.
* **Relevant**: The response actually answers the customer's question.
  Even if the information in the response is correct, it has to be the information the customer was looking for in order to give the customer a positive experience.
* **Accurate**: The response matches the content in your knowledge base, so your AI Agent can double-check that its response is true.

With these checks in place, you can feel confident that your AI Agent has not only made sound decisions in how to help your customer, but has also sent them high-quality responses.

## Reasoning Engine\[#reasoning-engine]

Your AI Agent runs on Ada's Reasoning Engine — a sophisticated system that determines how to best help each customer, powered by a combination of knowledge, automation, and continuous improvement.

When customers ask your AI Agent a question, the Reasoning Engine takes into account the following:

* **Conversation context**: Does the conversation before the current question contain context that would help your AI Agent better answer the question?
* **Knowledge base**: Does the knowledge base contain the information the customer is looking for?
* **Business systems**: Are there any Actions configured with your AI Agent designed to let it fetch the information the customer is looking for?
* **Playbooks**: Are there any automated workflows (Playbooks) that can resolve the customer's inquiry or trigger a next step automatically?

From there, the Reasoning Engine decides how to respond to the customer:

* **Follow-up question**: If the AI Agent needs more information, it can ask clarifying questions before proceeding.
* **Knowledge base**: If the answer exists in your knowledge base, it can use that information to generate a response. For more information, see [Understand how your AI Agent generates content from your knowledge base](/generative/docs/knowledge/core-workflows/content-generation).
* **Business systems**: If data is available through an integrated system, the AI Agent can use an [Action](/generative/docs/automation/actions/action-control) to fetch that information by making an API call.
* **Playbooks**: If an automated flow applies, the Agent can initiate the appropriate [Playbook](./../automation/playbooks/playbook-management.mdx) to perform a predefined series of steps.
* **Handoff**: If none of these options resolve the inquiry, the AI Agent can hand the conversation off to a human agent for further assistance.

To help your AI Agent improve over time, Ada's [Coaching tools](/generative/docs/optimization/coaching/coaching-tools) provide feedback and insights into how these reasoning decisions are made. Coaching helps identify opportunities to optimize your AI Agent's performance — ensuring it continues to deliver accurate, helpful, and consistent responses.

Together, these elements form Ada's **Reasoning Engine**, the mechanism that enables your AI Agent to think, act, and learn. Just like a human agent relies on training, tools, and experience to decide how to help a customer, the Reasoning Engine considers multiple inputs to resolve inquiries as effectively as possible.

## Prompt injection prevention\[#prevent-prompt-injections]

Many AI chatbots are vulnerable to prompt injections or jailbreaking, which are prompts that get the chatbot to provide information that it shouldn't - for example, information that is confidential or unsafe.

The Reasoning Engine behind Ada's AI Agents is structured in such a way as to make adversarial LLM attacks very difficult to succeed. Specifically, it has:

* A series of AI subsystems interacting together, each of which modifies the context surrounding a customer's message
* Several prompt instructions that make the task to be performed very clear, directing the AI Agent to not share inner workings and instructions, and to redirect conversations away from casual chitchat
* Models that aim to detect and filter out harmful content in inputs or outputs
* State of the art generative AI testing prior to new deployments

<hr />

<p>
  Have any questions? Contact your Ada team, or email us at 

  <a href="mailto:help@ada.cx?subject=Help%20Docs%20inquiry" class="email">{"help@ada.cx"}</a>

  .
</p>