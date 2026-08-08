---
title: Improvement tactics
source_url: https://docs.ada.cx/docs/welcome/improvement-tactics
slug: welcome--improvement-tactics
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://docs.ada.cx/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.ada.cx/_mcp/server.

# Improvement tactics

## What happens once your AI Agent is live?

Your focus shifts from building to improving. You've launched with a solid foundation, but now the goal is to make your Agent smarter, more reliable, and more impactful. Improvement is about small, targeted changes that add up to big gains—whether that's faster, more accurate answers, more relevant conversations, or smoother workflows.

### Just looking to take action?

Here's a quick checklist to help you start improving your AI Agent right away, without reading through all the details first. If you're comfortable jumping in without the full walkthrough, try this exercise in your own workspace:

| ✅ | **Step**                                                                                           | **Where to do it**                                                                                              |
| - | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| 1 | Open **Analytics → Topics & Intents** and sort by **AR Opportunity**                               | **Analytics → Topics & Intents**                                                                                |
| 2 | Pick one high-volume Topic or Intent with low **AR Rate** or **CSAT**                              | **Analytics → Topics & Intents**                                                                                |
| 3 | Review three low-CSAT conversations in that Topic or Intent                                        | **Analytics → Topics & Intents → See Conversations**                                                            |
| 4 | Identify what's missing: is it **Knowledge**, an **Action**, **Coaching**, or **Personalization**? | **Convos → Conversation**                                                                                       |
| 5 | Improve the response using one (or more):                                                          |                                                                                                                 |
|   | – Add or update a **Knowledge** article                                                            | **Config → AI AGENT → Knowledge**                                                                               |
|   | – Use **Coaching** to guide the Agent's behavior                                                   | **Convos → Conversation → Provide coaching**                                                                    |
|   | – Add an **Action** if external data is needed                                                     | **Config → AI AGENT → Actions / Processes / Playbooks**                                                         |
|   | – Add **Personalization** to tailor the response based on user context                             | [Various entry points](/generative/docs/optimization/personalization/personalization-data#implementation-usage) |
| 6 | Publish your changes and monitor the impact on **CSAT** or **AR**                                  |                                                                                                                 |

## Next steps at a glance

Once your AI Agent is live, your focus naturally shifts from building to improving. You've launched with a solid foundation—but now it's time to make it even smarter, more reliable, and more impactful. That's where continuous improvement comes in.

The goal is to identify where your Agent is underperforming and apply focused enhancements that help it do more—and do it better. It's not about starting over or rewriting everything. Instead, it's about finding specific areas to improve: better responses, more relevant content, access to live data, or a more personalized experience.

Here's how to identify gaps in your Agent's performance, understand what's going wrong, and choose the right tools to improve it:

| **Phase**             | **Feature**                             | **When to use it**                                                                                                                |
| --------------------- | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **[Identify](#spot)** | **[Topics & Intents](#topics)**         | High-volume conversations clustered around a single intent that rarely resolve automatically—indicated by a high AR Opportunity   |
|                       | **[CSAT](#csat)**                       | Declining CSAT—low satisfaction in *resolved* conversations, with feedback citing vague answers, long waits, or repeated handoffs |
| **[Fix](#fix)**       | **[Knowledge](#knowledge)**             | Generic replies caused by missing, outdated, or unclear content                                                                   |
|                       | **[Actions](#actions-playbooks)**       | Inability to complete tasks without external data (e.g., refund status)                                                           |
|                       | **[Coaching](#coaching)**               | Intent is right but reply is vague or too formal—needs quick tweak                                                                |
|                       | **[Personalization](#personalization)** | Conversation ignores plan tier, region, or user segment, reducing relevance                                                       |

## Identifying areas for improvement\[#spot]

Before you can improve anything, you need to know what's not working as well as it could. Ada gives you two key tools to help with this: [Topics](#topics) and [CSAT](#csat). Together, these tools provide a complete picture of both what's going wrong and how it feels to the customer.

**Prefer a conversational approach?** Connect Ada to an AI assistant like Claude or ChatGPT using the [MCP Server](/mcp/introduction/overview). Ask questions like "How can I improve my CSAT?" or "Analyze my unresolved conversations from last week" and get actionable recommendations without navigating dashboards.

### Topics and Intents: What end users are asking\[#topics]

[Intent Intelligence](/generative/docs/optimization/performance/intent-intelligence) groups conversations into Topics and Intents based on the reason an end user reached out. Each Topic and Intent surfaces key performance metrics that help you understand how well your AI Agent is handling a specific type of inquiry.

You can click on any Topic and drill down into the related conversations, making it easy to explore real examples where the Agent might be missing the mark. This helps you quickly spot patterns—like repeated [Handoffs](/generative/docs/handoffs), vague responses, or missing [Knowledge](#knowledge)—and uncover concrete opportunities for improvement.

#### Why these metrics matter

Focus on [Topics](/generative/docs/optimization/performance/intent-intelligence) that have high volume, low AR Rate, high AR Opportunity, and low [CSAT](#csat). These signals indicate that:

* The issue comes up often (high volume)
* The AI Agent is struggling to resolve it (low AR Rate)
* There's a large portion of conversations that could be automated with improvements (high AR Opportunity)
* Customers are having a negative experience, even when issues are technically *handled* (low CSAT)

In other words, these Topics represent high-friction, high-impact opportunities. Improving them can unlock quick wins—reducing [Handoffs](/generative/docs/handoffs), improving satisfaction, and scaling automation where it matters most.

**Want to see this in action?** Check out the [Refund requests](/generative/docs/optimization/performance/intent-intelligence/best-practices#topics-example-refund-requests) and [Card fulfillment](/generative/docs/optimization/performance/intent-intelligence/best-practices#topics-example-card-fulfillment) examples. They show how to use Topic metrics and conversation patterns to identify issues and take targeted action—like adding content, refining messaging, or introducing automation—to improve performance and reduce Handoffs.

### CSAT: How end users feel\[#csat]

[Customer Satisfaction (CSAT) surveys](/generative/docs/optimization/performance/csat-survey) help you understand how end users feel about their experience — not just whether the AI Agent resolved their issue. A [Conversation](/generative/docs/optimization/conversations) might be marked as resolved, but if the CSAT score is low, the answer may not have been clear, helpful, or empathetic enough.

**To get the most out of CSAT data**:

* Look at CSAT trends over time.
* Watch for negative CSAT scores even when the Agent provides an answer — this could signal confusion or poor tone.
* Check if certain [Topics](#topics) have dropping CSAT scores.
* See if [Handoffs](/generative/docs/handoffs) are frustrating users.

**Want to see this in action?** Explore the [Account cancellation](/generative/docs/optimization/performance/intent-intelligence/best-practices#csat-example-account-cancellation) and [Warranty replacement](/generative/docs/optimization/performance/intent-intelligence/best-practices#csat-example-warranty-replacement) examples. They show how to use CSAT and Topic insights to spot friction, analyze related Conversations, and take focused action—like clarifying responses, asking better questions, or reducing unnecessary Handoffs.

## Making the right improvements\[#fix]

Once you've identified a gap in your AI Agent's performance—whether that's from unresolved [Topics](#topics), low [CSAT](#csat), or customer feedback—the next step is choosing how to improve it. Ada gives you several tools, and each one is designed to solve a different kind of problem.

Here's a quick guide to choosing the right one:

* [Knowledge](#knowledge) improvements are useful when the Agent doesn't have the right content.
* [Actions](#actions-playbooks) connect your Agent to real-time data when static answers aren't enough.
* [Coaching](#coaching) helps when the Agent is almost getting it right but needs a better response.
* [Personalization](#personalization) helps you make the experience feel more relevant and human.

Each of these tools gives you a way to make your Agent better, smarter, and more helpful over time. The goal isn't to fix everything at once. Start with the clearest gaps, apply the right kind of improvement, and measure the results. With each small change, you move your Agent closer to handling more on its own—with better outcomes for your team and your end users.

Let's take a closer look at each one—what it does, why it matters, and how to apply it effectively.

### If your AI Agent doesn't have the right answer — Improve your Knowledge base\[#knowledge]

Your AI Agent relies on your [Knowledge](/generative/docs/knowledge) base — the articles and resources it uses to answer questions. If that content is missing details or doesn't cover common situations, the Agent might give poor answers or hand off too soon.

Use Knowledge improvements when:

* The Agent understands the question but still escalates.
* Responses are vague or unhelpful, even for known [Topics](#topics).

You can improve outcomes by:

* Adding missing articles.
* Breaking up broad content into more specific pieces.
* Using [Coaching](#coaching) to fine-tune how the Agent uses Knowledge.

**Want to see this in action?**
Check out the [Payment troubleshooting](/generative/docs/knowledge/core-workflows/knowledge-setup/best-practices#knowledge-example-payment-troubleshooting) and [Refund guidance](/generative/docs/knowledge/core-workflows/knowledge-setup/best-practices#knowledge-example-refund-guidance) examples. They show how clearer, more focused Knowledge helps the Agent give better answers, reduce [Handoffs](/generative/docs/handoffs), and improve the overall experience.

### If your AI Agent needs external data to help — Use Actions\[#actions-playbooks]

To perform at its best, your AI Agent needs access to more than just static content. That's where [Actions](/generative/docs/automation/actions) and [Playbooks](/generative/docs/automation/playbooks) come in:

* **Actions** let the Agent pull or send real-time data from your backend systems.
* **Playbooks** guide the Agent through multi-step flows — like collecting inputs, applying logic, and triggering Actions — based on the [Conversation](/generative/docs/optimization/conversations).

These tools improve your AI Agent's performance by enabling it to:

* Give personalized, accurate answers using live data
* Complete tasks on the customer's behalf, not just explain how to do them
* Reduce frustration and unnecessary [Handoffs](/generative/docs/handoffs) by resolving complex issues directly

Use Actions when static answers aren't enough — like checking order status, verifying refund eligibility, or retrieving account info.

**Want to see this in action?**
Check out the [Card fulfillment](/generative/docs/automation/actions/action-control/best-practices#actions-playbooks-example-card-fulfillment) and [Subscription refund status](/generative/docs/automation/actions/action-control/best-practices#actions-playbooks-example-subscription-refund-status) examples. They show how automation can lead to faster resolutions, better experiences, and a more capable AI Agent.

### If the response is almost right, but not quite — Use Coaching\[#coaching]

[Coaching](/generative/docs/optimization/coaching) helps you fine-tune how your AI Agent responds in specific situations — without changing its overall logic or retraining the model.

Use Coaching when the Agent gets the right intent but gives a response that's:

* Too vague
* Too formal
* Missing key details
* Lacking a clear next step

With Coaching, you can make quick, targeted improvements — like updating a message, pointing to a better article, triggering an [Action](/generative/docs/automation/actions), or improving how the Agent escalates.

This helps your AI Agent:

* Respond more clearly and helpfully
* Avoid unnecessary [Handoffs](/generative/docs/handoffs)
* Create a smoother support experience

**Want to see this in action?**
Check out the [Card fulfillment](/generative/docs/optimization/coaching/best-practices#coaching-example-card-fulfillment) and [Account cancellation](/generative/docs/optimization/coaching/best-practices#coaching-example-account-cancellation) examples. They show how small tweaks through Coaching can make a big impact on performance.

### If the interaction feels irrelevant or generic — Add Personalization\[#personalization]

[Personalization](/generative/docs/optimization/personalization/personalization-data) helps your AI Agent respond in a way that feels more relevant by using details like the customer's location, language, membership tier, or order history.

Use it when the Agent gives correct answers, but they feel too generic or disconnected. Small changes — like mentioning a user's plan or adjusting tone by region — can make responses feel more thoughtful and specific.

This helps your AI Agent:

* Sound more tailored and less robotic
* Set better expectations
* Improve customer trust and satisfaction

**Want to see this in action?**
Check out the [Membership support](/generative/docs/optimization/personalization/best-practices#personalization-example-membership-support) and [Product replacement by region](/generative/docs/optimization/personalization/best-practices#personalization-example-product-replacement) examples. They show how using Personalization can make your Agent more helpful and engaging.

<hr />

<p>
  Have any questions? Contact your Ada team, or email us at 

  <a href="mailto:help@ada.cx?subject=Help%20Docs%20inquiry" class="email">{"help@ada.cx"}</a>

  .
</p>