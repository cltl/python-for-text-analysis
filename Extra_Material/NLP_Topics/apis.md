# APIs and scraping

Nowadays, the web is our main source of data. Sometimes, website developers provide
APIs (*application programming interface*), so that you can programmatically access
their content. Other times, there is no API and you have to *scrape* the content yourself.

## APIs

We cover APIs in the notebook on *Getting and Processing data*.

## Scraping

The [Wikipedia page on scraping](https://en.wikipedia.org/wiki/Web_scraping) covers
the subject pretty well. Relevant techniques in Python are:

* Using the *requests* library to retrieve relevant pages, and using lxml.html to parse them.
* If you have a Mac or Windows machine, you can use [the Scrapy module](https://doc.scrapy.org/en/latest/index.html).
* If the website is difficult to crawl using only the page source, you can use
[Selenium](http://selenium-python.readthedocs.io/) to control either your own browser
or a 'headless' browser such as [PhantomJS](http://phantomjs.org/). Using the latter
option, you're basically similating a browser and letting Python control a virtual
keyboard and mouse. You can even take screenshots during the scraping procedure!

There are two important rules when it comes to scraping:

1. Be nice to the server. Ensure that you're not making too many requests in a short
period of time. Breaking this rule could get you banned from the website, or cause the
server to crash.
2. Don't do anything illegal. Respect the copyright of the content owners, and don't
further distribute the scraped data unless you've ensured that it's OK to do so
(e.g. under [fair use](https://en.wikipedia.org/wiki/Fair_use)).
