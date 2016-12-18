# Forensics option: Authorship features

The goal of this assignment is to compute statistics about a text that may help you identify its author. Besides extracting statistics, you should also visualize the extracted features, so that you can show the differences between multiple authors in an insightful manner.

## Responsibility

First, a point on responsibility. I want to make this very clear (especially since some of you might end up in Forensics): **Never blindly trust in a machine's judgment!** Computers are stupid, but they can easily impress humans with their ability to crunch numbers. Therefore, it's very important to manually inspect the data as well. Also remember that this notebook doesn't cover any measure of statistical significance. So any difference that you find between two authors may just be coincidence (a full discussion of statistical significance goes beyond the scope of this course) or due to the domain (people write differently on Facebook than in a formal letter).

The methods illustrated in this notebook are by no means state-of-the-art, but they are foundational to the field of authorship detection.

## Features

By *features*, we mean properties or characteristics of a text that are useful inputs for a machine to make predictions about that text (in this case: predicting authorship). We recommend that you read [A survey of modern authorship attribution methods](http://onlinelibrary.wiley.com/doi/10.1002/asi.21001/full) by Efstathios Stamatatos. This paper provides a nice overview of features that are commonly used in authorship attribution. The paper dates back to 2008, and newer methods have been developed, but these features are still important. We'll work with a selection of features from the literature. Most important for us here is how to extract features *efficiently* and how to *represent* them. These are the features we will use:

* Character counts
* Mean word length
* Mean sentence length
* Standard deviation of sentence length
* Type-token ratio
* Hapax legomena ratio
* Stopword counts
* Whitespace
* Part-of-speech (e.g. does the author use a lot of adjectives?)
* ...your own suggestion(s)

Some of these features sound really basic, but don't let their basic nature fool you. [This piece on punctuation in novels](https://medium.com/@neuroecology/punctuation-in-novels-8f316d542ec4) shows you how informative punctuation can be. And here is an excellent quote by Gary Provost (from *100 Ways To Improve Your Writing*) that shows the power of sentence length to change the character of a text:

> **VARY SENTENCE LENGTH**
> 
> This sentence has five words. Here are five more words. Five-word sentences are fine. But several together become monotonous. Listen to what is happening. The writing is getting boring. The sound of it drones. It's like a stuck record. The ear demands some variety.
>
> Now listen. I vary the sentence length, and I create music. Music. The writing sings. It has a pleasant rhythm, a lilt, a harmony. I use short sentences. And I use sentences of medium length. And sometimes when I am certain the reader is rested, I will engage him with a sentence of considerable length, a sentence that burns with energy and builds with all the impetus of a crescendo, the roll of the drums, the crash of the cymbals--sounds that say listen to this, it is important.
>
> So write with a combination of short, medium, and long sentences. Create a sound that pleases the reader's ear. Don't just write words. Write music.

(Fun fact: the use of sentence length to determine authorship goes back to [1939](http://www.jstor.org/stable/2332655?seq=1#page_scan_tab_contents)!)

Of course, there are many more possible features. E.g. n-gram features (what combinations of words does the author use?). Feel free to experiment! Another approach is language modeling, e.g. using a Hidden Markov Model (HMM) or a Long Short-Term Memory network (LSTM). If you take this approach, the goal is to learn what sequences of tokens are typical for an author to use. With enough text, these models are really powerful.

## Assignment

Now let's get to work! The plan for this assignment is to write functions to extract the different features. However, you shouldn't write a separate function for each feature! Instead, group features that are naturally related to each other so that you minimize repeating yourself.

Read the list of features again and try to think of the requirements each of them has: **what do you need to do in order to compute these features?**

* Character counts
* Mean word length
* Mean sentence length
* Median sentence length
* Standard deviation of sentence length
* Type-token ratio
* Hapax legomena ratio
* Stopword counts
* Whitespace
* Part-of-speech
* ...your own suggestion(s)

Also think about the situation where you have multiple files for one author.

**Storing and visualizing the data** you are also required to visualize and store the data, so that you can communicate your results with others. Think of different use cases that you may have, and how you may accommodate the requirements for those use cases. For example:

* Suppose I asked you to compare two authors. What kind of information would you show me?
* Does the answer to that question change if I have multiple texts for each author?

## General advice

This assignment isn't something you should do in a linear fashion. First try to extract one feature from one document and store and visualize it. Then you will get a feeling for how much work the assignment will be, and also you will know what format the features should have for you to easily store and visualize your results.

## Python libraries

There are already several libraries to perform authorship detection. Below is a short list of libraries that I've found while researching this subject. If you want to delve deeper into authorship detection, I'd recommend you look at these in more detail. (Even if you won't use these libraries, it's nice to see how others have tackled the problem. No need to reinvent the wheel!)

* Mike Kestemont's [PyStyl](https://github.com/mikekestemont/pystyl) is probably the most complete library for authorship detection.
* The Information Sciences Institute provides the [digStylometry](https://github.com/usc-isi-i2/dig-stylometry) package.

It's also possible to determine authorship using neural networks. But that goes way beyond the scope of our course.

## Miscellaneous scripts
Here are some other scripts that I've used as inspiration for the exercises in this notebook.

* [Stylometry](https://github.com/jpotts18/stylometry) is a small set of scripts from Jeff Potter.
* [Here](https://github.com/d10genes/Authorship-Attribution) is another pair of scripts from 'Chris'.
* [Here](http://www.aicbt.com/authorship-attribution/) is a blog from a consultancy company called AICBT Consulting.