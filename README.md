# Python for text analysis
*As taught at the Vrije Universiteit Amsterdam in the Research MA Linguistics, track [Linguistic Engineering](http://www.cltl.nl/teaching/research-master-linguistic-engineering/).*

This is a practical course in Python, geared towards those who want to get some hands-on experience working with language data.
No knowledge of programming is required or presupposed.
We will work with Python 3. If you haven't worked with Python before, we recommend that you install [Anaconda](https://www.continuum.io/downloads).

(If you have worked with Python 3 before, be sure to check if Jupyter Notebook
is installed on your machine. We will work extensively with notebooks.)

## Goals

After this course you will know the basics of the Python programming language, and you will be familiar with several external libraries that are commonly used to analyze text. Our goal is for you to become an independent programmer, who is able to find solutions to new problems. You will..

*	Learn how to analyze text data using Python.
*	Learn how to deal with different file types (plain text, doc, CSV, JSON, HTML, XML).
*	Learn how to get the data you want (through APIs or using a script).
*	Learn how to deal with large amounts of (text) data.
*	Learn how to visualize and share your code and results.

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

* Notebooks can be found in the `Notebooks` folder. This is our primary teaching material. You will work through an interactive notebook every week.

* Chapters on Python can be found in the `Python-chapters` folder. You can use these chapters for future reference.

* Other topics, related to natural language processing and 'everyday work' are covered
  in the `NLP-topics` folder. So if you're just here to learn Python, you can skip these
  notebooks. You may still find them useful, however!

* The `Data` folder contains all data used in this course, and scripts used to obtain
  this data. (So you can see what techniques we used.)

This file serves as the syllabus and a general reference for this course.

## Assignments and Grading

There will be weekly assignments, a midterm exam, and a final assignment. They are weighted as follows.

| Part    | weight % | | Part    | weight % |
|---------|---------|---|---------|---------|
|Assignment 1|	 4  | | Total Assignments |	35 |
|Assignment 2|	 4  | | Exam	            |	20 |
|Assignment 3|	 9  | | Final assignment  |	45 |
|Assignment 4|	 9  | | **Total**         |	100 |
|Assignment 5|	 9  | | | |
|**Total Assignments** |	35 | | | |

### Weekly assignments
Every week you are asked to hand in an assignment before Tuesday 15:00pm.
Submission is done through Blackboard.
There are three possible grades for an assignment: **not OK (5)**, **OK (7)**, and **good (9)**.
Submission after the deadline results in one point deduction of your grade.
In addition, we do not guarantee feedback if your submission is after the deadline.
You have to hand in all assignments in order to be able to get a passing grade for the course. We use these assignments to keep
track of your progress in the course, and to address misunderstandings when they arise.
As practice is essential to learn how to program, and since these assignments also serve
as a feedback mechanism in the course (keeping track of your progress), the assignments
are **mandatory.**

### Midterm exam
The midterm exam on the 15th of December tests your knowledge of the syntax of Python, and your knowledge
of the standard library. It also tests whether you are able to write simple functions
in Python. This knowledge is fundamental to the rest of the course. As such, you cannot
pass the course without a passing grade on the midterm. But don't worry: if you are able
to finish the assignments, you will be fine on the exam.

### The final assignment
The final part of the course consists of a final assignment, for which you will work on your own code project.
As part of the final assignment, we ask you to present your work.
You will not receive a grade for this presentation, but it is compulsory.
You can use the feedback on your presentation to improve your project.

The exact details of the final assignment are to be determined. If you come up with
an interesting task of your own, we are happy to turn that into an assignment as well.

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

After the introductory session, assignments will be given on Thursday. You can
work on these assignments in class and at home. We'll have a Q&A session on Monday,
along with additional theory. We'll also work on the assignments in class. Assignments
are handed in on Tuesday, so we can check everything in time for Thursday where you
will receive feedback and get the new assignment.

In order to download a notebook about a Topic or an Assignment, please right click on the link in the schedule below and save the file in your course materials.

| week | what     | when                   | preparation           | description |
|------|----------|------------------------|-----------------------|-------------|
|  44  | lecture  | 31-10-2016 11:00-12:45 | None                  | Introduction + start of topic 1 |
|  44  | lecture  | 3-11-2016 11:00-12:45  | [Topic 1](https://raw.githubusercontent.com/evanmiltenburg/python-for-text-analysis/master/Notebooks/Topic%201%20-%20Getting%20started.ipynb)               | discussion topic 1 + start of topic 2 + introduction assignment 1 |
|  45  | lecture  | 7-11-2016 11:00-12:45  | [Topic 2](https://raw.githubusercontent.com/evanmiltenburg/python-for-text-analysis/master/Notebooks/Topic%202%20-%20Understanding%20string%20and%20list%20methods%20%2B%20boolean%20expressions%20%2B%20if%20statements.ipynb)              | discussion topic 2 + working on assignment 1 |
|  45  | deadline | 8-11-2016 15:00        | [Assignment 1](https://raw.githubusercontent.com/evanmiltenburg/python-for-text-analysis/master/Notebooks/ASSIGNMENT-1.ipynb)          | |
|  45  | lecture  | 10-11-2016 11:00-12:45 |                       | feedback assignment 1 + start of topic 3 + introduction assignment 2 |
|  46  | lecture  | 14-11-2016 11:00-12:45 | [Topic 3](https://raw.githubusercontent.com/evanmiltenburg/python-for-text-analysis/master/Notebooks/Topic%203%20-%20Diving%20into%20files%20and%20data%20formats.ipynb) <br> [Data](https://github.com/evanmiltenburg/python-for-text-analysis/blob/master/Data.zip)               | discussion topic 3 + working on assignment 2 |
|  46  | lecture  | 17-11-2016 11:00-12:45 |                       | working on assignment 2 |
|  47  | lecture  | 21-11-2016 11:00-12:45 |                       | working on assignment 2 |
|  47  | deadline | 22-11-2016 15:00       | [Assignment 2](https://raw.githubusercontent.com/evanmiltenburg/python-for-text-analysis/master/Notebooks/ASSIGNMENT-2.ipynb)          |  |
|  47  | lecture  | 24-11-2016 11:00-12:45 |                       | feedback assignment 2 + start of topic 4 + introduction assignment 3 |
|  48  | lecture  | 28-11-2016 11:00-12:45 | [Topic 4](https://raw.githubusercontent.com/evanmiltenburg/python-for-text-analysis/master/Notebooks/Topic%204%20-%20Getting%20and%20processing%20data.ipynb)               | discussion topic 5 + working on assignment 4 |
|  48  | deadline | 30-11-2016 17:00       | [Assignment 3](https://raw.githubusercontent.com/evanmiltenburg/python-for-text-analysis/master/Notebooks/ASSIGNMENT-3.ipynb)          |  |
|  48  | lecture  | 1-12-2016 11:00-12:45  |                       | feedback assignment 3 + start of topic 5 + introduction assignment 4 |
|  49  | lecture  | 5-12-2016 11:00-12:45  | [Topic 5](https://github.com/evanmiltenburg/python-for-text-analysis/raw/master/Notebooks/Topic%205%20-%20XML%20and%20conversion.ipynb)               | discussion topic 5 + working on assignment 4 |
|  49  | deadline | 6-12-2016 15:00        | [Assignment 4](https://github.com/evanmiltenburg/python-for-text-analysis/raw/master/Notebooks/ASSIGNMENT-4.ipynb)          | |
|  49  | lecture  | 8-12-2016 11:00-12:45  |                       | feedback assignment 4 + introduction practice exam |
|  50  | lecture  | 12-12-2016 11:00-12:45 | practice exam         | discussion practice exam + QA session exam |
|  50  | deadline | 15-12-2016 11:00-12:45 |                       | Exam |
|  51  | lecture  | 19-12-2016 11:00-12:45 |                       | introduction final assignment |
|  51  | lecture  | 22-12-2016 11:00-12:45 |                       | Exam feedback + working on final assignment |
|  52  |          |                        |                       | Christmas break |
|  1   |          |                        |                       | Christmas break |
|  2   | lecture  | not known yet          |                       | noncompulsory (due to LOT school) QA session final assignment |
|  2   | lecture  | not known yet          |                       | noncompulsory (due to LOT school) QA session final assignment |
|  3   | lecture  | not known yet          |                       | noncompulsory (due to LOT school) QA session final assignment |
|  3   | lecture  | not known yet          |                       | noncompulsory (due to LOT school) QA session final assignment |
|  4   | lecture  | not known yet          |                       | working on final assignment |
|  4   | lecture  | not known yet          |                       | working on final assignment  |
|  5   | lecture  | not known yet          |                       | working on final assignment  |
|  5   | deadline | not known yet          |                       | Presentation final assignment  |
|  5   | deadline | 5-2-2017 23:59         |                       | Final assignment  |

## Attendance policy
You are expected to attempt to attend all lectures. You are allowed to miss two lectures at most. After more than two absences, you are no longer able to obtain credits for the course.  

## Plagarism
Basically, please don't cheat. For the weekly assignments, let us know in the comments if you have worked together with someone or if you used code from online sources, such as [stackoverflow](http://stackoverflow.com/). If you found some useful code online, do try to understand what that piece of code does. If it looks 'complicated', we expect you to provide comments in the code explaining what it does.
