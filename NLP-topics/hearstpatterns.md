# Hearst-patterns

Hearst-patterns are a classic method to detect particular kinds of words. They are
named after Marti Hearst, following the paper [Automatic acquisition of hyponyms from large text corpora](http://dl.acm.org/citation.cfm?id=992154).
Hyponymy is a relation between a specific word (the hyponym) and a more general word (the hypernym).
E.g. [banana, fruit]. It is possible to extract hyponym-hypernym pairs from a corpus
by searching for phrases like "fruits, such as bananas". These phrases tell us that
'banana' is a specific instance of 'fruit'. We can generalize from this specific phrase
by using wildcards: 'X, such as Y'. This is a *pattern*. Hearst was able to extract
a large collection of hyponyms from a corpus using several different patterns.

## N-grams

## Regular expressions
