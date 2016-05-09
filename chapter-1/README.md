# Chapter 1 -- The basics

Welcome to our Python course! This first chapter covers a lot of material. 
You do not need to know everything by heart just yet.
This page is intended as a global reference that you will need less and less as we
progress through the course.
* If you are the kind of person who likes to have a high-level overview of the materials for
each week, then start with these documents first (we will have some theory every week).
* If you are the kind of person who likes to get some hands-on experience first, and then
reflect on the theory afterwards, then start with the notebook.

Some helpful links:

**Python:**

* [General documentation](https://docs.python.org/3.5/index.html)
* [Stack Overflow](http://stackoverflow.com/)
* [Learning resources on /r/learnpython](https://www.reddit.com/r/learnpython/wiki/index)

If you take a piece of code from StackOverflow (or some other website), always
acknowledge the source in the comments, and explain what that bit of code does.
(This is also to protect yourself: you should never run code that you haven't
verified or don't understand.)

**GitHub and Markdown:**

* [GitHub Desktop](https://help.github.com/desktop/guides/getting-started/)
* [GitHub Tutorial](http://readwrite.com/2013/09/30/understanding-github-a-journey-for-beginners-part-1/)
* [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Python: an object-oriented language
Python is an **object-oriented** programming language. This means that the computer
'reasons' about the world in terms of **objects**: chunks of information.
Different kinds of information are represented in different ways.
To this end, Python has different built-in **classes**:

* **String** for text.
* **Integers** and **floats** for whole and decimal numbers.
* **Booleans** for truth values.
* **Lists** for ordered sequences of objects.
* **None** for the special value of 'nothing'.

We will later discuss three other classes:

* **Set** and **frozenset** for sets.
* **Dictionary** for mappings between objects.
* **Tuple** for immutable ordered sequences.

Classes in Python are made so that you can perform particular operations on them.
For example: you can compute the sum of two numbers (e.g. `1 + 2`).
This operation is not defined for text; it would make no sense to ask what is the
sum of `'eggs'` and `'spam'`.

## An example

Let's take an example with strings. The box below shows code I typed into my Python interpreter.
`>>>` indicates input. The output is shown without `>>>`.

```python
>>> text = 'Here are some words'
>>> print(text)
Here are some words
>>> type(text)
<class 'str'>
```

What happened here?

1. First we **assigned** the **value** `'Here are some words'` to the
**variable** `text`.
2. Then we issued the `print`-function to print the value of `text`.
(Printing is just outputting some value to the screen.) As the output, we got
`Here are some words` without the single quotes. The single quotes were just there to
tell Python that all the characters in `Here are some words` belong together as a single string.
3. Then we asked Python about the **type** of the variable `text`, and the interpreter
answered that `text` is an **instance** of the class `'str'` (Pythons name for strings).

## Methods
OK, so now we know that `text` corresponds to an instance of the string-class, with the
value `Here are some words`.
The Python-documentation has an [overview of all the **methods** you can use with strings](https://docs.python.org/3.5/library/stdtypes.html#string-methods).
Methods provide the most common operations that you can perform with a particular class.
For example, there is a `startswith()` method that we can use to see if our text starts
with the word `here`:

```python
>>> text.startswith('Here')
True
>>> text.startswith('Her') # Only characters matter. Not whether it's a word.
True
>>> text.startswith('Floppy')
False
```

You can call any method using the dot-notation exemplified above.

Because methods are defined per class, you cannot use a string-method with an integer.
If you try to do so, the Python interpreter will complain:

```python
>>> x = 11
>>> x.startswith(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'startswith'
```

If you really do want to perform string operations on an integer, the only thing
you can do is **cast** the variable to another type:

```python
>>> x = str(x)
>>> x.startswith('1')
True
```

What happened here is that the integer 11 is re-interpreted as a string of two characters:
'1' and '1'.

**Other methods**
* List methods are given [here](https://docs.python.org/3.5/tutorial/datastructures.html#more-on-lists).
* Dictionary methods are given [here](https://docs.python.org/3.5/library/stdtypes.html#typesmapping)
* Set methods are given [here](https://docs.python.org/3.5/library/stdtypes.html#set-types-set-frozenset)

But if you don't want to look these up, you can always use a combination of the
`dir()` and `help()` functions that are built into Python.
The former gives you a list of methods for the variable that you call the function with:

```python
>>> dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
'__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__',
'__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__',
'__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize',
'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format',
'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier',
'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust',
'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust',
'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
'swapcase', 'title', 'translate', 'upper', 'zfill']
```

The double underscore ('dunder') methods are Python-internal. We will cover some
of them later on in this course. If you want to know what any of these methods do,
you can just use the `help()` function on them, like so:

```python
>>> help(text.split)
```

Result:

    Help on built-in function split:

    split(...) method of builtins.str instance
        S.split(sep=None, maxsplit=-1) -> list of strings

        Return a list of the words in S, using sep as the
        delimiter string.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified or is None, any
        whitespace string is a separator and empty strings are
        removed from the result.

(If you are doing this on the command line, you might have entered a different
'mode' to read the help text. Press 'q' and <enter> to go back to the interpreter.)

## Class properties & general operations
In addition to the class methods, Python also provides a set of general functions
and operators. [Here is a list of built-in functions](https://docs.python.org/3.5/library/functions.html). We'll cover these in the notebooks.

### Mathematical operators
Let's first start with [mathematical operators](https://docs.python.org/3.5/library/stdtypes.html#numeric-types-int-float-complex). These are defined for both **integers** and **floats** (numeric types):

| Operation | Result |
|-----------|--------|
| `x + y` |	sum of x and y|
| `x - y` |	difference of x and y 	|  	 
| `x * y` |	product of x and y 	  	 |
| `x / y` |	quotient of x and y 	  	 |
| `x // y` |	floored quotient of x and y	 |
| `x % y` |	remainder of x / y 	|
| `-x` |	x negated 	  	 |
| `+x` |	x unchanged 	  |	 
| `x ** y` |	x to the power y |

But two of these operators (`+` and `*`) also work for other types of objects.
E.g. for lists:

```python
# Addition:
>>> [1] + [2]
[1, 2]
# Multiplication:
>>> [1] *8
[1, 1, 1, 1, 1, 1, 1, 1]
# Combined:
>>> [1] * 4 + [2] * 4
[1, 1, 1, 1, 2, 2, 2, 2]
```

Or for strings:

```python
>>> 'a' + 'b'
'ab'
>>> 'a' * 4
'aaaa'
>>> 'a' * 4 + 'b' * 4
'aaaabbbb'
```

### Sequences
Lists, strings, and tuples are all ordered sequences. The `range()`-object is also a sequence.
Sequences support a [series of common operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations), copied here for convenience (omitting the notes):

| Operation | Result |
|-----------|--------|
| `x in s` |	True if an item of s is equal to x, else False 	|
| `x not in s` |	False if an item of s is equal to x, else True 	|
| `s + t` |	the concatenation of s and t 	|
| `s * n or n * s `|	equivalent to adding s to itself n times 	|
| `s[i]` |	ith item of s, origin 0 	|
| `s[i:j]` |	slice of s from i to j 	|
| `s[i:j:k]` |	slice of s from i to j with step k 	|
| `len(s)` |	length of s 	 |
| `min(s)` |	smallest item of s 	 |
| `max(s)` |	largest item of s 	 |
| `s.index(x[, i[, j]])` |	index of the first occurrence of x in s (at or after index i and before index j) 	|
| `s.count(x)` |	total number of occurrences of x in s |

All sequences are **iterable**, which means that you can iterate over them using a for-loop.
Here is a small example of a for-loop:

```python
for fruit in ['apple', 'pear', 'orange']:
    print(fruit)
```

This for-loop iterates over the list of fruits. Each round the variable `fruit`
gets updated so that it refers to the next string in the list. Then it prints the
relevant string and continues with the next one, until all strings have been printed.

Other things that are iterable include dicts, sets, and **file objects**. (If you iterate
over a dictionary you get keys, and if you iterate over a file you get lines.)

Ned Batchelder has a [great video about iteration](http://nedbatchelder.com/text/iter.html).

### Mutability
We will sometimes mention that some object is (im)mutable.
[The Python glossary](https://docs.python.org/3.5/glossary.html) provides useful definitions:

* **Immutable**: An object with a fixed value. Immutable objects include numbers, strings and tuples. Such an object cannot be altered. A new object has to be created if a different value has to be stored. They play an important role in places where a constant hash value is needed, for example as a key in a dictionary.
* **Mutable**: Mutable objects can change their value but keep their id(). See also immutable.

Examples of mutable objects are lists, sets, and dictionaries. Why this is relevant is a topic for a
later week. If you area really interested, Ned Batchelder has an [excellent talk about Python names and values that discusses these concepts](http://nedbatchelder.com/text/names1.html)

Objects that are instances of a built-in immutable type are *hashable* and can be
used as keys in a dictionary. For a really good explanation of this, see the youtube
video [the mighty dictionary](https://www.youtube.com/watch?v=C4Kc8xzcA68).

----------------
#### Later on in the course..
We will also see that you can define new classes, using either the general **object**
as a base class, or using one of the classes mentioned above as a base class. This
means that you can add more functionality to existing classes. Examples from the standard
library are **Counter** and **defaultdict** in the *collections* module, that use `dict`
as their base class.
