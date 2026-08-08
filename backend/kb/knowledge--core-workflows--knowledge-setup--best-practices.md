---
title: Best practices
source_url: https://docs.ada.cx/docs/knowledge/core-workflows/knowledge-setup/best-practices
slug: knowledge--core-workflows--knowledge-setup--best-practices
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://docs.ada.cx/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.ada.cx/_mcp/server.

# Best practices

## Overview

Improving your AI Agent isn't just about adding more articles—it's about structuring Knowledge so it reflects how people actually ask questions. When your content is clear, focused, and written in natural language, the Agent can provide more accurate answers and create a smoother experience for end users.

## Examples

The following examples demonstrate how to restructure Knowledge to improve AI Agent responses.

### Example: Payment troubleshooting\[#knowledge-example-payment-troubleshooting]

End users often ask why their payments are being declined, and the AI Agent points them to a generic *Common Payment Issues* article. While the article is technically accurate, it doesn't always provide the exact answer end users are looking for—leading to unnecessary frustration or escalations.

**To improve payment troubleshooting responses:**

1. Split the generic article into focused ones, such as *Card declined at checkout* and *Fixing payment verification errors*.
2. Use clear titles and keywords so the Agent can select the right article based on specific end user phrasing.
3. Include examples and common causes in each article, like insufficient funds, expired cards, or incorrect billing info.
4. Write articles in plain language with clear steps end users can try before escalating.

For example:

<table>
  <tr>
    <td>
      <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/967eb6a1d1d3d61c46614342d127807964439c89024e368debc8a80e52f1e233/versions/assets/image/improv_topics_example13.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225240Z&X-Amz-Expires=604800&X-Amz-Signature=91326edcc669ac233da95e3d126b57da56ec892d378da673bad7e944d852a976&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" />
    </td>

    <td>
      <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/0fb19afbe654b7269e755adcc0a96ad2d90d00b52f8e2b48b27a04bdfee01b0c/versions/assets/image/improv_topics_example14.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225240Z&X-Amz-Expires=604800&X-Amz-Signature=42ca9825a856ff6861644d3cfb0c37f0e8961be864be33f40d9ed93289e62bab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" />
    </td>
  </tr>
</table>

By organizing your knowledge this way, the Agent can surface more relevant answers, helping end users resolve payment issues quickly and reducing reliance on support teams.

### Example: Refund guidance for teen users\[#knowledge-example-refund-guidance]

Younger end users frequently ask how to get a refund from third-party apps or vendors. Since the knowledge base doesn't include a relevant article, the AI Agent escalates these conversations by default—even when the answer is simple and well-documented elsewhere.

**To add refund guidance for younger end users:**

1. Create a short, friendly article that explains how to request a refund from a third-party seller (e.g., *How to get a refund from an app store or game platform*).
2. Use approachable language that reflects how younger end users naturally ask for help (e.g., *I want my money back from a game* or *I bought something by accident*).
3. Include platform-specific instructions where possible (e.g., links to Apple, Google Play, or in-game refund request forms).
4. Add relevant tags and keywords so the Agent can find and serve the article when end users ask in casual or informal ways.

By providing clear, age-appropriate guidance, you empower the Agent to respond helpfully—reducing handoffs and improving the experience for younger end users.

For example:

<table>
  <tr>
    <td>
      <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/f7d47b76540a44076db8ae1f983b6687f0ae753d588586dd1f8fb94eb45b916d/versions/assets/image/improv_topics_example15.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225240Z&X-Amz-Expires=604800&X-Amz-Signature=1132b2c8b6ce573a0b31242a6bd293f8c0a55b9836620a613e31b25a347dfaca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" />
    </td>

    <td>
      <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/b18de454925f5988007a08bc1fd44bdc5b8b85862d4f3968e07b66806f474962/versions/assets/image/improv_topics_example16.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225240Z&X-Amz-Expires=604800&X-Amz-Signature=3d4fe9a71eff8d181c8b405c3d1c396c4ba45b0d1e749608020202bd653cb1f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" />
    </td>

    <td>
      <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/71d2c1b4f49ad0b3ec0ece6ef8016134653416983f0eaa2836f91c9d781772b8/versions/assets/image/improv_topics_example17.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225240Z&X-Amz-Expires=604800&X-Amz-Signature=9f9d2a0b5b6e0aac1e780e7c6a6467ef115f851aea215a9968c379b4e5c7be63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" />
    </td>
  </tr>
</table>

**Next steps:**
To improve this experience further, apply [Personalization](/generative/docs/optimization/personalization/personalization-data) to detect the end user's age group (e.g., based on app usage context or declared info), so the Agent can tailor its tone and resources accordingly. Also, consider using [Coaching](/generative/docs/optimization/coaching/coaching-tools) to guide the Agent to suggest the newly created article when end users mention refund-related terms in informal language.

This combination ensures the Agent not only finds the right information but delivers it in a way that resonates with younger end users.

<hr />

<p>
  Have any questions? Contact your Ada team, or email us at 

  <a href="mailto:help@ada.cx?subject=Help%20Docs%20inquiry" class="email">{"help@ada.cx"}</a>

  .
</p>