# Python for text analysis
*As taught at the Vrije Universiteit Amsterdam in the [Humanities Research Master: Linguistics](http://masters.vu.nl/en/programmes/linguistics-research/index.aspx) (track [Human Language Technology](http://www.cltl.nl/teaching/human-language-technology/)) and the [Minor Digital Humanities and Social Analytics (BA)](https://www.vu.nl/nl/studiegids/2017-2018/minor/c-d/digital-humanities/index.aspx).*

This is a practical course in Python, geared towards those who want to get some hands-on experience working with language data.
No knowledge of programming is required or presupposed.
We will work with Python 3. If you haven't worked with Python before, we recommend that you install [Anaconda](https://www.continuum.io/downloads).

(If you have worked with Python 3 before, be sure to check if Jupyter Notebook
is installed on your machine. We will work extensively with notebooks.)

*This course is based on the material used in [previous years](https://github.com/cltl/python-for-text-analysis/releases) and in [this course](https://github.com/kadarakos/python-course).*

## Goals

This course is meant to introduce you to the basics of the Python programming language. There is a lot to discover about Python and programming in general, and you will probably learn something new every day if you continue programming after this course. Our goal for you is to become an independent programmer, who is able to find solutions to new problems. You will..

* Learn how to work with the standard library of Python
*	Learn how to deal with different file types (e.g. plain text, CSV/TSV, JSON, XML)
*	Learn how to use some external libraries (e.g. to analyse texts)
*	Learn how to document and share your code and results

We will focus on readability and understandability, so that you will be able to share your code and results with others, and re-use your code in the future. This is a practical course, in which you will get a lot of hands-on experience. Due to the nature of this course, active participation is required.

## Core principles

Every course has a set of core principles that its teachers adhere to.
We strongly believe in the principles outlined by Mike Bostock in his article
[What makes software good?](https://medium.com/@mbostock/what-makes-software-good-943557f8a488) Here they are:

* **Good software is approachable**. It can be understood completely in independent, easy pieces. You don’t need to understand everything before you can understand anything.

* **Good software is consistent**. It lets you take what you’ve learned about one part and extrapolate it to the rest. It doesn’t self-contradict. It is parsimonious, avoiding superfluous elements.

* **Good software explains itself**. It has affordances for learning and discovery. It is role-expressive and minimizes hidden magic.

* **Good software teaches**. It doesn’t just automate an existing task, but provides insight or imparts knowledge, such as a best practice or a new perspective on a problem.

* **Good software is for humans**. It is cognizant of people and the reality in which they live. It does not expect elaborate and arbitrary rules to be memorized. It anticipates the need for learning and debugging.

## The 15 minute rule

When you are just learning how to program, it sometimes happens that you get stuck and you don't know what to do next. This is normal.
There are many fantastic resources online that we encourage you to use to solve your problem on your own. But we don't want this to be a frustrating experience for you. So if you're stuck for more than 15 minutes: please contact us! No matter how small the problem. If you're stuck, you're stuck.

In our experience it does help to solve the exercises together with a classmate. (See [pair programming](https://en.wikipedia.org/wiki/Pair_programming) and [rubber duck debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging).) If either one of you gets stuck, try to explain the thought process behind your program, and go through the lines step by step. Making your thought process explicit is a great way to find bugs in your code!

## Courseware structure

Our materials are structured as follows:

* The `Chapters` folder contains our primary teaching material. Every week, you will work through a subset of these interactive notebooks.

* The `Class_Notes` folder contains the examples and additional remarks that we discussed during class.

* The `Assignments` folder contains the assignments that you will be asked to submit during the course.

* The `Exam` folder contains sample exams from previous years.

* The `Final_Assignment` folder contains the instructions and data needed for the final assignment (only for the MA students).

* The `Extra_Material` folder contains some extra reading about the Python theory which you may use for future reference. It also contains some information specifically related to natural language processing, and examples on how to organize your code and how to create a Flask website. 

* The `Data` folder contains all data used in this course and more, as well as the scripts used to obtain
  this data. (So you can see what techniques we used.)

This file serves as the syllabus and a general reference for this course.

## Assignments and Grading

For the ReMa students taking the 9 ECTS Python for Text Analysis course (L_AAMPLIN017), there will be bi-weekly assignments, an exam, and a final assignment. They are weighted as follows.

| Part    | weight % | | Part    | weight % |
|---------|---------|---|---------|---------|
|Assignment 1|	 5  | | Total Assignments |	35 |
|Assignment 2|	 10  | | Exam	            |	20 |
|Assignment 3|	 10  | | Final assignment  |	45 |
|Assignment 4|	 10  | |   |	 |
| |	   | | **Total**         |	100 |
|**Total Assignments** |	35 | | | |


For the BA students taking the 6 ECTS Programming for Humanities and Social Sciences course (L_AABAALG069), there will be bi-weekly assignments and an exam. These students will **not** do a final assignment. The assignments and exam are weighted as follows.

| Part    | weight % | | Part    | weight % |
|---------|---------|---|---------|---------|
|Assignment 1|	 9  | | Total Assignments |	60 |
|Assignment 2|	 17  | | Exam	            |	40 |
|Assignment 3|	 17  | |   |	 |
|Assignment 4|	 17  | |   |	 |
| |	   | | **Total**         |	100 |
|**Total Assignments** |	60 | | | |


### Weekly assignments
You are asked to hand in 4 assignments in total. The deadlines are either on Friday before 23:59 or on Tuesday at 20:00.
Submission is done through Google Drive (see submission forms below in the schedule).
Submission 1 day after the deadline results in two points deduction of your grade. After that, the resulting grade is a 1.
We have to be strict about this, because we will discuss the assignments in class and we need time to look at your submissions. 

### Midterm exam
The exam on the 18th of December tests your knowledge of the syntax of Python, and your knowledge
of the standard library. For the BA students, it is the final test to show what you have learnt. For the MA students, it serves as a check to assure that your knowledge of the language is sufficient to tackle the final assignment. You cannot
pass the course without a passing grade on the exam. But don't worry: if you are able
to finish the assignments, you will be fine on the exam.

### The final assignment
The final part of the MA course consists of a final assignment, for which you will work on your own code project. The exact details of the final assignment will be announced later.

You can expect a project in which you are asked to:

1. process a number of files;
2. extract relevant information from those files;
3. present that information to the user;
4. store the information in a useful format

We will consider the following questions (along with the core principles) to evaluate your final assignment:

* Does the code work?
* Does the code fulfill the requirements?
* Is the code well-documented?
* Is the code clear and understandable?
* Is the code modular?
* Is the code easily extensible?
* How scalable is the solution?
* Is the code written in accordance with [the community standards](http://pep8.org/)? (That is: PEP8)
* Are there tests to ensure that the code works?

## Planning
The schedule for the entire course follows the same structure, illustrated below.
Our philosophy is that programming should be taught in a hands-on manner, so we tried
to reduce 'powerpoint time' to a minimum. Most theory is mainly taught through the
notebooks, but we'll also address the major topics in class.

Each Block will consist of three lectures. In the first lecture, we introduce some of the new topics. 
After this lecture, you are expected to work through the Chapters belonging to this block and start on the assignment. 
In the second lecture, we will further highlight some of the theory and you will have time to work on the assignment.
You will finish the assignment between the second and third lecture, and hand it in on either Friday or Thursday.
Finally, the third lecture is a feedback session where we will discuss some of the main problems that were encountered in the assignments. We will repeat this cycle 4 times (for each assignment).

New material will be added to this Github repository during the course. For downloading the material, please right click on the links in the schedule below and save the file in your course materials. Save the `Chapter X` notebooks in your `Chapters` folder, the `Assignment X` notebooks in your `Assignments` folder. If additional `data` is provided, save it in the `Data` folder.

| week | what     | when                   | description           | downloads/uploads |
|------|----------|------------------------|-----------------------|-------------|
|  44  | lecture  | Monday 30-10-2017 <br> 15:30 - 17:15 | BLOCK 1: Introduction | [Chapter 1](https://github.com/cltl/python-for-text-analysis/raw/master/Chapters/Chapter%201%20-%20Getting%20Started%20with%20Variables%20and%20Values.ipynb) <br>  [Chapter 2](https://github.com/cltl/python-for-text-analysis/raw/master/Chapters/Chapter%202%20-%20Basic%20Data%20Types%20(Integers%20and%20Floats).ipynb) <br> [Chapter 3](https://github.com/cltl/python-for-text-analysis/raw/master/Chapters/Chapter%203%20-%20Strings.ipynb) <br> [Chapter 4](https://github.com/cltl/python-for-text-analysis/blob/master/Chapters/Chapter%204%20-%20Boolean%20Expressions%20and%20Conditions.ipynb) <br> [Assignment 1](https://github.com/cltl/python-for-text-analysis/raw/master/Assignments/ASSIGNMENT-1.ipynb)|
|  44  | lecture  | Thursday 2-11-2017 <br> 13:30 - 15:15  | BLOCK 1: Discussion and work time | [Class Notes](https://github.com/cltl/python-for-text-analysis/raw/master/Class_Notes/Class%20Notes%202-11-2017%20(Block%20I).ipynb) |
|  44  | DEADLINE  | Friday 3-11-2017 <br> before 23:59  | SUBMIT ASSIGNMENT 1 | [submission form](https://goo.gl/forms/0DfPcX9cLbSzLdet1) |
|  45  | lecture  | Monday 6-11-2017  <br> 15:30 - 17:15 |  BLOCK 1: Feedback |  |
|  45  | lecture  | Thursday 9-11-2017  <br> 13:30 - 15:15 |  BLOCK 2: Introduction | [Chapter 5](https://raw.githubusercontent.com/cltl/python-for-text-analysis/master/Chapters/Chapter%205%20-%20Containers'%20core%20concepts.ipynb) <br> [Chapter 6](https://raw.githubusercontent.com/cltl/python-for-text-analysis/master/Chapters/Chapter%206%20-%20Lists.ipynb) <br> [Chapter 7](https://raw.githubusercontent.com/cltl/python-for-text-analysis/master/Chapters/Chapter%207%20-%20Sets.ipynb) <br> [Chapter 8](https://raw.githubusercontent.com/cltl/python-for-text-analysis/master/Chapters/Chapter%208%20-%20Comparison%20of%20lists%20and%20sets.ipynb) <br>  [Chapter 9](https://raw.githubusercontent.com/cltl/python-for-text-analysis/master/Chapters/Chapter%209%20-%20Looping%20over%20containers.ipynb) <br> [Chapter 10](https://raw.githubusercontent.com/cltl/python-for-text-analysis/master/Chapters/Chapter%2010%20-%20Dictionaries.ipynb) <br> [Assignment 2](https://raw.githubusercontent.com/cltl/python-for-text-analysis/master/Assignments/ASSIGNMENT-2.ipynb) |
|  46  | lecture  | Monday 13-11-2017  <br> 15:30 - 17:15 |  BLOCK 2: Discussion and work time |  |
|  46  | DEADLINE  | Tuesday 14-11-2017 <br> before 20:00  | SUBMIT ASSIGNMENT 2 | [submission form](https://goo.gl/forms/4OidikfRfz229WNW2) |
|  46  | lecture  | Thursday 16-11-2017  <br> 13:30 - 15:15 |  BLOCK 2: Feedback |  |
|  47  | lecture  | Monday 20-11-2017 <br> 15:30 - 17:15  |  BLOCK 3: Introduction |  |
|  47  | lecture  | Thursday 23-11-2017 <br> 13:30 - 15:15  | BLOCK 3: Discussion and work time |  |
|  47  | DEADLINE  | Friday 24-11-2017 <br> before 23:59  | SUBMIT ASSIGNMENT 3 | [submission form](https://goo.gl/forms/6iTiRiZk4z8W68UE3) |
|  48  | lecture  | Monday 27-11-2017 <br> 15:30 - 17:15  |  BLOCK 3: Feedback |  |
|  48  | lecture  | Thursday 30-11-2017 <br> 13:30 - 15:15  |  BLOCK 4: Introduction |  |
|  49  | lecture  | Monday 4-12-2017 <br> 15:30 - 17:15  |  BLOCK 4: Discussion and work time |  |
|  49  | DEADLINE  | Tuesday 5-12-2017 <br> before 20:00  | SUBMIT ASSIGNMENT 4  | [submission form](https://goo.gl/forms/Zjf24oobU5Ab5yAD3) |
|  49  | lecture  | Thursday 7-12-2017  <br> 13:30 - 15:15 | BLOCK 4: Feedback |  |
|  50  | lecture  | Monday 11-12-2017 <br> 15:30 - 17:15  | Practice EXAM  |  |
|  50  | lecture  | Thursday 14-12-2017  <br> 13:30 - 15:15 |  Practice EXAM |  |
|  51  | EXAM  | Monday 18-12-2017 <br> 08:45 - 11:30  |  EXAM |  |
|  51  | lecture  | Thursday 21-12-2017  <br> 13:30 - 15:15 |  Introduction FINAL ASSIGNMENT |  |


## Attendance policy
You are expected to attempt to attend all lectures. You are allowed to miss two lectures at most. After more than two absences, you are no longer able to obtain credits for the course.  

## Plagiarism
Basically, please don't cheat. For the weekly assignments, let us know in the comments if you have worked together with someone or if you used code from online sources, such as [stackoverflow](http://stackoverflow.com/). If you found some useful code online, do try to understand what that piece of code does. If it looks 'complicated', we expect you to provide comments in the code explaining what it does.
