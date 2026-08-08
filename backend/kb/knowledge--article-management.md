---
title: Article management
source_url: https://docs.ada.cx/docs/knowledge/article-management
slug: knowledge--article-management
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://docs.ada.cx/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.ada.cx/_mcp/server.

# Article management

## Overview

Article management lets you control which Knowledge articles your AI Agent can use when creating responses. After you've imported your articles, they appear on the **Knowledge** page, sorted so the articles that were most recently updated in your knowledge base appear first.

## Use cases

Article management helps you curate your AI Agent's knowledge to improve response quality.

* **Exclude outdated content**: Disable articles that contain outdated information until they are updated in your knowledge base.
* **Control sensitive information**: Restrict certain articles to specific end users based on variables like region or account type.
* **Test new content**: Disable new articles initially, then enable them after verifying they produce appropriate responses.
* **Seasonal or promotional content**: Activate or deactivate articles for time-limited campaigns or events.

## Capabilities & configuration

Article management provides the following controls:

* **Active/inactive status**: Enable or disable individual articles or bulk-select multiple articles at once.
* **Availability rules**: Restrict articles to specific end users based on variable conditions.
* **Search and filter**: Find articles by name, status, source, language, or custom tags.
* **Pagination**: Navigate through large article lists with customizable page sizes.

## Quick start

Control article availability in a few steps.

**To enable or disable articles:**

Go to **Config > AI AGENT > Knowledge**.

Select the check boxes beside the articles you want to change.

Click **Set as active** or **Set as inactive**.

For more options, see [Enable or disable articles](#enable-disable-articles).

## Implementation & usage

Manage article status, availability, and filtering to control how your AI Agent uses Knowledge content.

### Enable or disable articles\[#enable-disable-articles]

Control whether your AI Agent can create content from individual Knowledge articles. By default, when you connect your knowledge base to Ada, all articles are active, which means your AI Agent can create responses from them.

**To enable or disable articles:**

1. On the Ada dashboard, go to **Config > AI AGENT > Knowledge**.

2. Change settings for articles one by one, or select the articles you want to include or exclude all at once. If you want to see any of your articles in more detail, you can click an article's name to open it in a new tab.

   * To include or exclude an individual article from your AI Agent's response content, toggle the **Active** setting beside it.

   * To change article status in bulk, select the relevant check boxes to the left of the article name.

     To find articles, you can enter search terms in the **Search by article name** field, or click the **Filter** list to filter articles by:

     * Whether the articles are currently active
     * The source they came from
     * The language they're in
     * Any custom [article tags](https://developers.ada.cx/reference/tags-knowledge-api) you associated with them using the Knowledge API

     Then, you can select articles from your results.

     At the bottom of the list of articles, you can also change how many articles to display at a time, or move between pages. Even if you scroll through different pages onscreen, the dashboard remembers the articles you've already selected.

3. At the bottom of the page, click either **Set as inactive** or
   **Set as active**. Your AI Agent immediately adds or removes your selected articles from the content it can use to generate responses.

### Restrict article availability\[#article-rules]

Limit which end users can access specific Knowledge articles based on variable values. You can restrict Ada articles to certain end users based on information your AI Agent collects and saves in variables.

You can only use variables your AI Agent can collect through your browser, or that you collect in a block and allow to be available outside of the structured content the block is in. You can't use variables your AI Agent collects using Actions.

**To restrict article availability:**

1. On the Ada dashboard, go to **Config > AI AGENT > Knowledge**.

2. Select the articles you want to change the availability for.

   To find articles, you can enter search terms in the **Search by article name** field, or click the **Filter** list to filter articles by:

   * Whether the articles are currently active
   * The source they came from
   * The language they're in
   * Any custom [article tags](https://developers.ada.cx/reference/tags-knowledge-api) you associated with them using the Knowledge API

   Then, you can select articles from your results.

   At the bottom of the list of articles, you can also change how many articles to display at a time, or move between pages. Even if you scroll through different pages onscreen, the dashboard remembers the articles you've already selected.

3. Click **Set availability**. The Set availability window opens.

   * To restrict the article to certain end users, select **Based on the following rules**.
   * A section expands where you can enter the logic your AI Agent will use to decide whether to serve the article.

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
       | ![Begins With icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/e8b9c807586a4238654793da51b49ec15e7045c0691d461567178070e57a1840/versions/assets/image/uuid-a2a98e3d-9b57-9aef-9015-811511180acc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225344Z&X-Amz-Expires=604800&X-Amz-Signature=ff93ae6c94f9582dd9dab86e2625e64b24bf363d716a2543f5148b5b2cf9f1f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Begins With**           | <p>- All text variables (including phone and email)</p>                                                   | Match information in the variable that begins with certain text (partial match).                 |
       | ![Ends With icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/9bc404d3db5ea684a901bf8426485894bb62abb8369e498b98dc4e4f3807a5ec/versions/assets/image/uuid-4c3f70e3-9921-9b1a-bcf2-fff04c0c389c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225344Z&X-Amz-Expires=604800&X-Amz-Signature=c23ef857ec010cfd490d494c4f2941659f7779ea6866357e5e1b159ad8582e82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Ends With**               | <p>- All text variables (including phone and email)</p>                                                   | Match information in the variable that ends with certain text (partial match).                   |
       | ![Contains icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/a4f0225811b1ecde2f125de907c2ad1b084268805cd89a00f465649ddbf8eaa2/versions/assets/image/uuid-b0ca4ac7-18c4-d71d-9ff7-a56de57685bf.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225344Z&X-Amz-Expires=604800&X-Amz-Signature=2dfba80d26112b60fd02c7c2b2827f26851bb534163f98f0edcc1533726946e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Contains**                 | <p>- All text variables (including phone and email)</p><p>- List variables</p>                            | Match information in the variable that contains certain text in any position (partial match).    |
       | ![Is icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/7266dedcf2da1af5c496469379bd4fb68d5e65492c190e9567c75edbbbf7e260/versions/assets/image/uuid-ed7679a6-76c6-f8b3-d8cd-1323e8d98e0a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225344Z&X-Amz-Expires=604800&X-Amz-Signature=a25f10ee7283af7c424eeb94bc2accdc49c8e2391cd1aa6287f27cb1cbdf8f30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Is**                             | <p>- All text variables (including phone and email)</p> <p>- Number variables</p>                         | Match information in the variable that equals specific text exactly (exact match).               |
       | ![Is Not icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/d94952ab65e9f266413c582390a1d702ebb32c7a2023709ee96741b6df1b17e4/versions/assets/image/uuid-52c3ace1-f490-92df-8e17-aaa08418541b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225344Z&X-Amz-Expires=604800&X-Amz-Signature=a220a4467783435c1a3f45de44c261b2755d4a184da9e16ee58ecfb4829ab837&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Is Not**                     | <p>- All text variables (including phone and email)</p> <p>- Number variables</p>                         | Match information in the variable that does not equal specific text exactly (exact match).       |
       | ![Is Not Set icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/283cad3d89c7d92f279d722592cd958630a40527266a47d316ab3b3b2051b71f/versions/assets/image/uuid-498cb9b2-2d9e-40ef-9ed1-3cf51dc4a1d4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225344Z&X-Amz-Expires=604800&X-Amz-Signature=2bd20cec986696435e26af5fb27d677eff038f7294db0a7ca1a3194eb45da89c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Is Not Set**             | <p>- All text variables (including phone and email)</p> <p>- Number variables</p> <p>- List variables</p> | Match if there is no information contained in the variable.                                      |
       | ![Is Set icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/8c1019797a0482018682d52622c9e2fe56ddc5aef8925dc3e3db678c121c6869/versions/assets/image/uuid-dc59d677-9ded-d825-48e9-0fb7f5c48439.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225344Z&X-Amz-Expires=604800&X-Amz-Signature=049566074856c798d2f63e5a20922ae159fbf3203ef18bacc04f511e07be76ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Is Set**                     | <p>- All text variables (including phone and email)</p> <p>- Number variables</p> <p>- List variables</p> | Match if there is any information contained in the variable.                                     |
       | ![Greater Than icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/45636711dfe933087353da3923c6865b6816ea671ad6e9db4739aeea4c80a697/versions/assets/image/uuid-ea44ef37-6ef9-3b44-c1f6-86b4315c160c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225344Z&X-Amz-Expires=604800&X-Amz-Signature=fe79d3dc117ba0a634d7a24c7620badd3809a0e774db16a3c9a6790adc201eb1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Greater Than**         | <p>- Number variables</p>                                                                                 | Match if the information in the variable is greater than a specific value.                       |
       | ![Less Than icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/f2448b33a8931270e63ea8daab74e67ade1fdfdf1f8853529c2fb0a3e5abda55/versions/assets/image/uuid-6ad2273c-89e8-79b7-92ba-dd766b493b5f.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225344Z&X-Amz-Expires=604800&X-Amz-Signature=7fec39679acebf9bcec8c68c6521e3a61bf372319f6c314901aaa7035329518f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Less Than**               | <p>- Number variables</p> <p>- List variables</p>                                                         | Match if the information in the variable is less than a specific value.                          |
       | ![Is True icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/fcf3fe21099df957ee22609d5a5c211601d3e402fcc8402c12115f4680a692b0/versions/assets/image/uuid-b75658a2-623f-1317-139d-469254aca9cd.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225344Z&X-Amz-Expires=604800&X-Amz-Signature=28a5704c73a34c8568c14867a6099d4d4c22818633630b5b41cf0a276a93c047&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Is True**                   | <p>- Yes/No variables</p>                                                                                 | Match if the information in a variable is Yes (or True).                                         |
       | ![Is False icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/2b5c661e7e4445f1ea8f7736ee5b58b14f72283faf2dbd4f01220a26d621b238/versions/assets/image/uuid-83141cb5-fee0-686e-fb7e-5848842bd2af.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225344Z&X-Amz-Expires=604800&X-Amz-Signature=324d48c7747c603cdd8b1d7ef6d975965540d15c436a0a9214abe5eeb803e805&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Is False**                 | <p>- Yes/No variables</p>                                                                                 | Match if the information in a variable is No (or False).                                         |
       | ![Does Not Contain icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/2a459cf7a992abeb5cbdf8438f9f1be356bb5fcf915f55f7f1c2cdc3173b101d/versions/assets/image/uuid-a84f6c2f-dedb-70d5-7265-a0d7073bd683.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225344Z&X-Amz-Expires=604800&X-Amz-Signature=5f517024f0165d978d65a0e709c6ea18d5e3011da2903bfd29dbbf98977a1a25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Does Not Contain** | <p>- List variables</p>                                                                                   | Match if none of the selected items contains this value.                                         |
       | ![Is Equal To icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/7266dedcf2da1af5c496469379bd4fb68d5e65492c190e9567c75edbbbf7e260/versions/assets/image/uuid-ed7679a6-76c6-f8b3-d8cd-1323e8d98e0a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225344Z&X-Amz-Expires=604800&X-Amz-Signature=a25f10ee7283af7c424eeb94bc2accdc49c8e2391cd1aa6287f27cb1cbdf8f30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Is Equal To**           | <p>- List variables</p>                                                                                   | Match if the end user selected a particular number of options in a List Option block.            |
       | ![Is Greater Than icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/45636711dfe933087353da3923c6865b6816ea671ad6e9db4739aeea4c80a697/versions/assets/image/uuid-ea44ef37-6ef9-3b44-c1f6-86b4315c160c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225344Z&X-Amz-Expires=604800&X-Amz-Signature=fe79d3dc117ba0a634d7a24c7620badd3809a0e774db16a3c9a6790adc201eb1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Is Greater Than**   | <p>- List variables</p>                                                                                   | Match if the end user selected more than a particular number of options in a List Option block.  |
       | ![Is Less Than icon](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/f2448b33a8931270e63ea8daab74e67ade1fdfdf1f8853529c2fb0a3e5abda55/versions/assets/image/uuid-6ad2273c-89e8-79b7-92ba-dd766b493b5f.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225344Z&X-Amz-Expires=604800&X-Amz-Signature=7fec39679acebf9bcec8c68c6521e3a61bf372319f6c314901aaa7035329518f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject) **Is Less Than**         | <p>- List variables</p>                                                                                   | Match if the end user selected fewer than a particular number of options in a List Option block. |

       <li>
         In the 

         **Value**

          field, enter or select a value for the variable that you want to use to target end users.
       </li>

       <li>
         If required, add additional conditions.
       </li>

       * To add a new **top-level** condition, click **Add** <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/b0aa6bd9ade574c33763556b72bedb3fb7ba2384bf0c25ef6cc5401eab220757/versions/assets/image/button-add.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225344Z&X-Amz-Expires=604800&X-Amz-Signature=2186eaa73a21df86911e0c99ac4109d36f93280ad642c2c76bef899840a592f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" />.
         <p>If you're adding your first additional top-level condition, in the dropdown that appears, choose **And** or **Or** as the operator for all of your top-level conditions.</p>
       * To create or add to a **group** of conditions, click the **Add to group** icon <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/881a5902ee010bd99b16914b2ac663810ad93cade88c2fddc273b4c3bc508b28/versions/assets/image/icon-add.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225344Z&X-Amz-Expires=604800&X-Amz-Signature=2b13cc9e4936b76bdeaa57363a2ffdc4816db8f93856ad071d726601a111b5e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" /> beside a condition you want to include in the group.
         <p>If you're creating a group, in the dropdown that appears, choose **And** or **Or** as the operator for all of the conditions in that group.</p>
     </ol>

4. Click **Save**. Your AI Agent updates the availability for the selected articles, and lists the rules you set in the Availability column.

### Filter articles

Filter Knowledge articles by shared attributes such as language, activation state, source, or availability.

**To filter articles:**

1. On the Ada dashboard, go to **Config > AI AGENT > Knowledge**.
2. Under **Articles**, open the **Filter** drop-down. Select a [filter type](#filter-types): **Language**, **State**, **Source**, or **Availability**.
3. Choose an **Operator** (e.g., **Is**, **Is Not**).
4. Select a **Value** (e.g., "en" for Language, "Active" for State, a specific source, or an availability rule).
5. Click **Apply** to update the article list.

#### Filter types

Several filter types are available, each serving a specific use case:

* **State (Active/Inactive):** Filter to show only articles that are currently active or inactive. Useful for bulk activation/deactivation and auditing live content.

* **Source:** Filter articles by their source (e.g., Zendesk, Created in Ada, Imported Website) to manage or review content from specific integrations. This is helpful when multiple knowledge sources are connected and you want to isolate or troubleshoot content from a particular system.

* **Language:** Filter articles based on the language code. Useful for multilingual AI Agents to manage or review content in a specific language, or to ensure coverage across supported languages.

* **Availability:** Filter by custom rules (e.g., region, end user segment) defined in the article's rules field. This is useful when you need to quickly verify or edit articles that are available only for specific use cases.

These filters can be combined for granular control and bulk operations in the Ada dashboard.

## Related features

Explore related Knowledge capabilities:

* **[Article creation](/generative/docs/knowledge/content-ingestion/article-creation)**: Create Knowledge articles directly in Ada.
* **[Knowledge integrations](/generative/docs/knowledge/content-ingestion/knowledge-integration)**: Connect external knowledge bases like Zendesk, Salesforce, or Contentful.
* **[Web import](/generative/docs/knowledge/content-ingestion/web-import)**: Import content from public-facing websites.

<hr />

<p>
  Have any questions? Contact your Ada team, or email us at 

  <a href="mailto:help@ada.cx?subject=Help%20Docs%20inquiry" class="email">{"help@ada.cx"}</a>

  .
</p>