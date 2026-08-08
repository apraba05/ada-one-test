---
title: Article creation
source_url: https://docs.ada.cx/docs/knowledge/content-ingestion/article-creation
slug: knowledge--content-ingestion--article-creation
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://docs.ada.cx/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.ada.cx/_mcp/server.

# Article creation

## Overview

Article creation lets you add Knowledge content directly in Ada without updating your external knowledge base. This is useful when your AI Agent needs to provide different content from your connected knowledge sources.

## Limitations

Article creation has the following constraints:

* Changes to an article may take a few minutes before appearing consistently in generative answers. For timing expectations, see [Indexing latency & freshness](/generative/reference/knowledge/overview#indexing-latency-freshness).

## Use cases

Ada articles are useful for scenarios such as:

* Temporary content, like a promotion
* A product outage you need to communicate
* Formatting in your knowledge base that your AI Agent can't parse (e.g., images, complex tables, etc.), so you need to make an alternative version for your AI Agent

## Capabilities & configuration

Ada articles support the following options:

* **Rich text content**: Write article content directly in Ada with formatting support.
* **Availability rules**: Restrict articles to specific end users based on variable conditions.
* **Active/inactive status**: Control whether an article is available to your AI Agent without deleting it.
* **Draft mode**: Save articles as drafts before making them active.

## Quick start

Create a Knowledge article directly in Ada in a few steps.

**To create an article:**

On the Ada dashboard, go to **Config > AI AGENT > Knowledge**, then click **Create article**.

Enter an **Article Name** that describes the content.

Under **Content**, write your article content.

Enable the **Active** toggle and click **Save**.

For more options, see [Create an Ada article](#create-an-ada-article).

## Implementation & usage

Create, edit, and delete Knowledge articles directly in Ada to provide content for your AI Agent.

Before creating Ada articles, make sure you're familiar with the best practices in [Prepare your knowledge base as a source for AI generated content](/generative/docs/knowledge/core-workflows/knowledge-setup). Your AI Agent will be chunking and ingesting the information in this article like any other article in your knowledge base, so the more consistent you can make your content and its structure, the better chances you have of your AI Agent using your content to create relevant responses.

### Create an Ada article

Add Knowledge content directly in Ada when you need to supplement or override content from your connected knowledge sources.

**To create an Ada article:**

1. On the Ada dashboard, go to **Config > AI AGENT > Knowledge**. Then, at the top of the page, click **Create article**.
   The **Create article** dialog opens.

2. If required, you can restrict Ada articles to certain end users, based on information your AI Agent collects about your end users and saves in variables.

   You can only use variables your AI Agent can collect through your browser, or that you collect in a block and allow to be available outside of the structured content the block is in. You can't use variables your AI Agent collects using Actions.

   Beside **Availability**, you can click **Edit** to change which of your end users this Ada article is visible to.

   The **Set availability** window opens.

   * To make the article available to all end users, select **Everyone**.
   * To restrict the article to certain end users, select **Based on the following rules**. A section expands where you can enter the logic your AI Agent will use to decide whether to serve the article.

     <ol type="i">
       <li>
         Under 

         **Where**

         , in the 

         **Choose a variable**

          list, select a variable.
       </li>

       <li>
         In the next dropdown, select an operator so you can define a relationship between the variable and the value you want to target.
       </li>

       #### Understand comparison operators

       Comparison operators are logic statements that tell your AI Agent to match end user information that's captured in the variable you're using. The available operators vary based on the variable type you're using:

       | **Operator**                                                                                                            | **Variable types**                                                                                        | **Description**                                                                                  |
       | :---------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
       | ![Begins With icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/e8b9c807586a4238654793da51b49ec15e7045c0691d461567178070e57a1840/versions/assets/image/uuid-a2a98e3d-9b57-9aef-9015-811511180acc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225333Z&X-Amz-Expires=604800&X-Amz-Signature=47ebf705107eafa8b33dea5e625cf3e38b55d92a5f0292e90565793f0c8c190f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Begins With**           | <p>- All text variables (including phone and email)</p>                                                   | Match information in the variable that begins with certain text (partial match).                 |
       | ![Ends With icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/9bc404d3db5ea684a901bf8426485894bb62abb8369e498b98dc4e4f3807a5ec/versions/assets/image/uuid-4c3f70e3-9921-9b1a-bcf2-fff04c0c389c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225333Z&X-Amz-Expires=604800&X-Amz-Signature=70c58923ea63b6c9ea3f5d883f563221b8b672c2078cab1a201cad71c4922b7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Ends With**               | <p>- All text variables (including phone and email)</p>                                                   | Match information in the variable that ends with certain text (partial match).                   |
       | ![Contains icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/a4f0225811b1ecde2f125de907c2ad1b084268805cd89a00f465649ddbf8eaa2/versions/assets/image/uuid-b0ca4ac7-18c4-d71d-9ff7-a56de57685bf.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225333Z&X-Amz-Expires=604800&X-Amz-Signature=a52f5493b3d5a986bd7a1a2acd38ab6cf3ebec25e338ff87246fdeb35f99ef8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Contains**                 | <p>- All text variables (including phone and email)</p><p>- List variables</p>                            | Match information in the variable that contains certain text in any position (partial match).    |
       | ![Is icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/7266dedcf2da1af5c496469379bd4fb68d5e65492c190e9567c75edbbbf7e260/versions/assets/image/uuid-ed7679a6-76c6-f8b3-d8cd-1323e8d98e0a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225333Z&X-Amz-Expires=604800&X-Amz-Signature=8e0f3e6326958a931e17f451b660af34dd74831efae3e5b98d977234625d10f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Is**                             | <p>- All text variables (including phone and email)</p> <p>- Number variables</p>                         | Match information in the variable that equals specific text exactly (exact match).               |
       | ![Is Not icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/d94952ab65e9f266413c582390a1d702ebb32c7a2023709ee96741b6df1b17e4/versions/assets/image/uuid-52c3ace1-f490-92df-8e17-aaa08418541b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225333Z&X-Amz-Expires=604800&X-Amz-Signature=a0b88342d9ef43cf26b9d9c629d6561fe3488aa2fe139c91ab08731b5685325a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Is Not**                     | <p>- All text variables (including phone and email)</p> <p>- Number variables</p>                         | Match information in the variable that does not equal specific text exactly (exact match).       |
       | ![Is Not Set icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/283cad3d89c7d92f279d722592cd958630a40527266a47d316ab3b3b2051b71f/versions/assets/image/uuid-498cb9b2-2d9e-40ef-9ed1-3cf51dc4a1d4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225333Z&X-Amz-Expires=604800&X-Amz-Signature=70927b1155446f49e80712f98e10108ced4fb716a93f4d2cd506b4db089be0fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Is Not Set**             | <p>- All text variables (including phone and email)</p> <p>- Number variables</p> <p>- List variables</p> | Match if there is no information contained in the variable.                                      |
       | ![Is Set icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/8c1019797a0482018682d52622c9e2fe56ddc5aef8925dc3e3db678c121c6869/versions/assets/image/uuid-dc59d677-9ded-d825-48e9-0fb7f5c48439.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225333Z&X-Amz-Expires=604800&X-Amz-Signature=628272549a54932b758b338712445c96d38d1aad0ffb6ffc2ccb71a973423b4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Is Set**                     | <p>- All text variables (including phone and email)</p> <p>- Number variables</p> <p>- List variables</p> | Match if there is any information contained in the variable.                                     |
       | ![Greater Than icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/45636711dfe933087353da3923c6865b6816ea671ad6e9db4739aeea4c80a697/versions/assets/image/uuid-ea44ef37-6ef9-3b44-c1f6-86b4315c160c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225333Z&X-Amz-Expires=604800&X-Amz-Signature=5916a2b4a46ec9bb15c3d2853d7269e31146c35a500a712a78f8b8106428d7c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Greater Than**         | <p>- Number variables</p>                                                                                 | Match if the information in the variable is greater than a specific value.                       |
       | ![Less Than icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/f2448b33a8931270e63ea8daab74e67ade1fdfdf1f8853529c2fb0a3e5abda55/versions/assets/image/uuid-6ad2273c-89e8-79b7-92ba-dd766b493b5f.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225333Z&X-Amz-Expires=604800&X-Amz-Signature=906cdce7872ab717a2eadcf8f9d2eb8196cf6cdef73371864f8234405dabfa2f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Less Than**               | <p>- Number variables</p> <p>- List variables</p>                                                         | Match if the information in the variable is less than a specific value.                          |
       | ![Is True icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/fcf3fe21099df957ee22609d5a5c211601d3e402fcc8402c12115f4680a692b0/versions/assets/image/uuid-b75658a2-623f-1317-139d-469254aca9cd.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225333Z&X-Amz-Expires=604800&X-Amz-Signature=1546c964b7e524f53a2dbd691babd3ee95d37fba458f37bf33890913dbff75b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Is True**                   | <p>- Yes/No variables</p>                                                                                 | Match if the information in a variable is Yes (or True).                                         |
       | ![Is False icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/2b5c661e7e4445f1ea8f7736ee5b58b14f72283faf2dbd4f01220a26d621b238/versions/assets/image/uuid-83141cb5-fee0-686e-fb7e-5848842bd2af.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225333Z&X-Amz-Expires=604800&X-Amz-Signature=e8b750a737dfe694a75292e96797502b439bf2e7c8251078ff0a39c0fb11d9b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Is False**                 | <p>- Yes/No variables</p>                                                                                 | Match if the information in a variable is No (or False).                                         |
       | ![Does Not Contain icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/2a459cf7a992abeb5cbdf8438f9f1be356bb5fcf915f55f7f1c2cdc3173b101d/versions/assets/image/uuid-a84f6c2f-dedb-70d5-7265-a0d7073bd683.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225333Z&X-Amz-Expires=604800&X-Amz-Signature=509ac44c479b4544a61762ec19633303712a0c5eba4f1807b6754c1767ae75ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Does Not Contain** | <p>- List variables</p>                                                                                   | Match if none of the selected items contains this value.                                         |
       | ![Is Equal To icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/7266dedcf2da1af5c496469379bd4fb68d5e65492c190e9567c75edbbbf7e260/versions/assets/image/uuid-ed7679a6-76c6-f8b3-d8cd-1323e8d98e0a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225333Z&X-Amz-Expires=604800&X-Amz-Signature=8e0f3e6326958a931e17f451b660af34dd74831efae3e5b98d977234625d10f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Is Equal To**           | <p>- List variables</p>                                                                                   | Match if the end user selected a particular number of options in a List Option block.            |
       | ![Is Greater Than icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/45636711dfe933087353da3923c6865b6816ea671ad6e9db4739aeea4c80a697/versions/assets/image/uuid-ea44ef37-6ef9-3b44-c1f6-86b4315c160c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225333Z&X-Amz-Expires=604800&X-Amz-Signature=5916a2b4a46ec9bb15c3d2853d7269e31146c35a500a712a78f8b8106428d7c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Is Greater Than**   | <p>- List variables</p>                                                                                   | Match if the end user selected more than a particular number of options in a List Option block.  |
       | ![Is Less Than icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/f2448b33a8931270e63ea8daab74e67ade1fdfdf1f8853529c2fb0a3e5abda55/versions/assets/image/uuid-6ad2273c-89e8-79b7-92ba-dd766b493b5f.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225333Z&X-Amz-Expires=604800&X-Amz-Signature=906cdce7872ab717a2eadcf8f9d2eb8196cf6cdef73371864f8234405dabfa2f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Is Less Than**         | <p>- List variables</p>                                                                                   | Match if the end user selected fewer than a particular number of options in a List Option block. |

       <li>
         In the 

         **Value**

          field, enter or select a value for the variable that you want to use to target end users.
       </li>

       <li>
         If required, add additional conditions.
       </li>

       * To add a new **top-level** condition, click **Add** <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/b0aa6bd9ade574c33763556b72bedb3fb7ba2384bf0c25ef6cc5401eab220757/versions/assets/image/button-add.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225333Z&X-Amz-Expires=604800&X-Amz-Signature=823a4ffbabc6321871f74fad5d76b18ec225f7c2e6aac1dbfe68ecdee1eb9460&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" />.
         <p>If you're adding your first additional top-level condition, in the dropdown that appears, choose **And** or **Or** as the operator for all of your top-level conditions.</p>
       * To create or add to a **group** of conditions, click the **Add to group** icon <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/881a5902ee010bd99b16914b2ac663810ad93cade88c2fddc273b4c3bc508b28/versions/assets/image/icon-add.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225333Z&X-Amz-Expires=604800&X-Amz-Signature=b1bf193807389fbc89b8781d9c2268ddc2d2deb34c375ab0ee6ff61e657a49d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" /> beside a condition you want to include in the group.
         <p>If you're creating a group, in the dropdown that appears, choose **And** or **Or** as the operator for all of the conditions in that group.</p>
     </ol>

3. Under **Article Name**, enter a name for the article, so both you and your AI Agent can get an idea of the information it contains.

4. Under **Content**, write your article content.

5. To save your article content as a draft, click **Save**. When you're ready for your content to be available for end users, enable the **Active** toggle to make it available for your AI Agent to use in its responses.

### Edit or delete an Ada article

Update or remove Ada articles when your Knowledge content needs to change.

**To edit or delete an Ada article:**

1. On the Ada dashboard, go to **Config > AI AGENT > Knowledge**, then click the name of the article you want to edit.

   To find all of your Ada articles, you can filter articles by source and select **Created in Ada**.

2. Click the name of your Ada article.

   The **Article preview** dialog opens, with your saved article in it.

3. Edit or delete the article.
   * To edit it, click **Edit**, then make the edits to your article and click **Save**.
   * To delete it, click **Delete**.

## Related features

Expand your AI Agent's Knowledge with these related capabilities:

* **[Knowledge integrations](/generative/docs/knowledge/content-ingestion/knowledge-integration)**: Connect external knowledge bases like Zendesk, Salesforce, or Contentful.
* **[Web import](/generative/docs/knowledge/content-ingestion/web-import)**: Import content from public-facing websites.

<hr />

<p>
  Have any questions? Contact your Ada team, or email us at 

  <a href="mailto:help@ada.cx?subject=Help%20Docs%20inquiry" class="email">{"help@ada.cx"}</a>

  .
</p>