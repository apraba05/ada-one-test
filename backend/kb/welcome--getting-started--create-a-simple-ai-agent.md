---
title: Create a simple AI Agent
source_url: https://docs.ada.cx/docs/welcome/getting-started/create-a-simple-ai-agent
slug: welcome--getting-started--create-a-simple-ai-agent
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://docs.ada.cx/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.ada.cx/_mcp/server.

# Create a simple AI Agent

The following steps will guide you through setting up a basic AI Agent that can respond to customer inquiries using knowledge sources. This establishes a functional starting point before incorporating advanced automation features.

## When you'll see this setup process\[#when-youll-see-this]

* The specified AI Agent does not yet have any [Knowledge articles or sources](/generative/docs/knowledge).
* You have a role with edit [permissions](/generative/docs/other/team-access/my-team#user-permissions) (*Agent* or higher).
* You have not previously completed initial setup.

Most people who obtain access to their AI Agent don't go through this setup process. Ada's Customer Experience (CX) team usually configures AI Agents in advance, adding [Knowledge](#knowledge) (at minimum), and sometimes also customizing the [Persona](#persona). You'll only go through this flow if your AI Agent is brand new and hasn't been configured yet. **To ensure setup completes correctly, do not click the *Skip* button during the onboarding flow.**

## Step 1: Personalize your AI Agent\[#persona]

Choose or generate your AI Agent's name.

Verify your company name appears correctly.

Set your AI Agent's tone of voice (*Friendly*, *Plainspoken*, *Playful*, or *Sophisticated*).

Select an avatar from the available options or upload a custom one.

Click **Next** to continue.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/0b315f8104dcdf92c28032d5b070d2e8a65ac8fb7d87d0c714d790e3737bdb1b/versions/assets/images/gs_personalize.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225151Z&X-Amz-Expires=604800&X-Amz-Signature=f86339aadd6d5bf12a6b868fd408a644ffd37b8da58f69eb3186ce13a743169e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Personalize your AI Agent" />

## Step 2: Choose a sample skillset

Your AI Agent needs a field of knowledge to get started. Select one of the following:

* **Technology & software**: Answers common software and troubleshooting questions.
* **Retail & eCommerce**: Provides product recommendations, order tracking, return information, and more.
* **Banking & financial services**: Assists with checking balances, reviewing transactions, requesting new cards, and more.
* **Add my own content**: Start with a blank slate and define your AI Agent's knowledge manually.

On the right side of the page, sample conversations will appear to give you an idea of how each selection works. When ready, click **Next**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/2f823451a302bd7248cc182b25f153e2864ed7a9dd071f27390660206289fd1b/versions/assets/images/gs_skillset.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225151Z&X-Amz-Expires=604800&X-Amz-Signature=12ed64f50aba0a2c00bbb6632a3f65086a108ba94ba6c73cb1dbc9a0780f6354&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Choose your AI Agent's skillset" />

## Step 3: Watch a quick walkthrough

While Ada sets up your AI Agent, watch the introductory video that explains how your AI Agent works. Once setup is complete, click **Go to My Dashboard**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/84e2d69b8b71975fc38bf76faadbd3cdaa92141b5584c8f7db4d164177da9757/versions/assets/images/gs_goto_dashboard.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225151Z&X-Amz-Expires=604800&X-Amz-Signature=9121e756a0df336a1b9d293db8779aad8430f243d41a52d3756543df8002b4aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Go to your dashboard" />

## Step 4: Add Knowledge to your AI Agent\[#knowledge]

Your AI Agent relies on [Knowledge](/generative/docs/knowledge) sources to generate responses. In your Ada Dashboard, go to **Config > AI AGENT > Knowledge** to provide it with relevant and accurate information.

On the **Knowledge** page, you'll see a list of topics under the **Articles** tab, based on the skillset selected in [Step 2](#step-2-choose-a-sample-skillset). From here, you can do any of the following:

* **Connect a knowledge base**: Click **Add Source** and select an existing knowledge base integration, such as **Zendesk** or **Salesforce**.
* **Import website content**: Click **Add Source**, and select  **Website**. Then, name the source, specify the URLs you want to use, and click **Save**.
* **Create new articles**: Click **New Article**, enter content in the editor, and click **Save**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/e9c9471a041ba04af134a47a99fb2245ad0702eccd2e338199957938e19ccceb/versions/assets/images/gs_knowledge.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225151Z&X-Amz-Expires=604800&X-Amz-Signature=6f12ab8b07651d02bc105690f721c4d6b93c51b3398797c528fd76b1fa94b5f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Add Knowledge" />

## Step 5: Test your AI Agent's Knowledge

Now that your AI Agent has been set up with Knowledge sources, it's time to [test](/generative/docs/optimization/testing) how well it responds to customer inquiries.

In the left-side navigation, choose **Config > Test AI Agent**.

In the chat window, ask your AI Agent questions based on the knowledge sources you added. For example, if you selected *Technology & software*, ask something like: *How do I upgrade after the free trial?*

Review the AI Agent's responses. If needed, go back to the **[Knowledge](#knowledge)** section to add or refine information.

Continue testing with different questions to ensure your AI Agent provides accurate and relevant responses.

Once you're satisfied with its performance, you can proceed to enhancing automation with actions and processes in the next section.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/da055f990c786307d87ed3f31f09993cfe1af5c0e992ae0b5462bb525eb2406c/versions/assets/images/gs_test.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225151Z&X-Amz-Expires=604800&X-Amz-Signature=03cf1463d0357136b22c6e75f5da37e0c782993ddd1924a1db7f4b505254fa4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Test your AI Agent" />

<hr />

<p>
  Have any questions? Contact your Ada team, or email us at 

  <a href="mailto:help@ada.cx?subject=Help%20Docs%20inquiry" class="email">{"help@ada.cx"}</a>

  .
</p>