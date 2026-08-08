---
title: Content generation
source_url: https://docs.ada.cx/docs/knowledge/core-workflows/content-generation
slug: knowledge--core-workflows--content-generation
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://docs.ada.cx/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.ada.cx/_mcp/server.

# Content generation

## Overview

When you connect your AI Agent to your knowledge base and start to serve
automatically generated content to your customers, it might feel like
magic. But it's not! This topic takes you through what happens behind
the scenes when you start serving knowledge base content to customers.

## Knowledge base ingestion\[#UUID-6cc7c6af-e576-55c7-2fb8-aa8eb0d3e599\_section-idm459780816249123374949131016]

When you link your knowledge base to your AI Agent, your AI Agent copies down all
of your knowledge base content, so it can quickly search through it and serve relevant information from it. Here's how it
happens:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/890ae851f77ef4720c18ebb436dd3338845b16ba49e436293cb67414d209feb4/versions/assets/images/knowledge-base-ingestion.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225223Z&X-Amz-Expires=604800&X-Amz-Signature=5f925998a1b989da72ee11dcb46c2f578e9c1efbbf0e86cb3f57c9c4e4be5748&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" />

1. When you link your AI Agent with your knowledge base, your AI Agent
   imports all of your knowledge base content.

   Depending on the tools you use to create and host your knowledge
   base, your knowledge base then updates with different frequencies:

   * If your knowledge base is in Zendesk or Salesforce, your AI Agent
     checks back for updates every 15 minutes.

     * If your AI Agent hasn't had any conversations, either immediately
       after you linked it with your knowledge base or in the last 30
       days, your AI Agent pauses syncing. To trigger a sync with your
       knowledge base, have a test conversation with your AI Agent.

   * If your knowledge base is hosted elsewhere, you or your Ada team
     have to build an integration to scrape it and upload content to
     Ada's Knowledge API. If this is the case, the frequency of updates
     depends on the integration.

2. Your AI Agent splits your articles into chunks, so it doesn't have to
   search through long articles each time it looks for information - it
   can just look at the shorter chunks instead.

   While each article can cover a variety of related concepts, each
   chunk should only cover one key concept. Additionally, your AI Agent
   includes context for each chunk; each chunk contains the headings
   that preceded it.

3. Your AI Agent sends each chunk to a Large Language Model (LLM), which it
   uses to assign the chunks numerical representations that correspond
   to the meaning of each chunk. These numerical values are called
   embeddings, and it saves them into a database.

   The database is then ready to provide information for GPT to put
   together into natural-sounding responses to customer questions.

## Response generation\[#UUID-6cc7c6af-e576-55c7-2fb8-aa8eb0d3e599\_section-idm4568323742001633749558059795]

After saving your knowledge base content into a database, your AI Agent is
ready to provide content from it to answer your customers' questions.
Here's how it does that:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/452f4d239a76b826d29569cf7681fc3d2c02b8a91dcf5c703adc3a12a75e9672/versions/assets/image/uuid-b0b3dc08-dc83-ef45-dbb4-1d05e2e2f556.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225223Z&X-Amz-Expires=604800&X-Amz-Signature=3adee41a93c74bd94ffc605ece4bd3c0416fc905f4f23462b8a3c950073d26bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" />

1. Your AI Agent sends the customer's query to the LLM, so it can get an
   embedding (a numerical value) that corresponds with the information
   the customer was asking for.

   Before proceeding, the AI Agent sends the content through a moderation
   check via the LLM to see if the customer's question was inappropriate
   or toxic. If it was, your AI Agent rejects the query and doesn't continue
   with the answer generation process.

2. Your AI Agent then compares embeddings between the customer's question and
   the chunks in its database, to see if it can find relevant chunks
   that match the meaning of the customer's question. This process is
   called retrieval.

   Your AI Agent looks for the best match in meaning in the database to what
   the customer asked for, which is called semantic similarity, and
   saves the top three most relevant chunks.

   If the customer's question is a follow-up to a previous question,
   your AI Agent might get the LLM to rewrite the customer's question to
   include context to increase the chances of getting relevant chunks.
   For example, if a customer asks your AI Agent whether your store sells
   cookies, and your AI Agent says yes, your customer may respond with "how
   much are they?" That question doesn't have enough information on its
   own, but a question like "how much are your cookies?" provides
   enough context to get a meaningful chunk of information back.

   If your AI Agent isn't able to find any relevant matches to the customer's
   question in the database's chunks at this point, it serves the
   customer a message asking them to rephrase their question or
   escalates the query to a human agent, rather than attempting to
   generate a response and risking serving inaccurate information.

3. Your AI Agent sends the three chunks from the database that are the most
   relevant to the customer's question to GPT to stitch together into a
   response. Then, your AI Agent sends the generated response through three
   filters:

   <ol type="a">
     <li>
       The 

       **Safety**

        filter checks to make sure that the generated
       response doesn't contain any harmful content.
     </li>

     <li>
       The 

       **Relevance**

        filter checks to make sure that the generated
       response actually answers the customer's question. Even if the
       information in the response is correct, it has to be the
       information the customer was looking for in order to give the
       customer a positive experience.
     </li>

     <li>
       The 

       **Accuracy**

        filter checks to make sure that the generated
       response matches the content in your knowledge base, so it can
       verify that the AI Agent's response is true.
     </li>
   </ol>

4. If the generated response passes these three filters, your AI Agent
   serves it to the customer.

<hr />

<p>
  Have any questions? Contact your Ada team, or email us at 

  <a href="mailto:help@ada.cx?subject=Help%20Docs%20inquiry" class="email">{"help@ada.cx"}</a>

  .
</p>