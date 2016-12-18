# Linguistic engineering option: patterns

This assignment revolves around the idea that we can search corpora for the use of particular phrases, in order to identify relations between words. Two relevant citations are:

* [Hearst (1992) Automatic Acquisition of Hyponyms from Large Text Corpora](http://dl.acm.org/citation.cfm?id=992154): Marti Hearst used patterns like *NP, such as NP* to identify hyponyms. An example instance of this pattern would be *fruit, such as apples*. Upon seeing this phrase, we know that apples are a kind of fruit. If you have a large enough corpus, you can learn quite a lot with just a couple of patterns.

* [Veale (2012) Teaching WordNet to *Sing like an Angel* and *Cry like a Baby*](http://afflatus.ucd.ie/Papers/WordNet%20Veale%202012.pdf): Tony Veale used patterns like *VERBing like a NOUN* to find stereotypical behavior. Upon seeing an example instance of this pattern, like *crying like a baby*, we learn that babies typically cry. If you have a large enough corpus, you can find all sorts of stereotypical behaviors.

You can either choose to reproduce the results from one of these articles, or try to extract different information from a large corpus. You could also try to do this in a different language! (This would be especially nice with Tony Veale's paper, since there aren't many resources like his for languages other than English.)

## Data

You can use any corpus you want. For English, we'd recommend the UMBC Webbase corpus or the USENET corpus (the Westbury lab version). These corpora are sufficiently large for a study like this, but not *too* large for you to be drowning in data.

For other languages, contact us. We'll help you look for a nice corpus for you to use.

## Statistics

There are plenty of statistics you could collect. Let's take Tony Veale's paper as an example.

* What is the frequency of each noun?
* How many different verbs modify each noun?
* How many nouns are modified by each verb?
* Do the verbs in the results have the same distribution as in the corpus?
* ...

Also, the unfiltered results probably look only half-decent. There will be a lot of noise. Is there any way in which you could reduce the noise? E.g. by using a cutoff value for one or more of the statistics above.

## Visualization

Sticking to Tony Veale's example, you could visualize many things. A good start would be to create a table with all the statistics.

## Data format

How would you store the results? What information would be relevant for you or others interested in stereotypical actions?