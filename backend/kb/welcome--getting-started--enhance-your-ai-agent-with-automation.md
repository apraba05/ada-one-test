---
title: Enhance your AI Agent with automation
source_url: https://docs.ada.cx/docs/welcome/getting-started/enhance-your-ai-agent-with-automation
slug: welcome--getting-started--enhance-your-ai-agent-with-automation
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://docs.ada.cx/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.ada.cx/_mcp/server.

# Enhance your AI Agent with automation

Once your AI Agent is set up with basic [Knowledge](/generative/docs/knowledge), you can expand its capabilities with [Actions](/generative/docs/automation/actions), [Playbooks](/generative/docs/automation/playbooks), and custom configurations to improve automation and engagement.

## When you’ll see this setup process\[#when-youll-see-this]

* Your AI Agent has already been configured with basic [Knowledge](/generative/docs/knowledge).
* You have a role with edit [permissions](/generative/docs/other/team-access/my-team#user-permissions) (*Agent* or higher).
* You have not previously completed the automation setup flow.

Many AI Agents will already have some automation configured by Ada's Customer Experience (CX) team during initial setup — including [Greeting](#greeting), [Actions](#actions), or [Playbooks](#playbooks). You'll see this setup flow only if your AI Agent doesn't yet have these automation elements in place, or if you're adding new automation for the first time.

## Step 1: Add Actions\[#actions]

[Actions](/generative/docs/automation/actions) are tasks your AI Agent can perform, such as retrieving data from an external system or completing a customer-related workflow. They enable your Agent to go beyond answering questions and actually take action on behalf of your customers.

Before you can create Actions, you'll need to set up [Tokens](/generative/docs/automation/actions/token-configuration). Tokens provide the secure authentication your Agent relies on to connect with external systems.

Once your tokens are in place, you can create Actions by defining their inputs, outputs, and logic to match your customer workflows.

To get started, in your AI Agent's Ada Dashboard, navigate to **Config > AI AGENT > Actions**. On the **Actions** page, click **Manage Tokens**, then on the **Tokens** page, click **New Token**. Enter the required details, such as token name and type.

If you need to retrieve the token from a customer login, you'll also need to provide additional fields, including Auth URI, Client ID, and any others requested. When you finish adding all details, click **Save** to finish creating the token.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/1e2d095657d0e3b672b303f602eeaea2e18c09365fc299e5d5f94538162f3135/versions/assets/images/gs_token.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225153Z&X-Amz-Expires=604800&X-Amz-Signature=ea37a2887b257d1449ec9c8022149cf877a512ad54741ad65843d62044dfb95a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Create a token" />

After creating a token, click the **Back** button to return to the Actions page. From there, click **New Action**, give it a name and a description.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/b89758badfabc3c0b917c802ec4c2b964a5bf18a16f4bf79159f9c8540934e46/versions/assets/images/gs_new_action.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225153Z&X-Amz-Expires=604800&X-Amz-Signature=d556a0458bb4f24d044e237f156451b7c990b2c61506fd7feea61bd9fad56266&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Create a new Action" />

Build the API call. Enter the endpoint details, request format, and required headers.

Define API outputs. Choose which data from the response should be available for future interactions.

Test the API response. Use sample values to verify functionality.

Save the Action. Choose whether to activate or keep it inactive for now.

You can also import an Action in JSON format if needed.

## Step 2: Add a Playbook\[#playbooks]

[Playbooks](/generative/docs/automation/playbooks) allow your AI Agent to manage multi-step interactions and guide customers through more complex workflows. They combine conditions, actions, and responses to create tailored conversational paths.

In the Ada Dashboard, navigate to **Config > AI AGENT > Playbooks**.

Let Ada write your Playbook. On the **Create your first Playbook** page that appears, select **Generate a Playbook**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/7d10239ac1b18790dd3a5e0e04aa424c67cbf86be3f57e244c00a0d3e9e556fb/versions/assets/images/gs_create_playbook.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225153Z&X-Amz-Expires=604800&X-Amz-Signature=bdfe99574ed7ed4bd5ca7361964fc40c19669017c63cbc847d168577a79f3655&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Create a new Playbook" />

To quickly create your first Playbook, use AI generation. Simply choose a product area (for example, *SaaS*) and select a relevant use case (for example, *Help customers manage their subscription plans and upgrades*). You can also enter your own description if you have a specific workflow in mind.

Next, click **Generate Playbook** to produce a draft you can review and refine. This gives you a strong starting point—even if you're not sure how to structure the workflow yourself.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/7dea69a0bd7b605f1166c95b99ae1ec5a826913eaaaea15f801c81a2e806caaa/versions/assets/images/gs_select_usecase.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225153Z&X-Amz-Expires=604800&X-Amz-Signature=cb0446bcba504210c20772833b4c7ca1a22c8d0ec70741f8e800df0393537f1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Select your use case" />

Review your Playbook and confirm it references the [newly created Action](#actions).

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/c5c2fc9d87dbf76463fa04cf91ba49e9f6bb34129d98f01768134cd966f20a30/versions/assets/images/gs_reference_action.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225153Z&X-Amz-Expires=604800&X-Amz-Signature=6b083571e8a13971dd42cf11a835e9d9f60c2d5ec37cdc34d58d8febd567d82b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Reference your Action" />

Click **Save** to activate or keep it inactive for further adjustments.

For details, see [this section](/generative/docs/automation/playbooks).

## Step 3: Customize the Greeting\[#greeting]

First impressions matter! Define how your AI Agent starts conversations:

In the Ada Dashboard, navigate to **Config > AI AGENT > Greeting**.

Refine your greeting text and optionally add variations to keep responses fresh.

Click **Save** to finalize the greeting.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/4c200e347159a0b1738ad1e787fe5a5c9c0c056dfdca66bdd07d80f51e88d1b0/versions/assets/images/gs_greeting.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225153Z&X-Amz-Expires=604800&X-Amz-Signature=7ba8de2697e1e0667042bea16a59f7ef7812a80410bddd7722b76ecf153905f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Customize your Greeting" />

For details, see [this section](/generative/docs/automation/greetings).

## Step 4: Invite team members

Collaboration is key! Invite your team members to edit, test, and monitor your AI Agent:

In the Ada Dashboard, at the bottom of the left navigation, select your initial, then choose **My team**.

On the **Team** page, in the **Invite members** area, add team members. For each user, type their full name, email, and select their role. Then, click **Send Invitation**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/eea65fa699ff89e264be76dd4abbac7190adf99d77725c88c77bbd9984ecceaf/versions/assets/images/gs_team.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225153Z&X-Amz-Expires=604800&X-Amz-Signature=26e83cf605e92e0adaf30933ec69b45fb4bfc0a96f80789d2319b93ec10cf45b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Invite team members" />

For details, see [this section](/generative/docs/other/team-access/my-team).

## Step 5: Test your AI Agent

Now it's time to [test](/generative/docs/optimization/testing) your AI Agent with its enhanced capabilities. In the left-side navigation, click **Test** and start a conversation.

Try different types of inquiries to evaluate your AI Agent’s performance:

* **Actions**: Test API-powered interactions, such as retrieving order details or account information.
* **Playbooks**: Walk through multi-step workflows to confirm your AI Agent follows structured automation correctly.
* **Greeting**: Verify that the customized greeting appears as expected when the conversation starts.

Additionally, if you invite team members, collaborate by having them test different scenarios and provide feedback. Based on the test results, make any necessary adjustments to improve responses and automation before launching your AI Agent.

## What's next?

That's it! You've successfully created your first AI Agent. From here, you can continue refining its responses, improving workflows, and expanding integrations.

Some customers may also need access to additional features. If this applies to you, reach out to your Ada representative for more information. These additional features can include:

* **[Channel](/generative/docs/channels)-specific access**: For billing reasons, [Voice](/generative/docs/channels/voice) and [Social](/generative/docs/channels/social) channels may need to be enabled separately.
* **[Handoffs](/generative/docs/handoffs)**: Depending on your plan and tools in use, handoffs may include Zendesk Messaging, Zendesk Chat, Salesforce Chat, Salesforce Messaging, or a custom solution built by Ada’s Solutions team.
* **Additional integrations and customizations**: Some scenarios may require a more personalized setup or connections to specific third-party integrations.

Your Ada representative can walk you through these options and help you get set up with the features that best support your business.

<hr />

<p>
  Have any questions? Contact your Ada team, or email us at 

  <a href="mailto:help@ada.cx?subject=Help%20Docs%20inquiry" class="email">{"help@ada.cx"}</a>

  .
</p>