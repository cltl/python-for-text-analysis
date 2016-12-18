# Linguistic engineering option: statistics

The goal of this project is to compute statistics on the basis of a corpus, in order to compare it with other corpora. This is useful, because current natural language processing technology is quite sensitive to these differences. A NLP system that is trained on one kind of corpus, and displays very good performance, might perfom much worse on a different kind of corpus. This is known as the problem of *domain adaptation*. 

[A recent paper from our group (Ilievski et al. 2016)](http://www.aclweb.org/anthology/C/C16/C16-1112.pdf) proposes several advanced measures to be able to compare corpora in terms of the entities and events that a corpus refers to. This assignment focuses on more basic statistics.

## Data
In the folder **data**, there are 10.000 json files, each containing one article of the [SignalMedia corpus](http://research.signalmedia.co/newsir16/signal-dataset.html). **Please do not redistribute this data, this is for educational purposes only.**

Let's look at an example. Here's a small bit of Python to read in one article, and print its contents.

```python
import json

with open('data/4848.json') as infile:
    a_json = json.load(infile)
    print(json.dumps(a_json, indent=4, sort_keys=True))
```

Here are the contents:

```python
{
    "content": "CLEVELAND, OH - AUGUST 06: Republican presidential candidates (L-R) New Jersey Gov. Chris Christie, Sen. Marco Rubio (R-FL), Ben Carson, Wisconsin Gov. Scott Walker, Donald Trump, Jeb Bush, Mike Huckabee and Sen. Ted Cruz (R-TX) take the stage at the Quicken Loans Arena August 6, 2015 in Cleveland, Ohio. \n \nScott Olson \n \nImage copyright 2015 . All rights reserved. This material may not be published, broadcast, rewritten, or redistributed.",
    "id": "5bb69bce-741e-42b3-af0a-c911bfb71330",
    "media-type": "News",
    "published": "2015-09-16T16:57:45Z",
    "source": "KSHB",
    "title": "The GOP Presidential debate BINGO card"
}
```

Each json file (containing one news article) has the following keys (information taken [SignalMedia corpus](http://research.signalmedia.co/newsir16/signal-dataset.html)):

* **id**: a unique identifier for the article
* **title**: the title of the article
* **content**: the textual content of the article (may occasionally contain HTML and JavaScript content)
* **source**: the name of the article source (e.g. Reuters)
* **published**: the publication date of the article
* **media-type**: either *News* or *Blog*

You can use [spaCy](https://spacy.io/) to process the text. Please check the notebook **Topic 4** for instructions on how to install spaCy. Here is an example of how spaCy works:

```python
from spacy.en import English
nlp = English()

with open('data/4848.json') as infile:
    a_json = json.load(infile)
    
spacy_output = nlp(a_json['content'])

for sent_obj in spacy_output.sents: # for each sentence
    for token_obj in spacy_output: # for each token in a sentence
        print()
        print('token', token_obj.text)
        print('type', token_obj.lemma_)
        print('part of speech', token_obj.pos_)
        print('stopword', token_obj.is_stop)
        break
    break
```

Output: 

```
token CLEVELAND
type cleveland
part of speech NOUN
stopword False
```

To summarize, for each article you will have two sources of information:

1. you have the metadata in the json file
2. you have the annotations from spaCy




## Statistics

Write a a function/script that takes a list/set/generator of paths to one or more json files in the folder **data** as input and outputs a dictionary containing the:

* average number of tokens
    * per article
* average number of types
    * per article
* average number of sentences
    * per article
* 10 longest sentences in all articles
* type-token ratio (number of types / number of tokens)
    * per article
    * overall
* frequency per source (see metadata)
* frequency per media-type (see metadata)

In addition, please write the statistics to a TSV (tab separated) file.

## Visualizing interesting properties of the data
This part is completely open. Feel free to visualize whatever you want.
Please create at least three visualizations. Please take a look at **Topic 6** for inspiration.
