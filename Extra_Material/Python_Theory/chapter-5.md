# Chapter 5 -- On your own

Now that you know the basics of Python, let's talk strategy. How do you tackle new
problems? What do you do when you get stuck? What if your program takes ages to finish?
That's what this chapter is about: tips and tricks that we've found helpful over the years.

## How to tackle any problem

* Start small, with one data point.

* Start from the problem, not from the code. Don't think "I need to loop over this
  and then ...", but think "I want to take X, and get Y. How do I get from X to Y?"

* Start with what you know. E.g. if you want to do something with a string, make a variable
  with a suitable name and check whether any of the string methods might be useful.

* Divide the problem into steps: what do you need to do first? Solve that thing
  first, and only once you've verified that it works move on to the next step.

* Use print-statements extensively as you are moving forward. Make sure that you
  know what your code does at every point in the script.

* Document your code as you write. This forces you to explain what you are doing.

* Be conscious of your assumptions, and spell them out. (You could even write test
  cases with these assumptions in mind.)

* Keep to the style guide, and write clear function names. This forces you to
  think about what it is you're doing. Variables called 'a', 'b', 'c' obfuscate
  problems. (Unless these characters have a specific meaning in the context.)

* If you get stuck, try to explain to yourself what every part of your code does.
  This also works with others: see pair programming and rubber duck debugging.

## How to deal with large amounts of data

When you have to deal with large amounts of data, it's important to think about
scalability: what happens when you run your script on thousands of files?

There's a number of constraining factors (**bottlenecks**) that influence how long it will take for your program to run (or even whether it can complete). Here they are:

* **CPU speed** If your processor runs at 100% of its capacity, it is likely that processing speed is the limiting factor. There are two things you can do:
    1. optimize your code (see below),
    2. parallelize your code (look into the [multiprocessing package](https://docs.python.org/3/library/multiprocessing.html)).

* **Memory size** Sometimes a program can take up all of your computer's working memory (RAM). Some computers are configured to use part of your hard drive as additional memory ('swap memory'), but this has the downside of being much slower. If your computer runs out of memory, you will get a `MemoryError`. There are three things you can do:
    1. optimize your code (use generators and other techniques that only keep relevant data in memory and discard everything when it's no longer needed).
    2. preprocess the data first so that your program only works on the relevant data (this can be combined with 1).
    3. write the data you don't need all the time to the hard drive.
    
(On the flip side, if you have plenty of memory, you can sometimes exchange memory
for speed: keep stuff in memory so that everything is quickly accessible. Do note
that this strategy doesn't scale well.)

* **I/O (input/output)** When your program does a lot of reading and writing, you may see that the CPU runs at less than its full capacity. If this is the case, the capacity of your hard drive might be the limiting factor. One solution is to buffer the data: keep all the data-to-be-written in a list (or some other container) and write everything out at once (or every time a threshold amount is met).

### Optimizing your code

* Read your code again, preferably out loud. Try to simulate in your head what
    happens with some toy input data. Are there any things that stick out?
    Fix these things first.
    * Which parts are tedious to explain?
    * Are there any repetitions?
    * Are there any small helper functions that can be integrated back into the main function because they are oddly specific?
* Check that you're loading prerequisite files only once, and not each time your script
    processes a new document.
* Python built-ins are usually much faster than anything you can write by yourself.
    Check if you're making use of them.
* If you have many list membership checks in your code, check whether you could
    replace those lists by sets.
* If you only loop over a sequence of items once, try to use a generator instead.
* Are you calling a function many times with the same arguments?
    Then the `lru_cache` function might be useful (see [here](https://docs.python.org/3/library/functools.html)).
* If you run out of memory in places where variable reference to one large object
    is replaced by a reference to another large object, the `del` statement might
    be useful (so that Python never keeps *both* objects in memory).
* If you use a lot of if-statements to check for corner cases, consider using
    `try... except` instead. This gets rid of all the unnecessary checks.
* Speaking of unnecessary checks: look at the order of your `if... elif...` statements.
    If you put the most common case first, and the least common case last, the interpreter
    spends less time checking all the statements (because once it finds a match,
    it can skip the rest).
* Try to think about cheap (processing-wise) heuristics that indicate whether or
    not a sentence/file/??? is suitable for further (more intensive and time-consuming)
    processing.
