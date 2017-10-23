# Language resources

There are several language resources that you can make use of. Some of these are
covered in the notebook on getting and processing data.

## Examples

We can group the resources in three different categories:

* Psychological feature norms
* Corpora
* Taxonomies and knowledge bases

### Psychological feature norms

There's an abundance of data in the psychological literature, that's been collected
in order to be able to carry out controlled experiments. Here are some examples:

* Lynott & Connell's [Modality-Specific Norms of Perceptual Strength](http://www.lancaster.ac.uk/people/connelll/lab/norms.html)
* Brysbaert et al.'s [word ratings](http://crr.ugent.be/programs-data/word-ratings)

### Corpora

There are several corpora in the NLTK library already (e.g. Brown, the Switchboard
corpus), but there are many more online. Here is an incomplete list:

* the [Open American National Corpus (OANC)](http://www.anc.org/data/oanc/download/)
* the [UMBC WebBase corpus](http://ebiquity.umbc.edu/blogger/2013/05/01/umbc-webbase-corpus-of-3b-english-words/)
* the [Usenet corpus](http://www.psych.ualberta.ca/~westburylab/downloads/usenetcorpus.download.html)
* the [Enron corpus](https://www.cs.cmu.edu/~./enron/)


### Taxonomies and knowledge bases

* **WordNet** You can use WordNet through the NLTK library: `from nltk.corpus import wordnet as wn`.
* **FrameNet** You can request the FrameNet data [here](https://framenet.icsi.berkeley.edu/fndrupal/framenet_data).
* **DBPedia** You can either access DBPedia online (e.g. through their website [here](http://dbpedia.org/page/Amsterdam), or [through a SPARQL endpoint](http://wiki.dbpedia.org/OnlineAccess)) or download it [here](http://wiki.dbpedia.org/dbpedia-dataset-version-2015-10).
