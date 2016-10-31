# Frequently asked questions

#### Which brackets should I use?

* **Parentheses** are used to define *tuples*  and to call functions.
* **Curly braces** are used to define sets and dictionaries.
* **Square brackets** are used to define *lists*, for indexing, 
slicing, and to get the value for a particular key in a dictionary.


| Kind | Example | What does this do? |
|------|---------|--------------------|
| Tuple | `x = (1,2,3)` | Make `x` refer to a *tuple* with the values 1,2, and 3. |
| Function | `print("Hello, world!")`| *Call* the print function to display the string "Hello, world!" |
| Dictionary | `d = {'apples': 1, pears: 2}` | Make `d` refer to a dictionary containing the keys "apples" and "pears", and their corresponding values. |
| Set | `x = {1, 2, 3}` | Make `x` refer to a *set* containing the values 1,2, and 3. |
| List | `x = [1,2,3]` | Make `x` refer to a *list* with the values 1,2, and 3. |
| Indexing | `y = x[0]` | Make `y` refer to the first element of `x` |
| Slicing | `y = x[:2]` | Make `y` refer to the first two elements of `x` |
| Dictionary | `y = d['apples']` | Get the *value* corresponding to the *key* "apples" from the dictionary `d`. |

#### What is the difference between functions and methods?

* **Methods** are functions that are defined for specific types of objects. One 
example is the method used to make a string lowercase: `'Word'.lower()`. Methods
are always called using the dot-notation.
* **Function** is a more general term. Functions are like variables, but instead of referring
to specific values, they refer to chunks of code. If you call a function (using the parentheses), 
the corresponding chunk of code will be executed.

#### What is Jupyter, and what is the difference between Jupyter and Python?

Python is a programming language that you can use to give instructions to the computer. 
If you run a bit of Python code, your computer will use a *Python-interpreter* to 
understand what you would like the computer to do. The official Python-interpreter is 
called *CPython*. 

Jupyter is a program that allows you to run Python code through a browser-based interface.
It works using a special file format called 'Jupyter notebooks' (previously known as 'iPython notebooks',
which is why the file extension is still `.ipynb`). We really like this programming
environment, because it is very powerful, and you can use it to write reports about
your research. Because these notebooks are executable, you can give them to someone 
else, and they'll be able to reproduce your results. This is extremely useful for 
scientific research.

Anaconda provides a Python distribution with loads of useful pre-installed modules.
The developers of Anaconda have tried to make it as easy as possible to use Python
on any major operating system. Before Anaconda, it was very hard to install some 
modules if you happened to have the wrong operating system, or the wrong computer 
configurations. With Anaconda, we haven't had any issues with students not being
able to install Python on their laptops.
