# The natural language processing pipeline

Text data is unstructured. But if you want to extract information from text, then
you often need to process that data into a more structured representation. This is
what NLP pipelines do. They're called pipelines because they are constructed out
of several different *modules*. These are the most common ones:

* A tokenizer, to split text into paragraphs, sentences, and words.
* A part-of-speech (POS) tagger, to identify different parts of speech (verbs, nouns, ...).
* A lemmatizer, to identify word forms with their lemmas (basic word form).
* A Named Entity Recognizer (NER), to identify people, locations, organizations, etc.
* A dependency parser, to understand the sentence structure.
* A semantic role labeler (SRL), to determine who does what to whom (and how).
* A word sense disambiguation (WSD) system, to assign the correct meaning to every word.
* A polarity tagger, to know whether a sentence is positive or negative.

You don't always need all these modules. But it's important to know that they are
there, so that you can use them when the need arises.

### How can you use these modules?

Let's be clear about this: **you don't always need to use Python for this**. There are
some very strong NLP programs out there that don't rely on Python. You can typically
call these programs from the command line. Examples are:

* [Treetagger](http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/) is a POS-tagger
  and lemmatizer in one. It provides support for many different languages. If you want to
  call Treetagger from Python, use [treetaggerwrapper](http://treetaggerwrapper.readthedocs.io/).
  [Treetagger-python](https://github.com/miotto/treetagger-python) also works, but is much slower.

* [Stanford's CoreNLP](http://stanfordnlp.github.io/CoreNLP/) is a very powerful system
  that is able to process English, German, Spanish, French, Chinese and Arabic. (Each to
  a different extent, though. The pipeline for English is most complete.)

* [The Maltparser](http://www.maltparser.org/) has models for English, Swedish, French, and Spanish.

And there are many more out there. You'll hear all about these libraries in the NLP toolkits course.
Sometimes it's best to just run one of these programs and only analyze the output in Python.

Having that said, there are many **NLP-tools that have been developed for Python**:

* [Natural Language ToolKit (NLTK)](http://www.nltk.org/): Incredibly versatile library with a bit of everything.
  The only downside is that it's not the fastest library out there, and it lags behind the
  state-of-the-art.
    * Access to several corpora.
    * Create a POS-tagger. (Some of these are actually state-of-the-art if you have enough training data.)
    * Perform corpus analyses.
    * Interface with WordNet.
* [Pattern](http://www.clips.ua.ac.be/pattern): A module that describes itself as a 'web mining module'. Implements a
    tokenizer, tagger, parser, and sentiment analyzer for multiple different languages.
    Also provides an API for Google, Twitter, Wikipedia and Bing.
* [Textblob](http://textblob.readthedocs.io/en/dev/): Another general NLP library that builds on the NLTK and Pattern.
* [SpaCy](https://spacy.io/): Tokenizer, POS-tagger, parser and entity classifier for English and German. (More languages in progress.)
