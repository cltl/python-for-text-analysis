# Chapter 4 -- Remaining issues

This chapter is the last one covering Python-internals. After this, you know most
of what there is to know about the language. The topics in this chapter may be
considered *advanced*, but understanding them is very rewarding.

## Python names and values

It's important to understand the way that Python assigns values to variables.
Consider the following piece of code:

```python
x = [1]
y = x
y.pop()
```

What is the value of `x`? The answer may surprise you. Click [here](http://pythontutor.com/visualize.html#code=x+%3D+%5B1%5D%0Ay+%3D+x%0Ay.pop(%29%0A&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0) to see what happens when you run this code.

Ned Batchelder has a [great video about names and values](http://nedbatchelder.com/text/names1.html).
We'll discuss this video in class.

## Comprehensions

It's possible in Python to define lists using a for-loop. It works like this:

```python
words = ['monty','python','spam','spam','spam']
my_list = [word.upper() for word in words if word.startswith('sp')]
print(my_list)
```

This prints: `['SPAM', 'SPAM', 'SPAM']`

As you loop over a sequence (in this case a list of words), you can check if the
items fulfil some sort of condition (in this case: starting with the letters 'sp').
If so: convert them to upper case and add them to the list. The result is a list
with all the words matching that condition. This way of generating a list is called
a *list comprehension*.

You can do the same thing with sets; just replace the rectangular brackets with
curly brackets (and here I left out the conversion to upper case):

```python
words = ['monty','python','spam','spam','spam']
my_set = {word for word in words if word.startswith('sp')}
print(my_set)
```

This prints `{'spam'}`, because lists cannot contain duplicates.

You can also create dictionaries using comprehensions. Here is an example:

```python
# Store the result of multiplying a number by two in a dictionary:
doubles = {i: i*2 for i in range(20)}
```

But often the value isn't the output of a function or some other operation. Rather,
you have keys and values that you want to store in a dict somehow. This is one way
to do it:

```python
last = ['Chapman', 'Cleese', 'Gilliam', 'Idle', 'Jones', 'Palin']
first = ['Graham', 'Cleese', 'Terry', 'Eric', 'Terry', 'Michael']

names = {last:first for last,first in zip(last,first)}
```

Of course in this specific case you could also do `dict(zip(last,first))`, but it
is useful if there are particular conditions that you want to specify. For example,
all the members who are called Terry:

```python
last = ['Chapman', 'Cleese', 'Gilliam', 'Idle', 'Jones', 'Palin']
first = ['Graham', 'Cleese', 'Terry', 'Eric', 'Terry', 'Michael']

names = {last:first for last,first in zip(last,first) if first == 'Terry'}
```

When should you use a list comprehension?

* When you want a list/set/dict that can be defined in terms of some other iterable (or multiple iterables)

As we've seen above, there are two general modifications that you can make in a
comprehension:

* Restrictive: use an if-statement to select particular items.
* Transformative: use a function or operation to modify the items in your newly defined list/set/dict.

Finally, you can use *nested for-loops* in comprehensions:

```python
# Pairs of numbers between 0 and 10 that are not equal to each other.
# I like to align the for-loops so that it's clear to the reader how deep the
# nesting goes.
unequal_pairs = [(i,j) for i in range(10)
                       for j in range(10) if not i == j]

# This is equivalent to:
from itertools import product
unequal_pairs = [(i,j) for i,j in product(range(10),range(10)) if not i == j]

# But of course you could keep nesting:
unequal_pairs = [(i,j,k) for i in range(10)
                         for j in range(10)
                         for k in range(10) if not i==j==k]
```

## Generators

Generators are like a combination of functions and sequences: when you call them,
they return an iterable that you can loop over only once. The huge advantage of
generators is that you never have all items in the iterable in memory at once.
Here is a re-implementation of `range()` to give you an idea:

```python
def new_range(n):
    """
    Limited re-implementation of range(). Yields all numbers up to n.
    """
    x = 0
    while x < n:
        yield x
        x += 1

for i in new_range(10):
    print(i)
```

This will print all the numbers from 0 up to (but not including) 10. But notice
that the numbers aren't stored anywhere! Once you increment x, the old value is
gone forever. But sometimes that's just what you want to do: go over everything,
and throw away the data once you've extracted the relevant information. Else your
computer's memory might be full and can't handle the new data anymore.

Instead of functions, you can also define generators like this:

```python
squared_numbers = (x*x for x in range(10))
```

Or even use generator arguments:

```python
# Sum of all squared numbers below 10.
sum(x*x for x in range(10))

# Dictionary of numbers and their squares.
dict((x,x*x) for x in range(10))
```

Generators provide *the* way to save memory. So if you're using some collection
of items only once, or if you can't keep everything in memory, generators are the
way to go. But note that there is a trade-off between time and memory: whatever
you don't have to load into memory every time you need it saves you time. So think
about how you choose to load your data.

If you haven't already, now is the time to watch [Ned Batchelder's *loop like a native*](http://nedbatchelder.com/text/iter.html).

## Classes

As you've already seen, Python is an object-oriented language. It has basic classes,
like lists, strings, dictionaries, and sets that all have their own methods. And
it's fairly easy to extend those classes to provide new functionality. Or to create
completely new classes (inheriting from `object`).

The `Counter` and `defaultdict` classes are examples of extensions of the dict class, and the
`namedtuple` class is an extension of `tuple`. The Python tutorial has a
[good section on classes](https://docs.python.org/3.5/tutorial/classes.html).

We will not spend a lot of time on defining classes. You should know that they are
there, but for our purposes we will generally not be needing to define new ones.

Watch [Raymond Hettinger's talk](https://www.youtube.com/watch?v=HTLu2DFOdTg) on classes, though.
There are some really good ideas in it.

## External modules

While working on a problem, it's always worthwile to look around online to see if
someone else has worked on something similar (or even on the same problem). Often
you will find that, yes, someone has worked on something similar before, and there's
even a module out there that is super useful and would save you a lot of work. Awesome!
Now how to go from here?

The first thing to do is see if you already have the module installed. Just try
to import it and see what happens. Worst case, you'll see something like this:

```
>>> import unknown_module
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'unknown_module'
```

If the module is not already installed, and you're using anaconda, use `conda install MODULENAME`.
(Where MODULENAME is replaced by whatever the module is called.) If that doesn't work, try `pip install MODULENAME`.
This usually works. If it doesn't, look for instructions on how to install the module.
