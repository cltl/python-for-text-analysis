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



## Math: everything you need for basic math



## Random: shuffle lists, sample data, or generate random numbers



## Itertools: make your loops even better



## Functools: advanced function manipulation



## os.path: manipulate paths



## Glob: find ALL the files!



## Pickle: save python objects



## Gzip: compressing files



## Csv: manipulate csv and tsv files



## Json: manipulate json files



## Doctest: Enhance your docstrings and test your functions


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
The best thing to do then is to look into the `argparse` module.
