# Hearst-patterns

Hearst-patterns are a classic method to detect particular kinds of words. They are
named after Marti Hearst, following the paper [Automatic acquisition of hyponyms from large text corpora](http://dl.acm.org/citation.cfm?id=992154).
Hyponymy is a relation between a specific word (the hyponym) and a more general word (the hypernym).
E.g. [banana, fruit]. It is possible to extract hyponym-hypernym pairs from a corpus
by searching for phrases like "fruits, such as bananas". These phrases tell us that
'banana' is a specific instance of 'fruit'. We can generalize from this specific phrase
by using wildcards: 'X, such as Y'. This is a *pattern*. Hearst was able to extract
a large collection of hyponyms from a corpus using several different patterns.

## Searching for patterns in a text

You can easily search for patterns in a text using *regular expressions*. Use
[this tutorial](https://regexone.com/) to learn how they work. Then familiarize
yourself with the [re](https://docs.python.org/3/library/re.html) module in Python.

## Questions

1. Can you think of other patterns that signal hyponymy? What are they?
2. Can you think of patterns indicating antonymy? What are they?
3. Are there other lexical relations that you might use a pattern for?

## Read more

Read Tony Veale's article [Teaching WordNet to *Sing like an Angel* and *Cry like a Baby*](http://afflatus.ucd.ie/Papers/WordNet%20Veale%202012.pdf).
