# Chapter 2 -- Control flow tools and files

This chapter we will start working with files, and introduce for-loops, while-loops, and functions.
You will learn how to define your own functions, and use those functions to analyze
text. We will also discuss different file formats.

## For-loops
There are two kinds of loops: the for-loop and the while-loop.
In this paragraph, we will first introduce the for-loop, and we'll discuss while-loops in the next.

The for-loop is the most commonly used loop in Python. You'll find that, most of the
time, you just want to carry out some operation for all the items in a sequence.
And that's just what the for-loop does! It looks like this:

```python
for number in [1,2,3]:
    print(number)
```

This loop prints the numbers 1, 2, and 3, each on a new line. The variable name
`number` is just something I have chosen. It could have been anything, even something
like `sugar_bunny`. But `number` is nice and descriptive. OK, so how does the loop work?

1. The Python interpreter starts by checking whether there's anything to iterate over.
    If the list is empty, it just passes over the for-loop and does nothing.
2. Then, the first value in the iterable (in this case a list) gets assigned to the
variable `number`.
3. Following this, we enter a 'local context', indicated by the indentation (four spaces
    preceding the print function). This local context can be as big as you want. All Python
    cares about is those four spaces. Everything that is indented is part of the local context.
4. Then, Python carries out all the operations in the local context. In this case,
    this is just `print(number)`. Because `number` refers to the first element of the list,
    it prints `1`.
5. Once all operations in the local context have been carried out, the interpreter
    checks if there are any more elements in the list. If so, the next value (in this case `2`)
    gets assigned to the variable `number`.
6. Then, we move to step 3 again: enter the local context, carry out all the operations,
    and check if there's another element in the list, and so on, until there are no more
    elements left.

### Ranges of numbers

Sometimes, it is useful to do the same thing a number of times. To do this, you
can use the `range()` function:

```python
for i in range(10):
    print('I like repeating myself!')
```

This will print 'I like repeating myself' ten times. `range()` is a function that
returns a `range` object. Looping over that object will give you all the numbers in
a particular range, e.g. `range(5,9)` corresponds to [5,6,7,8], excluding 9.

(Note that `range` is not a list. It only keeps one number in memory at any given time,
    so it's really memory-efficient.)

### Enumerating sequences
Sometimes, it is also useful to have the index of an item as you iterate over a list.
For this purpose, there is another useful function called `enumerate()`. It works like this:

```python
for index, character in enumerate('Monty'):
    print('character with index', index, 'is', character)
```

The code above prints:

    character with index 0 is M
    character with index 1 is o
    character with index 2 is n
    character with index 3 is t
    character with index 4 is y

Note that we make use of **multiple assignment** here. Multiple assignment
is the practice of assigning values to multiple variables at once. The simplest example of
multiple assignment is this:

```python
>>> x,y = (1,2)
>>> print(x)
1
>>> print(y)
2
```

The `enumerate` example above is equivalent to this:

```python
for pair in enumerate('Monty'):
    index, character = pair
    print('character with index', index, 'is', character)
```

Or even this:

```python
for pair in enumerate('Monty'):
    index = pair[0]
    character = pair[1]
    print('character with index', index, 'is', character)
```

But both are longer and not as clear. We'll talk more about `enumerate` and multiple
assignment in the notebook.

## While-loops

## If, elif, else

## Functions

## Working with files

### Plain text

**Readings**

These two links are super relevant if you want to learn more about proper text
handling. Don't worry if you don't understand everything. Resources like these
are a good reference if you want to learn about the details.

* [The absolute minimum every software developer absolutely, positively should know about unicode and character sets (no excuses)](http://www.joelonsoftware.com/articles/Unicode.html)
* [Ned Batchelder on 'pragmatic unicode'](http://nedbatchelder.com/text/unipain.html)

### CSV and TSV files

### 'Machine-readable format'

--------------------
##### Later in this course

We will talk about XML and HTML files.
