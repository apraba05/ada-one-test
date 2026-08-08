---
title: Knowledge integration
source_url: https://docs.ada.cx/docs/knowledge/content-ingestion/knowledge-integration
slug: knowledge--content-ingestion--knowledge-integration
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://docs.ada.cx/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.ada.cx/_mcp/server.

# Knowledge integration

## Overview

Ready to start serving knowledge to your end users? You can start by connecting your knowledge base with your AI Agent.

The method you use to connect your knowledge base depends on the tools you use to author and publish your knowledge base:

* If you use one of Ada's supported knowledge bases, you can follow the instructions below to use Ada's existing integrations.
* If you use different authoring tools, you can contact your Ada team, so they can use a custom integration that collects information in your knowledge base and uploads it into your AI Agent using the [Knowledge API](/generative/reference/knowledge/overview).

After you have uploaded your knowledge base content into your AI Agent, you can [manage your knowledge content](/generative/docs/knowledge/article-management) to include or exclude information from individual articles in your AI Agent's responses.

## Use cases

Knowledge integration enables your AI Agent to provide accurate, up-to-date responses based on your existing content.

* **Customer self-service**: Allow end users to get answers from your help center or FAQ content without waiting for a human agent.
* **Product documentation**: Enable your AI Agent to explain product features, troubleshoot issues, or guide end users through processes using your existing documentation.
* **Policy and procedure inquiries**: Answer questions about company policies, return procedures, or service terms directly from your knowledge base.
* **Multi-language support**: Serve end users in their preferred language using translated or localized knowledge base content.

## Capabilities & configuration

Knowledge integration supports multiple connection methods and content sources.

* **Supported integrations**: Connect directly to Zendesk, Salesforce, Contentful, and other supported knowledge base providers.
* **Knowledge API**: Use the [Knowledge API](/generative/reference/knowledge/overview) for custom integrations with unsupported authoring tools.
* **Multi-language content**: Ingest knowledge base content in any of Ada's supported languages. See [About multilingual support](/generative/docs/setup/languages/about-multilingual-support#supported-languages) for the full list.
* **Automatic sync**: Keep your AI Agent's knowledge current with automatic synchronization from connected sources.
* **Article management**: Include or exclude specific articles from your AI Agent's responses after ingestion.

## Quick start

Connect your knowledge base to your AI Agent in a few steps.

**To connect a knowledge base:**

On the Ada dashboard, go to **Config > AI AGENT > Knowledge**.

Click **Add source** and select your knowledge base provider (e.g., Zendesk, Salesforce, Contentful).

Enter the required connection details and authenticate.

Wait for the initial sync to complete.

Your AI Agent can now use your knowledge base content to generate responses. For detailed setup instructions, see [Connect your knowledge base](#zd-sf).

## Implementation & usage

Follow these steps to prepare, configure, and connect your knowledge base to your AI Agent.

### Prepare your knowledge base content\[#kb-prep]

Good knowledge base content is structured logically, so both humans and AIs can get appropriate context and understand the information it contains. Take a look at [Prepare your knowledge base as a source for AI generated content](/generative/docs/knowledge/core-workflows/knowledge-setup) to make sure you're following best practices on making a knowledge base usable for both human and AI readers.

### Multi-language support\[#kb-langs]

Your AI Agent can provide end users with content sourced from knowledge bases written in any of Ada's supported languages. For the full list of supported languages and how the AI Agent selects between them, see [About multilingual support](/generative/docs/setup/languages/about-multilingual-support#supported-languages).

Make sure that any languages in your knowledge base content are enabled in your language settings. For more information, see [Support multiple languages in the same AI Agent](/generative/docs/setup/languages/about-multilingual-support).

Here's how your AI Agent generates responses from non-English knowledge bases:

* When an end user asks your AI Agent a question, your AI Agent looks for content from articles written in the same language the end user asked in. If articles are available in that language, it uses them to generate responses in the end user's language.

  If it can't find content in the knowledge base for that language, it doesn't look in knowledge base content written in any other languages, and asks the end user for a different question.

* If an end user asks your AI Agent a question in any language you don't have knowledge base content written in, but the language is enabled in your language settings, your AI Agent automatically translates knowledge content written in English to generate responses. It never translates knowledge content from any other languages.

If you're adding content in a new language using one of the supported integrations, note that it can take up to 15 minutes for your articles to appear on the Knowledge page.

### Connect your knowledge base\[#zd-sf]

#### Before you begin\[#before]

Before connecting your knowledge base with your AI Agent, check to make sure you're set up for success. If you're using one of the knowledge bases listed below, make sure it meets the following criteria:

* Your knowledge base must be public-facing (i.e., not restricted behind a login).
* The URLs in your knowledge base must have the default structure that your knowledge base automatically provides. If your knowledge base URLs have been modified, after your AI Agent has scraped the contents of your knowledge base, the links won't work.
* Each article must be smaller than 5MB to get uploaded into your AI Agent.

Additionally, you should know that your AI Agent will sync automatically with your knowledge base every 15 minutes.

#### Import your knowledge content\[#zd-sf-connect]

Open an expander to learn how to connect your knowledge base, depending on the tool you're using.

### Import articles from Zendesk Guide

#### Learn more

If you plan to sync private articles to your AI Agent, you must authorize your Zendesk subdomain via Config > Apps > Zendesk before proceeding. See [Connect your Zendesk account](https://docs.ada.cx/generative/docs/handoffs/zendesk#connect-your-zendesk-account).

**To connect Ada to your Zendesk help center:**

1. On the Ada dashboard, go to **Config > Knowledge**, then click **Add source**.
2. Select **Zendesk** from the menu and the Zendesk landing page will appear.
3. Click **Connect** and the **Connect to Zendesk Guide** window will open.
4. Enter the connection details:
   * **Zendesk Subdomain:** The subdomain is the "accompany" in accompany.zendesk.com

     #### Find your Zendesk subdomain if you're using a custom domain

     <ol type="a">
       If your organization uses a custom domain name for your knowledge
       base URL and not the default Zendesk subdomain, you'll need to find
       your actual subdomain to complete the configuration.

       Zendesk has some tips for [finding your subdomain](https://support.zendesk.com/hc/en-us/articles/4409381383578-Where-can-I-find-my-Zendesk-subdomain-).
       Alternatively, you can also use Google's DNS lookup tool:

       <li>
         Go to the 

         [Google Dig tool](https://toolbox.googleapps.com/apps/dig/)

         .
       </li>

       <li>
         In the 

         **Name**

          field, enter your knowledge base's custom domain
         name. Include only the domain elements. Don't include the


         `https://`

         , or any pathways, slashes, etc.


         <p>**Example:** Enter `help.acustomdomain.com`, not
         `https://help.acustomdomain.com/`</p>
       </li>

       <li>
         In the list of options below the Name field, click 

         **CNAME**

         . In
         the results field that appears, under 

         **Target**

         , you'll find
         your full Zendesk URL containing your actual subdomain.
       </li>

       <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/1d1871cbf596be4fe102c9cf082489dec9b731dd0a3512c7a2d157fde5bbf486/versions/assets/image/uuid-eaa782cf-7fde-cabf-8678-040ddc86e914.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225303Z&X-Amz-Expires=604800&X-Amz-Signature=38050854038b235de6a983061252736c9d1bbfdf0692ef7c33acc99b9c66a871&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" />
     </ol>

   * **Article labels to import as tags:** Optionally, to make segmenting articles in Ada even easier, you can specify up to 25 [article labels](https://support.zendesk.com/hc/en-us/articles/4408835056154-Using-labels-on-your-help-center-articles) set on your Zendesk articles to be imported as [Tags](https://docs.ada.cx/generative/reference/knowledge/tags) in Ada. These values are case-sensitive and must exactly match the label on the Zendesk article to be associated in Ada.

   * **Include Private Articles:** Select this option to ingest articles only accessible to authenticated users.
     * **Zendesk Login Email:** Only articles accessible to this user will be ingested.
5. Click **Continue** and then click **Allow** to grant the integration access to your AI Agent.
6. If successful, a new Source will appear in the Knowledge section and your articles will begin syncing.

Once connected, it may take a few minutes for the initial sync to complete. The AI Agent won't use articles from the knowledge base until that sync is complete. After the initial sync, the integration syncs automatically every 15 minutes.

<h4>
  Add multiple Zendesk help centers
</h4>

To connect another Zendesk help center, add a new connection:

1. On the Ada dashboard, go to **Config** > **Knowledge**.
2. At the top of the page, click **Add connection**. The **Connect to Zendesk Guide** window will open.
3. Enter the required details and complete the setup.

<h4>
  Disconnect your Zendesk help center
</h4>

Remove the Zendesk help center connection when you no longer need it.

To disconnect a Zendesk help center from your AI Agent:

1. On the Ada dashboard, go to **Config > Knowledge**, then select the **Sources** tab.
2. Beside the knowledge source, click **Settings**. The Zendesk landing page will open, showing all of your connected Zendesk help centers.
3. Click on the three dots **⋮** next to your installation and select **Delete Connection**.

Once deleted, the Source and all associated articles and tags are removed from the AI Agent's Knowledge section.

<h4>
  Migrate to the new Zendesk Guide integration
</h4>

If you connected your Zendesk help center before March 25, 2026, the existing integration will continue to work. Migration is only necessary to support:

* Syncing **article tags** (imported from Zendesk article labels) in Ada
* Importing **private articles** that are accessible only to authenticated users
* Connecting **multiple Zendesk help centers** to a single AI Agent

Any coaching applied to existing synced Zendesk articles, and availability rules set on those articles in Ada, will be migrated automatically to **matching** articles in the new Zendesk source.

The new source uses the Zendesk article ID and locale for identification. Some articles may not be automatically matched, if the stored locale for the existing article in Ada does not match the current Zendesk locale. In these cases, coaching and availability rules will need to be manually reconfigured on the newly synced articles after migration is complete. Reporting references to those articles will also not carry over.

**To migrate to the new integration:**

1. If you plan to sync private articles to your AI Agent, you must authorize your Zendesk subdomain via Config > Apps > Zendesk before proceeding. See [Connect your Zendesk account](https://docs.ada.cx/generative/docs/handoffs/zendesk#connect-your-zendesk-account).
2. Reconnect using the new integration. See [Import articles from Zendesk Guide](#import-articles-from-zendesk-guide) above.
3. Allow the initial sync to complete, then confirm that articles and tags appear as expected under the new source in **Config > Knowledge**, and that coaching and availability rules have been applied to the articles.
4. Once the new connection has synced, remove the old source: on the Ada dashboard, go to **Config > Knowledge > Sources**, click **Settings** beside the existing connection, then select **Disconnect Zendesk Guide**.

### Import articles from Salesforce Knowledge

#### Learn more

Salesforce Knowledge integrates with your AI Agent using the Client Credentials OAuth flow. Before connecting, configure your Salesforce instance and create an External Client App.

**To prepare your Salesforce instance:**

1. Confirm that **Salesforce Knowledge** is enabled in your Salesforce org. To enable Knowledge, go to **Setup > Feature Settings > Service > Knowledge Settings** and enable Knowledge.
2. Create a new **External Client App** with the **Client Credentials** OAuth grant type enabled. Follow Salesforce's documentation on [setting up an External Client App for the Client Credentials Flow](https://help.salesforce.com/s/articleView?id=xcloud.meta_configure_client_credentials_flow_for_external_client_apps.htm\&type=5) to complete this step. When configuring the External Client App, ensure the Run As user has access to the articles to be synced.
3. Once the External Client App is created, copy the **Consumer Key** and **Consumer Secret** from the app's API settings — these are required when connecting in the Ada dashboard.

**To connect an AI Agent to Salesforce Knowledge:**

1. On the Ada dashboard, go to **Config > Knowledge**, then click **Add source**.
2. Select **Salesforce Knowledge** from the menu.
   The Salesforce Knowledge landing page appears.
3. Click **Connect**.
   The **Connect to Salesforce Knowledge** window opens.
4. Enter the connection details:
   * **Instance URL** — The Salesforce instance URL (for example, `https://yourorg.my.salesforce.com`).
   * **Consumer Key** — The OAuth Client ID from the External Client App.
   * **Consumer Secret** — The OAuth Client Secret from the External Client App.
   * **Include articles from** — The Salesforce channel visibilities to include in the sync: Public Knowledge Base, Customer Portal, Partner Portal, and Internal App.
   * **Salesforce Knowledge version** — Select **Lightning** (default) or **Classic**.
   * **Help Center URL** *(optional)* — The base URL of the Salesforce Help Center (for example, `https://help.yourorg.com`). When provided, this URL is used to construct article URLs for articles synced to the AI Agent. If left blank, article URLs will not be set on synced articles.
   * **Custom Content Field API Name** *(optional)* — API name of a custom field to use for article content instead of the default rich and long text fields.
   * **Knowledge Article Type API Name** *(required if Classic is selected)* — API name of the custom knowledge article type (for example, `FAQ__kav`). This field appears only when **Classic** is selected.
   * **Filter by Data Category** *(optional)* — Enable to filter synced articles by Salesforce data category. When enabled, a **Data Category Filter SOSL** field appears — enter the SOSL WHERE clause for the data category filter.
   * **Filter by Locale** *(optional)* — Enable to limit synced articles to specific locales. When enabled, a **Salesforce Language Code / Locale** field appears — add the locales to include (for example, `en_US`, `fr`).
5. Click **Continue** and then click **Allow** to grant the integration access to your AI Agent.
   Ada validates the credentials directly with Salesforce. If successful, a new Source appears in the Knowledge section and articles begin syncing.

Once connected, it may take a few minutes for the initial sync to complete. The AI Agent won't use articles from the knowledge base until that sync is complete. After the initial sync, Salesforce Knowledge syncs automatically every 15 minutes.

**Data categories sync as tags:** Data categories set on articles in Salesforce are automatically added as tags in Ada. These tags can be used to filter and organize content within the AI Agent.

<h3>
  Add multiple Salesforce Knowledge connections
</h3>

Connect additional Salesforce Knowledge instances to expand your knowledge base.

**To connect another Salesforce Knowledge instance:**

1. On the Ada dashboard, go to **Config > Knowledge**.
2. At the top of the page, click **Add Connection**.
   The Connect to Salesforce Knowledge window opens.
3. Enter the required details and complete the setup.

<h3>
  Disconnect Salesforce Knowledge
</h3>

Remove the Salesforce Knowledge integration when you no longer need it.

**To disconnect Salesforce Knowledge from Ada:**

1. On the Ada dashboard, go to **Config > Knowledge**, then select the **Sources** tab.
2. Beside the knowledge base, click **Settings**.
   The Salesforce Knowledge landing page opens, showing all connected instances.
3. Click **⋮** next to the installation and select **Delete Connection**.

Once deleted, the Source and all associated articles and tags are removed from the AI Agent's Knowledge section.

<h3>
  Migrate to the new Salesforce Knowledge integration
</h3>

If you connected your Salesforce knowledge base before March 17, 2026, the existing integration will continue to work. Migration is only necessary to support:

* Connecting **multiple Salesforce Help Centers**
* **Advanced article filtering** (by data category or locale)
* Syncing **data categories as tags** in Ada

Any coaching applied to Salesforce Knowledge articles and availability rules set on those articles in Ada will not be migrated automatically. These must be reconfigured on the newly synced articles after migration is complete. Reporting references to those articles will also not carry over.

**To migrate to the new integration:**

1. In the Salesforce org, create a new **External Client App** with the **Client Credentials** grant type enabled. See the prerequisites above for detailed steps.
2. Reconnect using the new integration. See [Import articles from Salesforce Knowledge](#import-articles-from-salesforce-knowledge) above.
3. Articles re-sync automatically once the new connection is established.
4. Reconfigure any coaching and availability rules that were applied to articles in the previous Salesforce Knowledge source.
5. Once the new connection has synced, remove the old source: on the Ada dashboard, go to **Config > Knowledge > Sources**, click **Settings** beside the existing connection, then click **Disconnect Salesforce Knowledge**.

### Import articles from Contentful

#### Learn more

To connect Ada to your Contentful knowledge base:

1. On the **Ada dashboard**, go to **Config > AI AGENT > Knowledge**, then click **Add source**.

2. Select **Contentful** from the menu and the Contentful landing page will appear.

3. Click **Connect**. The Contentful window opens.

4. Provide the following details:

   * **Connection Name**: Enter a unique name for this connection.

   * **Contentful Space ID**: Enter the unique ID of your Contentful space.

     To find your **Space ID** in Contentful, check the **URL** in your browser or navigate to **Settings** (⚙️ in the top-right corner) > **General Settings**, then copy your **Space ID**.

   * **Top-Level Content Types**: Specify which content types should be imported as top-level articles.

     To find your **Content Type** in Contentful, navigate to **🔧 Content model**, click on the **Name** of the content type you are interested in, and select **Copy ID** at the top of the page.

   * **Excluded Content Types**: List any content types that should not be imported.

   * **Contentful Delivery API Token**: Required to retrieve published content.

   * **Contentful Preview API Token**: Used by the webhook to fetch top-level content, including references to unpublished or deleted content.

     Both the **Delivery API Token** and **Preview API Token** can be found in **⚙️ Settings** > **API Keys**.

   * **Content Languages** – Enter the language codes for the content you want to import.\
     *Example:* For English, enter `en-us` and for French, enter `fr-ca`.

   * **Include Tags**: Select if you want to import and use Contentful tags.

     Selecting **Include Tags** imports all tags in your Contentful instance, whether they are related to your top-level content or not.

5. Click **Connect**. A window will appear, requesting access to Contentful for your AI Agent. Click **Allow**.

6. If successful, a new **Source** appears in the **Knowledge** section, and your articles will begin syncing.

<h3>
  Update your content in real-time
</h3>

Keep your Contentful knowledge base in sync with Ada by configuring a webhook.

**To configure a Contentful webhook:**

1. In Contentful, navigate to: **Settings** (⚙️ in the top-right corner) > **Webhooks**.
2. Click **Add a new Webhook**.
3. Name the webhook (e.g. Ada Knowledge Sync).
4. Make sure to set the **URL** to the following and ensure the **HTTP method** is set to **POST**.

   * **AI Agents in the US region:**
     ```
     https://solutions.ada.support/kb_apps/contentful/webhook/update_articles
     ```
   * **AI Agents in the EU region:**
     ```
     https://solutions.eu.ada.support/kb_apps/contentful/webhook/update_articles
     ```
   * **AI Agents in the CA (Maple) region:**
     ```
     https://solutions.maple.ada.support/kb_apps/contentful/webhook/update_articles
     ```
5. Under **Triggers**, find the **Entry** row in the table and check **Publish** and **Unpublish**.
6. Under **Headers**, add a custom header with the following:
   * **Key:** `X-Ada-Authorization`
   * **Value:** Your **Installation ID**. Follow these steps to locate it.

     <ol type="i">
       <li>
         On the Ada dashboard, go to 

         **Config > AI AGENT > Knowledge**

         , then go to the 

         **Sources**

          tab.
       </li>

       <li>
         Beside your knowledge base setting, click 

         **Settings**

         . You are directed to the Contentful landing page showing your Connections.
       </li>

       <li>
         Click the three dots 

         **⋮**

          next to your installation and select 

         **Settings**

         .
       </li>

       <li>
         In the Connect to Contentful window, find the last ID value in the URL:
       </li>

       ```
       <your-ai-agent-handle>/platform/integrations/67993c61d8dd73984a6c7297/connections/<your_installation_id>/edit
       ```

       <li>
         Copy your 

         **Installation ID**

          in the webhook 

         **Headers**

         .
       </li>

       <li>
         Click 

         **Save**

          to complete the setup.
       </li>
     </ol>

     You can add multiple installation IDs under a single webhook using a comma separator (e.g., `id_1, id_2`).

<h3>
  Add more Contentful spaces
</h3>

If you need to connect another Contentful space, add a new connection and set up a webhook for that space.

1. On the **Ada dashboard**, go to **Config > AI AGENT > Knowledge**.
2. At the top of the page, click **Add Connection**. The Connect to Contentful window appears.
3. Enter the required details and complete the setup.

Each Contentful space requires its own webhook. However, if you have multiple installations under the same space, you can use one webhook and list all **Installation IDs** in the **X-Ada-Authorization** header.

<h3>
  Disconnect your Contentful knowledge base
</h3>

Remove the Contentful integration when you no longer need it.

**To disconnect Contentful from Ada:**

1. On the Ada dashboard, go to **Config > AI AGENT > Knowledge**, then select the **Sources** tab.
2. Beside your knowledge base setting, click **Settings** to open the Contentful landing page showing your Connections.
3. Click the three dots **⋮** next to your installation and select **Delete Connection**.
4. Once deleted, the **Source** and associated articles will be removed from Ada’s Knowledge section.

### Import articles from Dixa Knowledge

#### Learn more

To connect Ada to your Dixa knowledge base:

1. On the **Ada dashboard**, go to **Config > AI AGENT > Knowledge**, then click **Add source**.

2. Select **Dixa** from the menu. The Dixa landing page will appear.

3. Click **Connect**. The Connect to Dixa window will open.

4. Provide the following details:

   * **Collection Name**: Enter a unique name for this connection.

   * **Dixa Collection ID**: Enter the unique ID of your Dixa Knowledge collection.

     To find your <strong>Collection ID</strong>, go to <strong>Knowledge > Select your Collection</strong> in Dixa and copy the ID from the <strong>URL</strong>:<br />
     <code>\<your-dixa-domain>/knowledge/collection/\<your\_dixa\_collection\_id></code>

   * **Dixa API JWT Token**: Type the Dixa API JWT token, found in <strong>⚙️ Settings > Integrations > API tokens</strong>.

     You can either copy an existing token or generate a new one by clicking <strong>Add API Token</strong> in the top right.

   * **Languages** (Optional): Provide the language codes for the specific content that you want to import. Leave blank to sync all available languages.<br />
     <em>Example:</em> <code>en</code> for English, <code>fr</code> for French.

     Use lowercase only. Uppercase language codes like <code>EN</code> or <code>FR</code> will not work.

   * **Dixa Help Centre Subdomain** (Optional): If articles belong to multiple help centers, specify the subdomain to use for articles.

5. Click **Continue**. A window will prompt you to authorize access to Dixa for your AI Agent. Click **Allow**.

6. If successful, a new **Source** will appear in the **Knowledge** section, and your articles will begin syncing.

Once connected, it may take a few minutes for your AI Agent to complete the
initial sync with your knowledge base. Your AI Agent won't use articles
from your knowledge base until that sync is complete. After the initial sync, your Dixa knowledge base will continue to sync automatically every six hours.

<h3>
  Add Multiple Dixa Knowledge Collections
</h3>

Connect additional Dixa Knowledge collections to expand your knowledge base.

**To connect additional Dixa Knowledge collections:**

1. On the **Ada dashboard**, go to **Config > AI AGENT > Knowledge**.
2. Click **Add Connection** at the top of the page.
3. Complete the **Connect to Dixa** form with the new collection details.

Each Dixa Knowledge collection requires its own connection setup.

<h3>
  Disconnect Dixa Knowledge
</h3>

Remove the Dixa integration when you no longer need it.

**To disconnect Dixa Knowledge from Ada:**

1. On the Ada dashboard, go to **Config > AI AGENT > Knowledge**, then select the **Sources** tab.
2. Click **Settings** beside the Dixa connection to open its landing page.
3. Click the three dots **⋮** next to the installation and select **Delete Connection**.
4. Once deleted, the **Source** and all associated articles will be removed from Ada’s Knowledge section.

### Import articles from Gladly

#### Learn more

To connect Ada to your Gladly knowledge base:

1. On the **Ada dashboard**, go to **Config > AI AGENT > Knowledge**, then click **Add source**.

2. Select **Gladly** from the menu. The Gladly landing page will appear.

3. Click **Connect**. The Connect to Gladly window will open.

4. Enter the following details:
   * **Connection Name**: Enter a unique name to identify this connection.\
     *Example:* `Gladly US Help Center`

   * **Filter Type**: Select whether to import articles from a **Help Center** or an **Audience**.

   * **Filter ID**: Type the ID based on your selected filter type.

     For <strong>Help Center</strong>, this is the <code>brandId</code> from the embed script. Find it in <strong>Settings → Help Center → Configuration</strong>, then select <strong>Embed</strong> in the dropdown menu for the help center you’d like to ingest into your AI agent.<br /><br />
     For <strong>Audience</strong>, go to <strong>Settings → Help Center → Audiences</strong>, click the edit icon, and copy the ID from the URL:<br />
     <code>https\://\<your-gladly-domain>/admin/audiences/\<ID></code>

   * **Language**: Type the language code used in Gladly.\
     *Example:* `en-us` for English (United States), `fr` for French

     If your Gladly instance supports multiple languages, ensure your Ada team has enabled multi-lingual support in your AI agent and submit this form once per language you'd like to ingest.

   * **Gladly API URL**: Type the <code>api</code> value found in the embed script.

     Find it in <strong>Settings → Help Center → Configuration</strong>, then select <strong>Embed</strong> in the dropdown menu for the help center you’d like to ingest into your AI agent.

   * **Gladly API Token**: Type the token found in **Settings > API Tokens**.

     You can either copy an existing token or generate a new one by clicking <strong>Add API Token</strong> in the top right.

   * **Gladly Username**: Specify the user name of the Gladly user who created the API Token.

   * **Gladly Help Center URL** (Optional): If your Help Center is embedded on a public domain, enter the full URL.\
     *Example:* `https://support.example.com`\
     This allows your AI Agent to display clickable links to articles in conversations.

5. Click **Continue**. A window will prompt you to authorize access to Gladly for your AI Agent. Click **Allow**.

6. If successful, a new **Source** will appear in the **Knowledge** section, and your articles will begin syncing.

Once connected, it may take a few minutes for your AI Agent to complete the initial sync with your knowledge base. Your AI Agent won't use articles from your knowledge base until that sync is complete.

<h3>
  Article sync frequency and limitations
</h3>

* Articles are currently synced from Gladly to Ada every six hours.
* Only publicly available, published answers are ingested from your Gladly Help Center.
* Ada will ingest up to the first **1000** public answers, sorted alphabetically by name. This is a Gladly API limitation. Articles beyond the first 1000 alphabetically will not be available to your AI Agent.

<h3>
  Add multiple Gladly sources
</h3>

Connect additional Gladly Help Centers or Audiences to expand your knowledge base.

**To connect additional Gladly sources:**

1. On the **Ada dashboard**, go to **Config > AI AGENT > Knowledge**, then click **Add Connection** at the top of the page.

2. Complete the **Connect to Gladly** form with the new source details.

Each Gladly source requires its own connection setup.

<h3>
  Disconnect Gladly
</h3>

Remove the Gladly integration when you no longer need it.

**To disconnect Gladly from Ada:**

1. On the **Ada dashboard**, go to **Config > AI AGENT > Knowledge**, then select the **Sources** tab.
2. Click **Settings** beside the Gladly connection to open its landing page.
3. Click the three dots **⋮** next to the installation and select **Delete Connection**.
   Once deleted, the **Source** and all associated articles will be removed from Ada's Knowledge section.

### Import articles from ServiceNow Knowledge Management

#### Learn more

To connect Ada to your ServiceNow knowledge base:

1. On the **Ada dashboard**, go to **Config > AI AGENT > Knowledge**, then click **Add source**.
2. Select **ServiceNow** from the menu. The ServiceNow landing page will appear.
3. Click **Connect**. The Connect to ServiceNow window will open.
4. Enter the following details:
   * **ServiceNow Instance Subdomain**: The subdomain of your ServiceNow instance.

   * **OAuth Client ID**: The client ID of an OAuth application in your ServiceNow instance.

   * **OAuth Client Secret**: The corresponding client secret of an OAuth application in your ServiceNow instance.

     Your Client ID and Secret must be for an OAuth application with the client credentials grant type. To make sure you have the right setup, follow <a href="https://www.servicenow.com/docs/bundle/zurich-platform-security/page/integrate/authentication/concept/client-credentials.html">the client credentials instructions</a> shared by ServiceNow.

   * **Knowledge Base Name**: A friendly name to refer to your knowledge base in Ada.

   * **Knowledge Base ID**: The `sys_id` of the knowledge base in your ServiceNow instance.

   * **Public Help Center Base URL** (Optional): The base URL of your publicly accessible knowledge base. If provided, this is used to construct article URLs.
     *Example:* `https://help.example.com/csp?id=csp_kb_article_view`
5. Click **Connect**. A window will prompt you to authorize access to ServiceNow for your AI Agent. Click **Allow**.
6. If successful, a new **Source** will appear in the **Knowledge** section, and your articles will begin syncing.

Once connected, it may take a few minutes for your AI Agent to complete the initial sync with your knowledge base. Your AI Agent won't use articles from your knowledge base until that sync is complete. After the initial sync, your ServiceNow knowledge base will continue to sync automatically every 15 minutes.

<h3>
  Add multiple ServiceNow knowledge bases
</h3>

Connect additional ServiceNow knowledge bases to expand your knowledge base.

**To connect additional ServiceNow knowledge bases:**

1. On the **Ada dashboard**, go to **Config > AI AGENT > Knowledge**.
2. Click **Add Connection** at the top of the page.
3. Complete the **Connect to ServiceNow** form with the new knowledge base details.

Each ServiceNow knowledge base requires its own connection setup.

<h3>
  Disconnect ServiceNow
</h3>

Remove the ServiceNow integration when you no longer need it.

**To disconnect ServiceNow from Ada:**

1. On the Ada dashboard, go to **Config > AI AGENT > Knowledge**, then select the **Sources** tab.
2. Click **Settings** beside the ServiceNow connection to open its landing page.
3. Click the three dots **⋮** next to the installation and select **Delete Connection**.
   Once deleted, the **Source** and all associated articles will be removed from Ada's Knowledge section.

### Import articles from Helpjuice

#### Learn more

To connect Ada to your Helpjuice knowledge base:

1. On the **Ada dashboard**, go to **Config > AI AGENT > Knowledge**, then click **Add source**.
2. Select **Helpjuice** from the menu. The Helpjuice landing page will appear.
3. Click **Connect**.
4. In the Helpjuice window that opens, enter the following details:
   * **Subdomain**: Your Helpjuice subdomain in the URL (e.g. `yourcompany` in `yourcompany.helpjuice.com`).

   * **API Key**: Your Helpjuice API token, that you created under **Settings > API Credentials**. Select **Require token for API?** and copy the **Private Key** before selecting **Save Changes**.

     <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/933e95f937dabbf0c14ab74c39cd58886626de250af1eeda97ba214b142dd512/versions/assets/image/helpjuice-api-creds-settings.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225303Z&X-Amz-Expires=604800&X-Amz-Signature=d737af42842c316abf2349d736eb6d58835c438053adb657399b4851f0d8f514&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" />

     <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/732c993ef60e113a92c96eb483005bfe6fd83c563ee15da4f4a58916b5d1d9a0/versions/assets/image/helpjuice-api-key-page.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225303Z&X-Amz-Expires=604800&X-Amz-Signature=31d7a01ab20e43adeca5f376db94d98652cbc443b0138553e989ee126143938f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" />

   * **Localization** (optional): Enter specific language codes to sync (e.g., `en_US, fr_FR, de_DE`). Language will default to `en_US` if not specified.

     Codes are found by selecting the language on the left side of the Helpjuice dashboard, or by going into <strong>Settings > Languages & Translations</strong>.

     <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/fd9ce76a72fa2793b489cf05ff75441ca2f696eb1ba001cd09eb9d7f7dc26819/versions/assets/image/helpjuice-finding-localization-code.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225303Z&X-Amz-Expires=604800&X-Amz-Signature=a091b1e2c242dae9a676556afd22f040449d7ca65974c1ba1fe6ad7cd730a8c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" />

   * **Categories to skip** (optional): Add a list of categories to exclude from the sync. Articles in all other categories—including uncategorized ones—will be synced.

   * **Categories to include** (optional): Add a list of categories to sync exclusively. If this list is set, articles from all other categories will be skipped.

     If a category is incorrectly added to both lists, it will be skipped. Use the category codename as it appears in the Slug URL (e.g. <code>[https://yourcompany.helpjuice.com/codename-here](https://yourcompany.helpjuice.com/codename-here)</code>):

     <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/ada.docs.buildwithfern.com/cd7f14fbeed6903b8cc0803cbf98f1804c5dda4727b6da1b779959f3e0a2d0d7/versions/assets/image/helpjuice-finding-categorycodename.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T225303Z&X-Amz-Expires=604800&X-Amz-Signature=e2ed1961a8ff83181ecfc18c0b5dd05437cbd6f50e544944a0ad025f9a41eeb2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" />

   * **Include Private Articles:** Select this option to sync articles that have Private accessibility enabled.

   * **Include Internal Articles:** Select this option to sync articles that have Internal accessibility enabled.
5. Click **Connect**. A window will appear requesting access to Helpjuice for your AI Agent. Click **Allow**.
6. If successful, a new **Source** will appear in the **Knowledge** section, and your articles will begin syncing.

Once connected, it may take a few minutes for your AI Agent to complete the initial sync with your knowledge base. Your AI Agent won't use articles from your knowledge base until that sync is complete. After the initial sync, your Helpjuice will continue to sync automatically every two hours.

<h3>
  Add Multiple Helpjuice Knowledge Bases
</h3>

If you need to connect another Helpjuice knowledge base, add a new connection:

1. On the **Ada dashboard**, go to **Config > AI AGENT > Knowledge**.
2. At the top of the page, click **Add Connection**. The Connect to Helpjuice window will open.
3. Enter the required details and complete the setup.

<h3>
  Disconnect Helpjuice Knowledge Base
</h3>

Remove the Helpjuice integration when you no longer need it.

**To disconnect Helpjuice from Ada:**

1. On the Ada dashboard, go to **Config > AI AGENT > Knowledge**, then select the **Sources** tab.
2. Find your Helpjuice knowledge base in the list of connections and click **Settings** to open the Helpjuice landing page showing your connected Helpjuice Knowledge Base.
3. Click on the three dots **⋮** next to your installation and select **Delete Connection**.
4. Once deleted, the **Source** and associated articles will be removed from Ada's Knowledge section.

### Import articles from Microsoft Dynamics

#### Learn more

**To connect Ada to your Microsoft Dynamics knowledge base:**

1. On the **Ada dashboard**, go to **Config > AI AGENT > Knowledge**, then click **Add source**.
2. Select **Microsoft Dynamics** from the menu.
   The Microsoft Dynamics landing page will appear.
3. Click **Connect**.
   The Connect to Microsoft Dynamics window will open.
4. Enter the values in the window with the following details:
   * **Organization Domain and Region:** The subdomain and region of your Dynamics 365 environment. This is the "org1234.crm" portion of org1234.crm.dynamics.com.

   * **Tenant ID:** Your Azure Active Directory tenant ID. You can find this in the Azure Portal under **Azure Active Directory > Overview**.

   * **Client ID:** The Application (client) ID from your Azure app registration. This app registration must have API permissions for Dynamics 365.

   * **Client Secret:** The client secret generated for your Azure app registration. You can create one in the Azure Portal under **App registrations > your app > Certificates & secrets**.

     We recommend creating a dedicated Azure app registration for the Ada integration with the minimum required API permissions for Dynamics 365 (user\_impersonation scope on the Dynamics 365 API).

   * **Languages (Optional):** Optionally, specify which languages to sync. By default, only articles in **English - United States** are synced. The values must exactly match the language locale names configured in your Dynamics 365 environment (e.g., "English - United States", "French - Canada"). You can find the available language locale names in Dynamics 365 under **Settings > Languages**.

   * **Base URL (Optional):** Optionally, provide a base URL for generating article links (e.g., [https://your-portal.powerappsportals.com](https://your-portal.powerappsportals.com)). If set, each synced article in Ada will include a clickable link to the original article in your Dynamics portal.
5. Click **Connect**.
   A window will appear requesting access to Microsoft Dynamics for your AI Agent. Click **Allow**.
6. If successful, a new **Source** will appear in the **Knowledge** section, and your articles will begin syncing.

Only **published** articles in the configured languages are synced. Once connected, it may take a few minutes for your AI Agent to complete the initial sync with your knowledge base. Your AI Agent won't use articles from your knowledge base until that sync is complete.

After the initial sync, your Microsoft Dynamics will continue to sync automatically every 15 minutes.

<h3>
  Add multiple Microsoft Dynamics connections
</h3>

Connect additional Microsoft Dynamics environments to expand your Knowledge base.

**To connect additional Microsoft Dynamics environments:**

1. On the **Ada dashboard**, go to **Config > AI AGENT > Knowledge**.
2. At the top of the page, click **Add Connection**.
   The Connect to Microsoft Dynamics window will open.
3. Enter the required details and complete the setup.

<h3>
  Disconnect Microsoft Dynamics
</h3>

Remove the Microsoft Dynamics integration when you no longer need it.

**To disconnect Microsoft Dynamics from Ada:**

1. On the Ada dashboard, go to **Config > AI AGENT > Knowledge**, then select the **Sources** tab.
2. Beside your knowledge base setting, click **Settings** to open the Microsoft Dynamics landing page showing your connected Microsoft Dynamics Knowledge Bases.
3. Click on the three dots **⋮** next to your installation and select **Delete Connection**.
4. Once deleted, the **Source** and associated articles and tags will be removed from Ada's Knowledge section.

### Import articles from other integrations

#### Learn more

If you have created additional knowledge integrations beyond Zendesk and Salesforce, they will also be available for import. Simply select the integration from the **Add source** list to import articles from that source.

Developers can create custom knowledge integrations with Ada. To learn more, review our [Integration documentation](https://developers.ada.cx/reference/integrations/overview).

#### Manage your knowledge base connection\[#kb-manage]

After you connect your knowledge base with your AI Agent, you can go back to edit your connection settings.

**To edit your connection settings:**

1. On the Ada dashboard, go to **Config > AI AGENT > Knowledge**, then go to the **External sources** tab.
2. Beside your knowledge base setting, click **Settings**. There, you can modify your knowledge base connection settings, or disconnect it.

### Connect through the Knowledge API\[#kb-api]

To use a knowledge base that you maintain with tools other than the supported integrations, you have to use a custom integration that works with the tools you use to extract your data and upload it into the Knowledge API. Depending on your integration, the frequency of how often your AI Agent gets updated content from your knowledge base may vary.

To learn more about the Knowledge API, including limits on article and request size, see [Knowledge API](/generative/reference/knowledge/overview) at Ada's developer documentation.

## Related features

* [Web import](/generative/docs/knowledge/content-ingestion/web-import): Import content directly from publicly available websites.
* [Article creation](/generative/docs/knowledge/content-ingestion/article-creation): Create and manage knowledge articles directly in the Ada dashboard.

<hr />

<p>
  Have any questions? Contact your Ada team, or email us at 

  <a href="mailto:help@ada.cx?subject=Help%20Docs%20inquiry" class="email">{"help@ada.cx"}</a>

  .
</p>