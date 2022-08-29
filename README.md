# Python for text analysis
*As taught at the Vrije Universiteit Amsterdam in the [Humanities Research Master: Linguistics](http://masters.vu.nl/en/programmes/linguistics-research/index.aspx) (track [Human Language Technology](http://www.cltl.nl/teaching/human-language-technology/)) and the [Minor Digital Humanities and Social Analytics (BA)](https://studiegids.vu.nl/en/minor/2019-2020/minor-digital-humanities-and-social-analytics?_ga=2.61745324.1204416539.1597663557-1095921612.1591712788#study-program).*

In case you have questions about exemption, please first read [Python-test.md](https://github.com/cltl/python-for-text-analysis/blob/master/Assignments/Python-test.md).

This is a practical course in Python, geared towards those who want to get some hands-on experience working with language data.
No knowledge of programming is required or presupposed.
We will work with Python 3.9. We highly recommend installing [Anaconda](https://www.anaconda.com/download) for this course.

(If you have worked with Python 3 before, be sure to check if Jupyter Notebook
is installed on your machine. We will work extensively with notebooks. Make sure you are working with Python 3.9.)

*This course is based on the material used in [previous years](https://github.com/cltl/python-for-text-analysis/releases) and in [this course](https://github.com/kadarakos/python-course).*

## Goals

This course is meant to introduce you to the basics of the Python programming language. There is a lot to discover about Python and programming in general, and you will probably learn something new every day if you continue programming after this course. Our goal for you is to become an independent programmer who is able to find solutions to new problems.

You will

* learn how to work with the standard library of Python
* learn how to deal with different file types (e.g., plain text, CSV/TSV, JSON)
* learn how to use some external libraries (e.g., to analyze texts)
* learn how to document and share your code and results

We will focus on readability and understandability, so that you will be able to share your code and results with others, and re-use your code in the future. This is a practical course, in which you will get a lot of hands-on experience. Due to the nature of this course, active participation is required.

As of 2021-22, we are offering a bachelor- and a master-level version of this course. For the bachelor version, we emphasize applications in Digital Humanities. For the Master-level, we emphasize a more thorough understanding of the fundamentals of python and independent problem-solving. These differences are reflected in the material of the second half of the course (Block III and IV).

## Core principles

We strongly believe in a set of principles
outlined by Mike Bostock in his article
[What makes software good?](https://medium.com/@mbostock/what-makes-software-good-943557f8a488). We have designed our course around those principles and summarized them for you below:

* **Good software is approachable**. It can be understood completely in independent, easy pieces. You don’t need to understand everything before you can understand anything.

* **Good software is consistent**. It lets you take what you’ve learned about one part and extrapolate it to the rest. It doesn’t self-contradict. It is parsimonious, avoiding superfluous elements.

* **Good software explains itself**. It has affordances for learning and discovery. It is role-expressive and minimizes hidden magic.

* **Good software teaches**. It doesn’t just automate an existing task, but provides insight or imparts knowledge, such as a best practice or a new perspective on a problem.

* **Good software is for humans**. It is cognizant of people and the reality in which they live. It does not expect elaborate and arbitrary rules to be memorized. It anticipates the need for learning and debugging.

## What to do if you get stuck

Programming almost always involves running into problems and getting stuck. This is normal and even happens to very experienced programmers. We are trying to offer support to all students, but this means we have to prioritize and manage our time well. In order for this to work, please try to follow these strategies when you get stuck:


* Check the **class material** for solutions. The chapters treated in the assignment are usually a good start. As the course progresses, you may have to also check the material from earlier blocks.
* If you get **error messages**, read them carefully - they are informative! In particular, check the line in which the error occurs and the line immediately preceding it. If you don't understand what it says, try to google it (you will most likely find some explanation on Stackoverflow).
* Break down your task into **small steps using pen and paper**. Sometimes, you lose sight of the bigger picture when dealing with complicated code. Breaking down a big task into small tasks helps you identify the problem.
* **Explain the problem to someone else** (e.g., a classmate). Go through the code line by line and explain what it does (See [pair programming](https://en.wikipedia.org/wiki/Pair_programming) and [rubber duck debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging)).
* Finally, **take a break**! Very often, just having a fresh look at the code helps!
* If none of these steps helped, please try to ask for help well before the assignment deadline. Please start by posting your questions on Piazza.  If you email the teachers or TAs, please always email your code rather than a screenshot.

Learning how to help yourself is a valuable skill and will be very useful in your future programming projects.


## Courseware structure

Our materials are structured as follows:

* The `Chapters` folder contains our primary teaching material. Every week, you will work through a subset of these interactive notebooks. It is highly recommended to start looking at the material in preparation for the lectures. If you get stuck with an assignment, first see if you can find the solution in the Chapters.

* The `Assignments` folder contains the assignments that you will be asked to submit during the course.

* The `Exam` folder contains sample exams from previous years.


* The `Extra_Material` folder contains some extra reading about the Python theory, which you may use for future reference. It also contains some information specifically related to natural language processing, and examples on how to organize your code and how to create a Flask website.

* The `Data` folder contains all data used in this course and more, as well as the scripts used to obtain this data. (So you can see what techniques we used.)

This file serves as the syllabus and a general reference for this course.

## Assignments and Grading

The course is worth 6 ECTS and will consist of **4 assignments** and a **final exam**. The assignments have to be submitted after the content and tutorial session of each block (4 in total). In the third session of each block, we will discuss the assignment in class and provide feedback. The assignments and the exam are weighted as follows.

| Part    | weight % |  Part    | weight % |
|---------|----------|----------|---------|
|Assignment 1| 0*   |  Total Assignments |	60 |
|Assignment 2|	 10  |  Exam	            |	40 |
|Assignment 3|	 20  |    |	 |
|Assignment 4|	 30  |    |	 |
|  **Total** |       |     |	100 |

*Assignment 1 is not graded, but you are required to submit a serious attempt by the deadline to pass the course.


### Course assignments
You are asked to hand in 4 assignments in total. The deadlines are indicated below. Submission 1 day after the deadline and before the feedback session downgrades your grade by 2 (e.g., a 9 will result in a 7).  After that (i.e. on day 2 or after the feedback session has started), the resulting grade is a 1. We have to be strict about this because we will discuss the assignments in class, and we need time to look at your submissions. In addition, the solutions will be discussed in the feedback session, and we cannot award points after the solutions have been discussed.


Please note that a passing grade for the assignments (in total) is a requirement for passing the course and you need at least a 5.0 for the final assignment (regular assignment or resit assignment).

### Assignment submissions

Submission is made through Canvas. Please submit your assignments using the corresponding assignment submission on Canvas (e.g. labeled 'Assignment 1' for Assignment 1).

Please note that we cannot accept assignments submitted via email.

### Resits for Assignments

We provide a resit opportunity for each assignment at the end of the course (deadline will be announced). The maximum grade for the resit assignments is 7.5.

The following Assignments have to be completed as resits for the regular assignments. The deadline for the resit assignments will be announced at the end of the course.

| Assignment    | Resit |
|---------|----------|
|Assignment 1| Resit part A (serious attempt)  |
|Assignment 2|	Resit part A  |
|Assignment 3|	Resit part B  |   
|Assignment 4|	 Resit part C  |    

**It is highly recommended to aim for passing grades at the first attempt. Please only make use of the resit opportunities in case you failed an assignment or were dealing with exceptional circumstances (e.g. illness).**


### Final exam
The exam tests your knowledge of the syntax of Python, and your knowledge of the standard library. It serves as an opportunity to show what you've learned and will ensure that you have sufficient knowledge to tackle your own code projects and continue improving your python skills by yourself. You cannot pass the course without a passing grade on the exam. But don't worry: if you are able to finish the assignments, you will be fine on the exam.

### Resit exam

There will be an opportunity to take a resit exam. The exact date will be announced.

**It is highly recommended to aim for a passing grade at the regular exam date. Please only make use of the resit exam if you fail the regular exam or were dealing with exceptional circumstances (e.g. exam date conflict, illness).


## Planning
There are 4 Blocks with associated chapters and assignments:

| Block   | Chapters BA | Chapters MA | Assignment BA | Assignment MA |
|---------|---------|---------|-----|----|
| I | Chapters 1-4 | Chapters 1-4 |	 Assignment 1 | Assignment 1 |
| II |Chapters 5-11  |  Chapters 5-11 |Assignment 2 | Assignment 2 |
| III |Chapters 12-15 | Chapters 12-15 |	Assignments 3a and 3b (Exercises 3 and 4 of Assignment 3b are excluded for BA students)	| Assignments 3a and 3b	|
| IV |Chapters 16, 17, 22 | Chapters 16-18 | Assignments 4a and 4b-BA | Assignments 4a and 4b-MA |

The schedule for the entire course follows the same structure, illustrated below.

All blocks except block IV will consist of three lectures. There is one additional lecture for block IV.

**Lecture 1**

In the first lecture, we introduce some of the new topics. It is highly recommended to go through the chapter notebooks in preparation for the classes. After the first lecture, you are expected to start working on the assignment and consult the chapters for things that are unclear to you. Please be aware that the assignments can most likely not be completed in a single day. Also, solving code problems is much easier if you have **sufficient time for breaks**.

**Lecture 2**

In the second lecture, we will further highlight some of the theory, and you will have time to work on the assignment in class. Support will be provided by the teachers and student assistants. It is highly recommended to prepare questions you have about the assignment. We will dedicate time TO this in this lecture. You will finish the assignment between the second and third lecture and hand it in on either Tuesday or Friday.

**Lecture 3**

Finally, the third lecture is a feedback session where we will discuss some of the main problems that were encountered in the assignments. We will repeat this cycle 4 times (for each assignment).




| week | what     | when                   | description           |
|------|----------|------------------------|-----------------------|
|  36  | lecture  | Monday 2022-09-05 <br> 15:30 - 17:15 | BLOCK 1: Introduction theory |
|  36  | lecture  | Thursday 2022-09-08 <br> 13:30 - 15:15  | BLOCK 1: Theory and work time |  
|  36  | DEADLINE  | Friday 2022-09-09 <br> before 17:00  | SUBMIT ASSIGNMENT 1 |
|  37 | lecture  | Monday 2022-09-12  <br> 15:30 - 17:15 |  BLOCK 1: Feedback assignment |  
|  37  | lecture  | Thursday 2022-09-15  <br> 13:30 - 15:15 |  BLOCK 2: Introduction theory |  
|  38  | lecture  | Monday 2022-09-19 <br> 15:30 - 17:15 |  BLOCK 2: Theory and work time |  
|  38  | DEADLINE  | Tuesday 2022-09-20 <br> before 17:00  | SUBMIT ASSIGNMENT 2 |
|  38  | lecture  | Thursday 2022-09-22  <br> 13:30 - 15:15 |  BLOCK 2: Feedback assignment |  
|  39  | lecture  | Monday 2022-09-26 <br> 15:30 - 17:15 |  BLOCK 3: Introduction theory |  
|  39  | lecture  | Thursday 2022-09-29 <br> 13:30 - 15:15  | BLOCK 3: Theory and work time |  
|  39  | DEADLINE  | Friday 2022-09-30 <br> before 17:00  | SUBMIT ASSIGNMENT 3 |
|  40  | lecture  | Monday 2022-10-03 <br> 15:30 - 17:15  |  BLOCK 3: Feedback assignment |  
|  40  | lecture  | Thursday 2022-10-06 <br> 13:30 - 15:15  |  BLOCK 4: Introduction theory |
|  41  | lecture  | Monday 2022-10-10 <br> 15:30 - 17:15   |  BLOCK 4: Theory and work time |  
|  41  | lecture  | Thursday 2022-10-13 <br> 13:30 - 15:15  | BLOCK 4: Theory and work time  |
|  41  | DEADLINE  | Friday 2022-10-14 <br> before 17:00  | SUBMIT ASSIGNMENT 4  |
|  42  | lecture  | Monday 2022-10-17  <br> 15:30 - 17:15 | BLOCK 4: Feedback assignment |  
|  42  | lecture  | Thursday 2022-10-20  <br> 13:30 - 15:15 |  Exam preparation |
|  43  | EXAM  | Tuesday 2022-10-25 <br> 8:30-11:15 (11:45, extra time)  |  EXAM |


## Plagiarism
Cheating is serious: it is considered fraud and can lead to being excluded from your studies (https://vu.nl/en/student/your-faculty/examination-board). It is also harmful: not only for yourself (you can fool yourself and fail to learn this useful skill), but also for other students (if multiple students do better because of cheating, teachers may think a grading scheme is fair, even though it needs to be adjusted).

How to avoid this, while making use of online sources and working together:

For the weekly assignments, let us know in the comments if you have worked together with someone or if you used code from online sources, such as [stackoverflow](http://stackoverflow.com/). If you found some useful code online, do try to understand what that piece of code does. If it looks 'complicated', we expect you to provide comments in the code explaining what it does.

If you use code you found online in an assignment, please indicate it in the following way:

```
### Taken from [link] [date]

[code]

\###
```

Please use a similar format to indicate that you have worked with a classmate (e.g. mention the name instead of the link). Make sure to provide your own comments to show that you understood and indicate what you did yourself, e.g. by commenting your partial solution out (we cannot give credits for copy-pasting full answers from classmates, but you may get full points for a partial individual solution and well commented working one with components from a classmate). If you work on a solution together, also indicate this and make sure to provide individual explanations.
