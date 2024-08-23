# Python for text analysis

*As taught at the Vrije Universiteit Amsterdam in the [Humanities Research Master: Linguistics](http://masters.vu.nl/en/programmes/linguistics-research/index.aspx) (track [Human Language Technology](http://www.cltl.nl/teaching/human-language-technology/)) and the [Minor Digital Humanities and Social Analytics (BA)](https://studiegids.vu.nl/en/minor/2019-2020/minor-digital-humanities-and-social-analytics?_ga=2.61745324.1204416539.1597663557-1095921612.1591712788#study-program).*

In case you have questions about exemption, please first read [Python-test.md](https://github.com/cltl/python-for-text-analysis/blob/master/Assignments/Python-test.md).

This is a practical course in Python, geared towards those who want to get some hands-on experience working with language data.
No knowledge of programming is required or presupposed.
We will work with Python 3.9 or higher. We highly recommend installing [Anaconda](https://www.anaconda.com/download) for this course.

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

Since 2021-22, we have been offering a bachelor- and a master-level version of this course. For the bachelor version, we emphasize applications in Digital Humanities. For the Master-level, we emphasize a more thorough understanding of the fundamentals of python and independent problem-solving. These differences are reflected in the material of the second half of the course (Block III and IV).

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

Programming almost always involves running into problems and getting stuck. This is normal and even happens to very experienced programmers. We are trying to offer support to all students, but this means we have to prioritize and manage our time well. In order for this to work, please try to follow the following strategies when you get stuck:


* Check the **class material** for solutions. The chapters treated in the assignment are usually a good start. As the course progresses, you may have to also check the material from earlier blocks.
* If you get **error messages**, read them carefully - they are informative! In particular, check the line in which the error occurs and the line immediately preceding it. If you don't understand what it says, try to google it (you will most likely find some explanation on Stackoverflow).
* Break down your task into **small steps using pen and paper**. Sometimes, you lose sight of the bigger picture when dealing with complicated code. Breaking down a big task into small tasks helps you identify the problem.
* **Explain the problem to someone else** (e.g., a classmate). Go through the code line by line and explain what it does (See [pair programming](https://en.wikipedia.org/wiki/Pair_programming) and [rubber duck debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging)).
* Finally, **take a break**! Very often, just having a fresh look at the code helps!
* If none of these steps helped, please try to ask for help well before the assignment deadline. Please start by posting your questions on Piazza.  If you email the teachers or TAs, please always email your code rather than a screenshot.

Learning how to help yourself is a valuable skill and will be very useful in your future programming projects.


## Courseware structure

Our materials are structured as follows:

* The `Chapters` folder contains our primary teaching material. Every week, you will work through a subset of these interactive notebooks. We expect you to look at the material in preparation for the lectures. If you get stuck with an assignment, first see if you can find the solution in the Chapters.

* The `Assignments` folder contains the assignments that you will be asked to submit during the course.

* The `Exam` folder contains sample exams from previous years.


* The `Extra_Material` folder contains some extra reading about the Python theory, which you may use for future reference. It also contains some information specifically related to natural language processing, and examples on how to organize your code and how to create a Flask website.

* The `Data` folder contains all data used in this course and more, as well as the scripts used to obtain this data. (So you can see what techniques we used.)

This file serves as the syllabus and a general reference for this course.

## Assignments and Grading

The course is worth 6 ECTS and will consist of **4 assignments** and a **final exam**. The assignments have to be submitted after the content and tutorial session of each block (4 in total). In the third session of each block, we will discuss the assignment in class and provide feedback. The assignments and the exam are weighted as follows.

| Part    | weight % |  
|---------|----------|
|Assignment 1| 0*   |  
|Assignment 2|	 10  | 
|Assignment 3|	 20  |   
|Assignment 4|	 30  |    
| Exam | 40 |
|  **Total** |    100   |	

*Assignment 1 is not graded, but you are required to submit a serious attempt by the deadline to pass the course.


### Course assignments
You are asked to hand in 4 assignments in total. The deadlines are indicated below. Submission 1 day after the deadline and before the feedback session downgrades your grade by 2 (e.g., a 9 will result in a 7).  After that (i.e. on day 2 or after the feedback session has started), the resulting grade is a 1. We have to be strict about this because we will discuss the assignments in class, and we need time to look at your submissions. In addition, the solutions will be discussed in the feedback session, and we cannot award points after the solutions have been discussed.


Please note that a passing grade for each assignment (5.5) is required to pass the course. If you fail an assignment, you can submit a resit assignment to make up for it (please consider the limitations on resit opportunities outlined below). 


### Assignment submissions

Submission is made through Canvas. Please submit your assignments using the corresponding assignment submission on Canvas (e.g. labeled 'Assignment 1' for Assignment 1).

Please note that we cannot accept assignments submitted via email.

### Resits for Assignments

You can retake a maximum of two out of the four assignments. You have to retake assignments you missed and can retake assignments you failed. Please note that if you fail or miss more than two assignments, you automatically fail the course. 

Please note that the level of the resit assignments will be equivalent to the more advanced components of Assignment 4. The resit assignments will be published at the end of the course and there will be a deadline for submission. The deadline will be the same regardless of whether you have to submit one or two resit assingments. 


**It is highly recommended to submit all of your assignments at the regular deadlines. Please only make use of the resit opportunities in case you failed an assignment or were dealing with exceptional circumstances (e.g. illness). Please note that the deadline of the resit assignments will fall into period 2 and thus interfere with your new courses.**


### Final exam
The exam tests your knowledge of the syntax of Python, and your knowledge of the standard library. It serves as an opportunity to show what you've learned and will ensure that you have sufficient knowledge to tackle your own code projects and continue improving your python skills by yourself. You cannot pass the course without a passing grade on the exam. But don't worry: if you are able to finish the assignments, you will be fine on the exam. Please note that the format of the final exam is pen on paper (without the use of a computer or notes). 

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

The content of the exam only covers the content of the chapters treated in the course. Chapters 19, 20, and 21 will not be tested in the Assignments (nor on the exam). They serve as additional resources.

The schedule for the entire course follows the same structure, illustrated below.

All blocks except block IV will consist of three lectures. There is one additional lecture for block IV.

 ### Block structure

**Lecture 1**

In the first lecture, we explain and practice the basics of the new block. It is highly recommended to go through the chapter notebooks **in preparation** for the classes. Feel free to watch the additional video material provided on Canvas to understand the basic notions. After the first lecture, you are expected to start working on the assignment and consult the chapters for things that are unclear to you. 

Please be aware that the level of the assignments is a little bit higher than the level of the exercises provided at the end of each chapter. Solving the assignments requires taking some extra steps; you will have to combine notions from different chapters and most likely go through several cycles of trial and error. Therefore, please take into account that the assignments can most likely not be completed in a single day. Also, solving code problems is much easier if you have **sufficient time for breaks**.

**Lecture 2**

In the second lecture, we will further highlight some of the theory, and you will have time to practice more advanced notions. Support will be provided by the teachers and student assistants. It is highly recommended to prepare questions you have about the assignment and post them on Piazza (QA forum - access provided via our Canvas) before class. Ideally, we can prepare the lecture in such a way that it will help you finalize your assignment. You will finish the assignment between the second and third lecture and hand it in on either Wednesday or Friday.

**Lecture 3**

Finally, the third lecture is a feedback session where we will discuss some of the main problems that were encountered in the assignments. We will repeat this cycle 4 times (for each assignment).

### Course schedule


<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"><span style="font-weight:bold">Block</span></th>
    <th class="tg-21f3">What</th>
    <th class="tg-21f3">When</th>
    <th class="tg-21f3">Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-uzvj" rowspan="2">1</td>
    <td class="tg-kwiq">lecture</td>
    <td class="tg-kwiq">Tuesday 2024-09-03<br>13:30 - 15:15</td>
    <td class="tg-kwiq">Introduction theory</td>
  </tr>
  <tr>
    <td class="tg-kwiq">lecture</td>
    <td class="tg-kwiq">Thursday 2024-09-05<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Theory and work time</td>
  </tr>
  <tr>
    <td class="tg-uzvj" rowspan="4">2</td>
    <td class="tg-kwiq">lecture</td>
    <td class="tg-kwiq">Tuesday 2024-09-10<br>13:30 - 15:15</td>
    <td class="tg-kwiq">Introduction theory</td>
  </tr>
  <tr>
    <td class="tg-kwiq">lecture</td>
    <td class="tg-kwiq">Thursday 2024-09-12<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Theory and work time</td>
  </tr>
  <tr>
    <td class="tg-kwiq"><b>EXAM</b></td>
    <td class="tg-kwiq">Tuesday 2024-09-17<br>13:30 - 15:15</td>
    <td class="tg-kwiq">Midterm Exam (in class)</td>
  </tr>
  <tr>
    <td class="tg-kwiq">lecture</td>
    <td class="tg-kwiq">Thursday 2024-09-19<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Feedback Midterm/Assignments</td>
  </tr>
  <tr>
    <td class="tg-uzvj" rowspan="4">3</td>
    <td class="tg-kwiq">lecture</td>
    <td class="tg-kwiq">Tuesday 2024-09-24<br>13:30 - 15:15</td>
    <td class="tg-kwiq">Introduction theory</td>
  </tr>
  <tr>
    <td class="tg-kwiq">lecture</td>
    <td class="tg-kwiq">Thursday 2024-09-26<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Theory and work time</td>
  </tr>
  <tr>
    <td class="tg-kwiq">DEADLINE</td>
    <td class="tg-kwiq">Monday 2024-09-30<br>before 17:00</td>
    <td class="tg-kwiq">SUBMIT ASSIGNMENT 3</td>
  </tr>
  <tr>
    <td class="tg-kwiq">lecture</td>
    <td class="tg-kwiq">Tuesday 2024-10-01<br>13:30 - 15:15</td>
    <td class="tg-kwiq">Feedback assignment</td>
  </tr>
  <tr>
    <td class="tg-uzvj" rowspan="8">4</td>
    <td class="tg-kwiq">lecture</td>
    <td class="tg-kwiq">Thursday 2024-10-03<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Introduction theory</td>
  </tr>
  <tr>
    <td class="tg-kwiq">MA lecture</td>
    <td class="tg-kwiq">Tuesday 2024-10-08<br>13:30 - 15:15</td>
    <td class="tg-kwiq">Theory and work time</td>
  </tr>
  <tr>
    <td class="tg-kwiq">BA lecture</td>
    <td class="tg-kwiq">Tuesday 2024-10-08<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Theory and work time</td>
  </tr>
  <tr>
    <td class="tg-kwiq">MA lecture</td>
    <td class="tg-kwiq">Thursday 2024-10-10<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Theory and work time</td>
  </tr>
  <tr>
    <td class="tg-kwiq">BA lecture</td>
    <td class="tg-kwiq">Thursday 2024-10-10<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Theory and work time</td>
  </tr>
  <tr>
    <td class="tg-kwiq">DEADLINE</td>
    <td class="tg-kwiq">2024-10-14<br>before 17:00</td>
    <td class="tg-kwiq">SUBMIT ASSIGNMENT 4</td>
  </tr>
  <tr>
    <td class="tg-kwiq">Resit</td>
    <td class="tg-kwiq">Tuesday 2023-10-15<br>13:30 - 15:15</td>
    <td class="tg-kwiq">Resit for Midterm Exam</td>
  </tr>
  <tr>
    <td class="tg-kwiq">BA/MA lecture</td>
    <td class="tg-kwiq">Tuesday 2023-10-15<br>15:30 - 17:15</td>
    <td class="tg-kwiq">BA/MA Feedback assignment</td>
  </tr>
  <tr>
    <td class="tg-uzvj" rowspan="2">Exam Preparation</td>
    <td class="tg-kwiq">Lecture</td>
    <td class="tg-kwiq">Thursday 2023-10-17<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Exam preparation</td>
  </tr>
  <tr>
    <td class="tg-kwiq">EXAM</td>
    <td class="tg-kwiq">Tuesday 2023-10-22<br>8:30-11:15 (11:45, extra time)</td>
    <td class="tg-kwiq">EXAM (important: check location)</td>
  </tr>
</tbody>
</table>





## Plagiarism
Cheating is serious; it is considered fraud and can lead to being excluded from your studies (https://vu.nl/en/student/your-faculty/examination-board). It is also harmful; not only for yourself (you can fool yourself and fail to learn this useful skill), but also for other students (if multiple students do better because of cheating, teachers may think a grading scheme is fair, even though it needs to be adjusted).

How to avoid plagiarism, while making use of online sources and collaborating with fellow students:

For the weekly assignments, let us know in the comments if you have worked together with a class mate or if you used code from online sources, such as [stackoverflow](http://stackoverflow.com/). If you found some useful code online, do try to understand what that piece of code does. If it looks 'complicated', we expect you to provide in-line comments in the code explaining what it does.

If you use code you found online in an assignment, please indicate it in the following way:

```
### Taken from [link] [date]

[code]

\###
```

Please use a similar format to indicate that you have worked with a classmate (e.g. mention the name instead of the link). Make sure to provide your own comments to show that you understood and indicate what you did yourself, e.g. by commenting your partial solution out (we cannot give credits for copy-pasting full answers from classmates, but you may get full points for a partial individual solution and well commented working one with components from a classmate). If you work on a solution together, also indicate this and make sure to provide individual explanations.
