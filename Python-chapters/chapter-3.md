# Chapter 3 -- Batteries included

Python is sometimes described as a 'batteries-included' language. What people mean
by this is that the language comes with a rich collection of modules that you can
use to solve everyday tasks. There's no need to write any specialized code to do
common tasks: others have probably solved the task for you and wrote an efficient
implementation. This chapter is devoted to the many modules that come with Python.

Much of what we'll cover below is also in [the Python library reference](https://docs.python.org/3.5/library/index.html).
Below is a list of sections in the library reference we think are most important
for our purpose of analyzing text.

The first four are full sections that cover the same material as chapters 1 and 2.
You may want to read these first, but you can also skip them and move to the built-ins.
(They're great reference material, though!)

* **1.** [Introduction](https://docs.python.org/3.5/library/intro.html)
* **2.** [Built-in Functions](https://docs.python.org/3.5/library/functions.html)
* **3.** [Built-in Constants](https://docs.python.org/3.5/library/constants.html)
* **4.** [Built-in Types](https://docs.python.org/3.5/library/stdtypes.html)

We will focus on these sections:

* **6.1** [string](https://docs.python.org/3.5/library/string.html)
* **6.2.** [re](https://docs.python.org/3.5/library/re.html)
* **8.1.** [datetime](https://docs.python.org/3.5/library/datetime.html)
* **8.3.** [collections](https://docs.python.org/3.5/library/collections.html)
* **9.2.** [math](https://docs.python.org/3.5/library/math.html)
* **9.6.** [random](https://docs.python.org/3.5/library/random.html)
* **10.1.** [itertools](https://docs.python.org/3.5/library/itertools.html)
* **10.2.** [functools](https://docs.python.org/3.5/library/functools.html)
* **11.2.** [os.path](https://docs.python.org/3.5/library/os.path.html)
* **11.7.** [glob](https://docs.python.org/3.5/library/glob.html)
* **12.1.** [pickle](https://docs.python.org/3.5/library/pickle.html)
* **13.2.** [gzip](https://docs.python.org/3.5/library/gzip.html)
* **14.1.** [csv](https://docs.python.org/3.5/library/csv.html)
* **19.2.** [json](https://docs.python.org/3.5/library/json.html)
* **26.3** [doctest](https://docs.python.org/3.5/library/doctest.html)

## Importing modules

Whenever you want to use a module, you first have to import that module. For example:
`import re` lets you import the regular expressions module.

You can rename a module as you import it: `import re as regex4life` if you want to
show how much of a fan of regex you are, for example. Or just if you want to avoid
a clash between names that have already been defined and the module name.

You can also import part of a module, for example: `from string import ascii_lowercase`.
This allows you to use that part directly, without having to use `string.ascii_lowercase`.
(It also saves you from importing the *entire* library.)

One thing that you will see, but should *never* do is `from re import *`. That asterisk
tells Python to import everything from the `re` module into your namespace. But that
also means that you might be overriding functions or variables that you've defined
before! After all: it's unclear how much you're importing and what all these new things
are called.

## String: useful tools to work with strings

The `string` module doesn't add much to the string functionality in Python, but
it does provide some useful constants (copied from the docs):

* **string.ascii_letters** The concatenation of the ascii_lowercase and ascii_uppercase constants described below. This value is not locale-dependent.

* **string.ascii_lowercase** The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not locale-dependent and will not change.

* **string.ascii_uppercase** The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not locale-dependent and will not change.

* **string.digits** The string '0123456789'.

* **string.hexdigits** The string '0123456789abcdefABCDEF'.

* **string.octdigits** The string '01234567'.

* **string.punctuation** String of ASCII characters which are considered punctuation characters in the C locale.

* **string.printable** String of ASCII characters which are considered printable. This is a combination of digits, ascii_letters, punctuation, and whitespace.

* **string.whitespace** A string containing all ASCII characters that are considered whitespace. This includes the characters space, tab, linefeed, return, formfeed, and vertical tab.

Use these constants whenever you want to loop over all characters or all numbers.
As a general rule: **don't implement stuff that already exists in Python.** At the
very least it will save you from embarrassing typos (missing letters in the alphabet).

## Re: regular expressions

Regular expressions provide a very powerful way to search for patterns in text.
The Python documentation already offers [a great how-to](https://docs.python.org/3/howto/regex.html#regex-howto)
that tells you all you should know about regular expressions. We will practice regular
expressions in the notebooks.

## Datetime: to work with dates



## Collections: useful classes to store data

The collections module provides specialized classes that build on the core classes
in the standard library. You can use them by importing them from the `collections`
module, e.g. `from collections import namedtuple`. The most useful ones are listed
below.

* **namedtuple** is an extension of the `tuple` class. It enables you to make your
code more explicit and self-documenting, by making custom tuples. Suppose we were
working with coordinates a lot. Then you could use `namedtuple` to create a `Point`
object like this: Point = namedtuple('Point',['x', 'y']). Now every time you want to work
with coordinates, you can use `Point` with the relevant coordinate values to instantiate
a new point. E.g. `Point(5,8)` returns a `Point` object with attributes `x` and `y`,
where the value of `x` is 5 and the value of `y` is 8.

* **defaultdict** is an extension of `dict` that lets you create dictionaries
with default values. E.g. `d = defaultdict(list)` creates a dictionary where the
standard value is an empty list. So you could immediately add values to that list
for any key, without checking whether the key is in the dictionary already.

* **Counter** is an extension of `dict` that makes counting much easier. You can
initialize it with an iterable to immediately count all the objects in the iterable,
e.g. `c = Counter([1,2,3,4,5,6,5,4,35,3,2,2,4,6,7,8])`, or you can initialize an empty
Counter and update the counts. E.g. `c = Counter()` followed by `c.update([1,2,3,4,1])`.

## Math: everything you need for basic math



## Random: shuffle lists, sample data, or generate random numbers

The `random` module provides all kinds of randomizations. After you've imported
`random`, you can:

* **Shuffle a list** in place using `random.shuffle(the_list)`

* **Sample a subset** using `random.sample(the_list, 25)`. You can also use this
  function as a shuffling function. If `n = len(the_list)`, use `random.sample(the_list, n)`.

* **Generate random numbers** either use `random.random()` to generate a number
  between 0 and 1, or use `random.choice(range(30))`.

* **Seed the random number generator** to make your results reproducible. Just use
  `random.seed(12345)` right after importing the `random` module and it will use that
  seed number to generate pseudorandom numbers that will be the same each run.

## Itertools: loop over your data

The `itertools` module has too many useful functions to list here. [Read the docs](https://docs.python.org/3/library/itertools.html)

## Functools: advanced function manipulation

The `functools` module has useful meta-functions that you can use to manipulate
existing functions. These are the two most common ones for me.

* `@functools.lru_cache()` is a decorator that memorizes input-output combinations
  for a function. This can speed up your code tremendously if you frequently call
  a particular function with the same input.

* The `partial` function is useful to 'fill in' an argument in a function, so that
  you won't have to type as much.

```python
from functools import partial

def hello(source, target):
    "Tell someone hello."
    print('Hello,', source, '\nGreetings,', target)
    
hello_from_emiel = partial(hello, target='Emiel')

# This will print:
# "Hello Marten
# Greetings, Emiel"
hello_from_emiel('Marten')
```
## os.path: manipulate paths

Windows machines have paths that look like 'C:\\some\folder', whereas UNIX-based
operating systems have paths that look like '/some/folder'.
Os.path is a very useful library if you want to create OS-independent paths, so
that your scripts will work on any computer without modifications. Here's how to
use it:

```python
import os
# Suppose that you have a set of texts in ./data/corpora/exciting corpus.
# If you want to make an OS-independent path to that folder, use:
relative_path = os.path.join('data', 'corpora','exciting_corpus')
absolute_path = os.path.abspath(relative_path)
```

This module is very useful in combination with `glob`.

## Glob: find files

The `glob` module is useful to list all the files in a particular directory. After
importing the module with `import glob`, you can find files using the `glob.glob()`
function. For example, if you have a folder called 'data' with different kinds of
files, and you want a list of all the text files, you might use `glob.glob('data/*.txt')`.
The asterisk serves as a wildcard that matches any filename. You can also use the
asterisk to match folders, e.g. `glob.glob('*/*.txt')`.

## Csv: manipulate csv and tsv files

The `csv` module is very useful if you have spreadsheet-like data. Basic usage is
as follows:

```python
import csv

header = ['Name','Age']
rows = [['John', 5], ['Mary', 6], ['Bob', 12], ['Alice', 13]]

with open('Ages.tsv','w') as f:
    # If you don't specify a delimiter, the file will be a standard CSV file.
    # But now we specified a tab delimiter, the file is a TSV file instead.
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(header) # for a single row
    writer.writerows(rows) # for multiple rows
```

The module also contains a `DictReader` and a `DictWriter` object that allows you
to read and write rows using dictionaries. Very useful! Read the docs [here](https://docs.python.org/3.5/library/csv.html).


## Json: manipulate json files

JSON is a very common file format on the internet, and it's useful to store data
(lists, dicts, numbers and strings -- no sets or tuples!) in a readable format.

Here's how to load a JSON file:

```python
import json

with open('filename.json') as f:
    obj = json.load(f)
```

Writing out JSON files is equally simple:

```python
import json

obj = ['bla', 2.0, {1: 'apple', 2: 'pear'}]

with open('filename.json','w') as f:
    json.dump(obj, f)
```

If you ever need to pretty-print a JSON object: `json.dumps(obj, indent=4, sort_keys=True)`
returns a string. You can turn that string back into a JSON-serializable object by using
`json.loads(str_representation)`.


## Pickle: save python objects

The `pickle` module lets you save Python objects to your computer, so that you can
reload them later. This may be useful if those objects take a long time to create.
A downside of pickling objects, as opposed to saving your data in CSV/TSV/JSON/TXT/XML
format is that `.pickle` files are not human-readable. Moreover, you should never
try to load a `.pickle` file from an untrusted source, as it may contain malicious
code that will be executed when you load the file.

```python
import pickle

# Create a dictionary
d = {'a':0, 'b':1, 'c':3}

# Write it to a pickle file:
with open('dictionary.pickle','w') as f:
    pickle.dump(d,f)

# Read a pickle file and load the object:
with open('dictionary.pickle') as f:
    obj = pickle.load(f)
```

## Gzip: compressing files

If you're working with a lot of data, your files can become really big. To save
space on your hard drive, or to be able to share your results without having to
upload huge files, you can use the Gzip module. Gzip is a compression format that
is well-suited to make text, xml, and csv data really small. Here's how it works:

```python
import gzip

# If you use the 'w' or 'wb' mode then you need to encode the string:

with gzip.open('test.txt.gz','wb') as f:
    f.write('Hello, world!'.encode('utf-8'))

# But you don't have to if you open the file in text mode.
# See: http://stackoverflow.com/a/27206278/2899924

with gzip.open('test.txt.gz','wt') as f:
    f.write('Hello, world!')

# And you can even use the CSV module if you open the file in text mode:
import csv

rows = [list(range(10))] * 10
with gzip.open('test.csv.gz', 'wt') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
```

Reading from gzip files works in a similar way. Read [the docs](https://docs.python.org/3/library/gzip.html)
for more.

## Doctest: Enhance your docstrings and test your functions

Doctest is a module that enables you to automatically check whether your functions
produce the output that you expect. It works like this:

```python
# Example in /Examples/doctest-example.py

def hello(name):
    """
    Function that returns a greeting for whatever name you enter.

    Usage:
    >>> hello('Emiel')
    'Hello, Emiel!'
    """
    return ''.join(["Hello, ", name, '!'])
```

The docstring shows how to use the function, and the expected output of the function.
The Doctest module allows you to test whether you actually get that expected output
when you use the function as in the example. You can try this yourself. Navigate to
the Examples folder on the command line and use the following command: `python -m doctest -v doctest-example.py`
This should print the following message:

```
Trying:
    hello('Emiel')
Expecting:
    'Hello, Emiel!'
ok
1 items had no tests:
    doctest-example
1 items passed all tests:
   1 tests in doctest-example.hello
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
```

Of course this is a trivial example, but it's very useful if you're working on a
larger codebase. Especially if you want to add new functionality without changing
the behavior of your functions. Then you really want to be able to check that
everything still works as expected.

## Standalone scripts and the Argparse module

While we've mostly been working with notebooks so far, you can also just write
python scripts as standalone files. Basically it's just a plain text file with
python code (called a 'script'), saved with the `.py` extension. Here's a very
minimal example:

```python
def main():
    "The main function."
    print("Hello, world!")

if __name__ == "__main__":
    main()
```

If you save this file as "helloworld.py", you can either import it (`import helloworld`)
or run it from the command line by typing `python helloworld.py`. The if-statement
is there so that it will only run the main function if the script is run from the
command line. If you import the file, it won't print "Hello, world!" unless you
use `helloworld.main()`.

If your program becomes bigger, you will probably want to pass arguments to the
script from the command line. (Maybe you want to say "Hello" to a specific person!)
The best thing to do then is to look into the `argparse` module. Here's how you set it up:

```python
# import the module
import argparse

# Initialize the parser
parser = argparse.ArgumentParser()

# Add arguments to be specified on the command line:
parser.add_argument("--target", help="Person you want to say 'hello' to.", type=str)
parser.add_argument("--source", help="Who is saying hello?", type=str)

def hello(source, target):
    "The main function that says 'hello' to the target, with greetings by the source."
    print("Hello", target)
    print("Greetings from", source)

if __name__ == "__main__":
    args = parser.parse_args()
    hello(args.source, args.target)
```

You can test whether your code works by providing it with some arguments like this:

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--target", help="Person you want to say 'hello' to.", type=str)
parser.add_argument("--source", help="Who is saying hello?", type=str)

arguments = '--source Emiel --target Marten'.split()
print(parser.parse_args(arguments))
# This will print Namespace(source='Emiel', target='Marten')
```

For full reproducibility, it's recommended that you store all the arguments in a
log file so that you'll always know exactly how the program was called.
[Here](https://docs.python.org/3.5/howto/argparse.html) is a longer tutorial on
the use of argparse.
