# Useful external modules

This document lists modules I've found useful in my research. It is *not* meant
as an introduction to those modules. Rather, I encourage you to try them out if
they sound interesting to you, follow the documentation, and experiment a little.
If you have any questions, of course you can always contact me.

## Natural language processing

* Natural Language ToolKit (NLTK): Incredibly versatile library with a bit of everything.
  The only downside is that it's not the fastest library out there, and it lags behind the
  state-of-the-art.
    * Access to several corpora.
    * Create a POS-tagger.
    * Perform corpus analyses.
    * Interface with WordNet.
* Pattern: A module that describes itself as a 'web mining module'. Implements a
    tokenizer, tagger, parser, and sentiment analyzer for multiple different languages.
    Also provides an API for Google, Twitter, Wikipedia and Bing.
* Textblob: Another general NLP library that builds on the NLTK and Pattern.
* SpaCy: Tokenizer, POS-tagger, parser and entity classifier.
* Gensim: For building vector spaces and topic models.

## Data analysis and machine learning

* Scikit-learn: For all your machine learning needs.
* Python-louvain: provides the `community` module, that implements louvain clustering for NetworkX graphs.

## File formats and I/O

* beautifulsoup: Read and write HTML. (Also reads XML but lxml is better.)
* lxml: Read and write XML.
* xlrd: Read Excel format.
* xlwt: Write Excel format.

## Visualization

Also see the visualization notebook.

* Matplotlib: The basic plotting library.
* Bokeh: Make interactive graphs.
* Seaborn: Make Matplotlib graphs prettier.
* Pandas: mostly for data management, but also has some visualization built in.

## Other

* Networkx: one of the best libraries to work with data represented as a graph.
  Exports to Gephi format, so that you can make beautiful visualizations.
* Flask: lightweight module to create websites. Very useful if you want to make a
  demo or browser-based interface.
* Django: more powerful module to create websites.
