---
title: Knowledge setup
source_url: https://docs.ada.cx/docs/knowledge/core-workflows/knowledge-setup
slug: knowledge--core-workflows--knowledge-setup
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://docs.ada.cx/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.ada.cx/_mcp/server.

# Knowledge setup

## Overview

Getting ready to create automatically generated content from your
knowledge base for the first time? Or maybe you're just looking to tune
up your knowledge base? Follow these principles to make the information
in your knowledge base easy for your AI Agent to parse, which will improve
your AI Agent's chances of serving up relevant and helpful information to
your customers.

## Content structure\[#UUID-9d2e534b-9f12-97fa-a9ec-cf438f036d0e\_section-idm4610629762313633762904455055]

When you're maintaining a knowledge base, it can be easy to organize
information in a way that makes sense to you, but not to people who
aren't familiar with the information in it already. If you watch a new
customer trying to navigate your knowledge base, you'll almost certainly be
surprised at what they do! If you're like most people who maintain
knowledge bases, you probably aren't a beginner, which means that you
likely aren't your own target audience.

So how can you make sure your knowledge base is useful for customers, and
what does that have to do with AI? The answer here comes down to using
**titles** and **headings**. These
are referred to as **signposts** collectively, because they act as
signposts for both humans and AI, to indicate how likely it is that a
customer is getting closer to the information they want to get to in your
knowledge base. Additionally, when Ada ingests your knowledge base
content, it saves the topic title as context for
each chunk of information it splits your knowledge base into. When
information has proper context, it's less likely that your AI Agent will
serve irrelevant information to customers.

* **Categorize your information into groups that don't overlap.** That
  way, both your human customers and your AI are less likely to make a wrong
  turn and find information that isn't relevant to what they're looking
  for.

* **Make every signpost relevant to all of the information under it.**
  If there's information under a heading that isn't relevant to that
  heading, both customers and AI might have trouble finding that
  information. Similarly, if the heading is confusing or implies that
  it's followed by information that isn't actually there, it makes it
  harder for customers and AI to navigate your knowledge base.

* **Always organize information from most broad to most specific.** It
  should be easy for customers to figure out whether they're getting closer
  to the information they're looking for by following your signposts.

* **Make your signposts descriptive.**

  * Orient signposts around customer objectives. Most likely, customers are
    coming to your knowledge base or AI Agent looking for help with a
    specific task, so making it clear which articles are about which
    tasks is very helpful.

    As a best practice, use verbs in your signposts to make it easier
    for customers to find the actions they want to perform.

  * To help people and AI scan your content more easily, put important
    verbs and vocabulary closer to the front of your signposts than to
    the end.

  * Wherever you can, avoid mentioning concepts or terminology that new
    customers might not be familiar with yet. Unfamiliar wording makes it
    harder for signposts to do their job, because both people and LLMs
    can find them confusing.

  * Try to make it easy for customers to figure out whether they're the
    intended audience for an article just from reading the signposts. No
    customer wants to waste their time opening articles just to find that
    they're not relevant, or reading irrelevant responses.

* **Use proper HTML structure to create signposts.** It might look just
  as good if you highlight some text, increase the size, and make it
  bold, but an AI model might struggle to recognize that that formatting
  is supposed to indicate a heading. Instead, use the appropriate `<h1>`
  tags, and so on. When you do, your formatting will be much more
  consistent, and AI can pick out the hierarchy your information is in.
  Additionally, your customers who have visual impairments can navigate
  properly formatted content more easily, because their assistive
  technology (e.g., screen readers) are programmed to parse HTML.

* **Don't assume that customers are going to read your knowledge base in
  order.** Customers might find an article, or even a section of an article,
  via a search engine, and might get frustrated if the information they
  see requires a lot of context they don't have. Likewise, if your AI Agent
  sends a customer information without context, that can be a frustrating
  chat experience too. Make sure you lay some groundwork in your more
  advanced articles so all of your customers can go back and get more
  information if they need to.

The study of organizing information to aid customer navigation is called
**information architecture**. If you're interested in more information,
including resources on how to perform tests to see how your knowledge
base organization works for new customers, see [Information Architecture: Study Guide](https://www.nngroup.com/articles/ia-study-guide/) at the
Nielsen Norman Group's website.

### Write standalone content\[#UUID-9d2e534b-9f12-97fa-a9ec-cf438f036d0e\_section-idm4585938791220833916926910122]

When an AI ingests the content in your knowledge base, it breaks the
information up into chunks. Then, when customers ask your AI Agent questions,
your AI Agent searches for chunks that have relevant meanings and uses them
to create responses. Here are some ways you can ensure each chunk makes
sense on its own:

* **Provide information in full sentences.** Because your AI Agent puts
  information into chunks, the best way to make sure your information
  has full context is to provide full sentences.

  For example, let's say your knowledge base contains a FAQ, and one of
  your questions is "Can I pay by credit card?" Instead of a simple
  "Yes," which isn't helpful on its own, phrase the answer as "Yes, you
  can pay by credit card."

* **Avoid references to other locations in your knowledge base.** When
  customers are reading your knowledge base content in the context of a
  AI Agent, they won't have context for references like "As you saw in our
  last example." Avoid these kinds of references that make customers feel
  like they're missing out on information.

### Write clearly and concisely\[#UUID-9d2e534b-9f12-97fa-a9ec-cf438f036d0e\_section-idm4653398621256033763280654432]

With information organization covered, the next consideration is
what the information itself should look like. The simpler
your content is, the easier it is for both humans and AI to find the
important pieces of information they need.

* **Use clear terminology that doesn't overlap.** The easier your
  terminology is to follow, the more likely it is that a customer or AI can
  recognize whether content is relevant to a customer's question.

  For example, let's say your company makes music publishing software,
  and your knowledge base has some information about making a demo. But
  your knowledge base might also have information about how prospective
  customers can contact your Sales team for a demo of your software. The
  word "demo" meaning two different things in your knowledge base can
  cause confusion and cause irrelevant search results to come up. If you
  can, see if you can replace one instance with a different word, so the
  word "demo" consistently means only one thing in your knowledge base.

* **Use simple language.** Have you ever read a really long, meandering
  sentence, and by the end weren't really sure what the author was
  trying to say? This can happen when either human customers or an AI are
  parsing your knowledge base. Take the time to cut unnecessary content
  so it's easier to pick out the takeaways from your content.

* **Minimize your reliance on images and videos.** Generative content
  only works with text; your AI Agent can't access images in your knowledge
  base. If you have content in images, it's a good idea to re-evaluate
  if there's a way to provide that same content in text.

  Another reason this is a good idea is for accessibility: your customers
  who have visual disabilities may not be able to see your images or
  videos. Making as much text available in text as possible, like in alt
  text or transcripts, helps both customers chatting with your AI Agent and your
  customers who access your knowledge base using assistive technology like
  screen readers.

* **Verify your table content.** Some tables work better than others
  with AI; sometimes AI is able to parse the spatial relationships
  between cells, and sometimes it gets confused. After setting up your
  AI Agent, test its ability to provide information that comes
  from tables in your knowledge base. Your tables are likely to work if they're
  formatted using proper Markdown, but note that they won't work if they're
  embedded in images.

## Data-driven maintenance\[#UUID-9d2e534b-9f12-97fa-a9ec-cf438f036d0e\_section-idm4550426331680033785813801902]

It's common for documentation teams to be small and sometimes struggle
with keeping entire knowledge bases up to date. If you're on a team like
that, the idea of turning over your knowledge base to an AI Agent
can feel daunting. You're not alone! If this situation feels familiar to
you, it's important to work smarter and not harder by following some
best practices:

* **Collect analytics data for your knowledge base.** There are lots of
  ways to track usage data for your knowledge base, depending on the
  tools you use to make it. Customer usage data is often surprising to people who
  spend all day using a product - that's why it's important to collect
  it.

* **Decide which metrics best indicate success for your knowledge
  base.** The metrics in your analytics data can be tricky: the stories
  they tell are often up to interpretation.

  For example, if customers only tend to spend 10 seconds on a long topic,
  is it because they tend to be looking for a crucial piece of
  information near the top of the page? If that's the case, you probably
  don't need to change anything. But what if they're spending that
  time scanning through the page for information that isn't there and
  leaving in frustration? In that case, there's probably something you
  can improve about the way your knowledge base is organized.

  There's no right or wrong set of metrics to focus on. It's common to
  focus on the topics that are most commonly viewed, or topics that have
  the most positive or negative reviews from customers, but ultimately it's
  up to you and your organization to choose how to measure the success
  of your knowledge base. That strategy can change over time, but you
  should have some data that you can refer back to.

* **Prioritize content reviews based on the data you collect.** After
  collecting some customer usage data, start to go through it. Can you find
  patterns about the kinds of content that customers seemed to gravitate
  towards, or other content that customers didn't touch at all? Using your
  usage data, start creating a priority list for important topics to
  make sure they're polished.

* **You can always disable articles from the Knowledge page.** If you
  know that a topic is out of date, but it's too low on your priority
  list to get to right away, you can disable it from showing up in
  generative content. That way, you can prevent inaccurate information
  from appearing in your AI Agent, without delaying your launch. In the
  future, when you do get a chance to update that topic, you can enable
  it again.

* **Revisit your data on a regular basis.** After connecting your
  knowledge base to your AI Agent, you'll have even more usage data from your
  customers to analyze. When you revisit your data, you can test the
  success of your prior decisions and adjust your priorities
  accordingly.

* **Make use of Ada's reporting tools.** On your Ada dashboard, you can
  see high-level reports on your AI Agent's automated resolution rate, and
  dig deeper into individual conversations to see how your AI Agent
  performed. Once your AI Agent is customer-facing, you'll have
  even more information on how your knowledge base is serving your
  customers through generative AI.

If you're just getting started and don't have analytics yet, consider
prioritizing a few key areas of your product to review first, and go
from there. You don't have to have a perfect plan for collecting
analytics data right away! The important thing is that you eventually
have a system where you can both collect and analyze usage data.

## Ongoing improvement\[#UUID-9d2e534b-9f12-97fa-a9ec-cf438f036d0e\_section-idm4495177675051233908602928966]

What do you do once you have customer data? You use it! Here are a few tips:

* **Keep maintenance regular.** As your product changes, so will your
  documentation, and so will your customers' questions. Set aside regular
  maintenance time to take a look at your AI Agent's reports and conversation
  transcripts, so you can pick out opportunities to improve your
  knowledge base and have your AI Agent performing even better for future
  customers.

* **Keep feedback loops tight.** If you see an opportunity to improve
  your knowledge base so you can improve your AI Agent, make that change
  right away, so you can improve your AI Agent's performance right away.

Over time, with the information about how your customers interact with
your AI Agent, you'll be able to settle into a workflow where you can improve
both your knowledge base and your AI Agent all at once.

<hr />

<p>
  Have any questions? Contact your Ada team, or email us at 

  <a href="mailto:help@ada.cx?subject=Help%20Docs%20inquiry" class="email">{"help@ada.cx"}</a>

  .
</p>