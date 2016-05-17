# Reproducibility

Reprodicibility is becoming more and more important across all fields of scientific
inquiry. Let's first start with a bit of terminology (cf. [here](http://simplystatistics.org/2011/12/02/reproducible-research-in-computational-science/),
but note that sometimes these terms are used interchangeably):

* **Reproducing** results means that you can use the same data and tools as someone
    else and get the same results.
* **Replicating** results means that you can use the same tools on different data
    and observe the same effects.

These two concepts are fundamental to doing good science. If your research is at
least reproducible, that means that other researchers can build on your results.
If your code can be used to study the same effects (or extract similar information)
from different data, that means your ideas can have greater impact.

In class, we will discuss [this paper](http://aclweb.org/anthology//P/P13/P13-1166.pdf),
showing the importance of keeping notes about your work. Every detail matters.
The paper mentions:

* How you are preprocessing the data.
* The version of the software you are using.
* The parameter settings for your algorithm.
* Random variation.

## Guidelines

At the Computational Lexicology and Terminology Lab (CLTL), we use [this policy](./misc/publication_policy.md)
for all publications. This not only ensures that others can build on our results,
but it also makes life easier for ourselves:

* Our data is organized better.
* It's easier to pick up where you left off.
* There are fewer questions from others "how did you do XYZ?"

## Useful techniques

Now how do you carry out reproducible research? Here are several useful techniques that can help you write better code:

* **Using Argparse.** The built-in [argparse](https://docs.python.org/3/library/argparse.html)
    module makes it easier to use command-line arguments. This enables you to run your
    code with different sets of parameters each time. With argparse, you don't have to
    change anything about the code itself. Just provide the script with a different set
    of parameters. This is also very useful if you want to run the same analysis on
    different datasets.

* **Logging your runs.** The built-in [logging](https://docs.python.org/3.5/library/logging.html)
    module lets you log what your scripts do. [The tutorial in the module's documentation](https://docs.python.org/3.5/howto/logging.html#logging-basic-tutorial) describes it as follows:
    > Logging is a means of tracking events that happen when some software runs. The software’s developer adds logging calls to their code to indicate that certain events have occurred. An event is described by a descriptive message which can optionally contain variable data (i.e. data that is potentially different for each occurrence of the event). Events also have an importance which the developer ascribes to the event; the importance can also be called the level or severity.
    
    You can also use the `logging` module to store the command-line arguments.

* **Seeding the randomization function.** If your code contains a randomization
    function, the results are likely to differ with each run. If you supply a *seed*
    value, however, the random number generator will produce the same set of pseudorandom
    numbers each time while the generated numbers still seem random. Use `random.seed(1234)`
    to do this. (An alternative would be to run your script a hundred times and report the
    mean and the standard deviation. If someone were to run your script again, the result
    should fall within that distribution.) Note that it is considered *bad science* to experiment
    with the seed value until you get the best result and only report that result.

* **Testing your code.** Testing means that you write additional code to see if your
    functions do what they are supposed to do. Ned Batchelder has
    [a good video about it](http://nedbatchelder.com/text/test0.html).

* **Documenting as you write.** This bears repeating:
    * Every time you write a function, start with the docstring: what do you expect
    the function to do? You could even add [doctest](https://docs.python.org/3.5/library/doctest.html)-style examples of
    input and output. (In that case, you already have some tests!)
    * Once you have a plan for what you want to do, write it down in the README.
    Especially hypotheses, structure of your code, structure of the data.
    * If you get stuck and find an answer online somewhere, add the URL to that
    answer in your code. Just have couple of lines saying something like:
    ```python
    # The following bit of code is taken from here:
    # http://www.stackoverflow.com/...
    ```
    And proceed to explain the code in the comments. (If you don't understand it,
    don't use it.)
