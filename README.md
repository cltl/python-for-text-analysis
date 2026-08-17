# Python for text analysis

*As taught at the Vrije Universiteit Amsterdam in the [Humanities Research Master: Linguistics](https://vu.nl/en/education/master/humanities-research-linguistics) (track [Human Language Technology](https://home.cltl.labs.vu.nl/education-ma-hlt)), the [Linguistics Master: Language and AI](https://vu.nl/en/education/master/linguistics-language-and-ai) and the [Minor Digital Humanities and Social Analytics (BA)](https://vu.nl/en/education/minor/digital-humanities-and-social-data-analytics).*

In case you have questions about exemption, please first read [Python-test.md](https://github.com/cltl/python-for-text-analysis/blob/master/Assignments/Python-test.md).

This is a practical course in Python, geared towards those who want to get some hands-on experience working with language data.
No knowledge of programming is required or presupposed.
We will work with Python 3.12 or higher. We highly recommend installing [Anaconda](https://www.anaconda.com/download) for this course.

(If you have worked with Python 3 before, be sure to check if Jupyter Notebook is installed on your machine. We will work extensively with notebooks. Make sure you are working with Python 3.12.)

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
* If none of these steps helped, please try to ask for help in a timely manner (i.e., within the respective block). You can approach the lecturers in class for small questions or come to office hours if you feel you need to review a concept. In person discussions are always preferred! If you end up emailing the lecturer, please include your code rather than a screenshot.

Learning how to help yourself is a valuable skill and will be very useful in your future programming projects!

## Notes on the use of Generative AI:

Everyone knows how easy it has become to ask Generative AI models to do tasks for us. We want to ask you: **RESIST THIS URGE!** 

While trying to avoid broader discussions, we are open to the arguments that Generative AI has role to play in modern societies. We do believe, however, that their role in education is not yet well understood and that, when used incorrectly, it can seriously hinder the learning process. Please remember that passively accepting a solution provided by these models is very different than coming up with solutions yourself. During exams, you will need to come up with solutions yourself (i.e., without the help of generative models). Resisting the urge to use generative AI during your learning journey will pay off! Trust the system! Finding ways to solve a problem when you get stuck is one of the most important skills a programmer can have, and one of this course's learning learning goals. We highly discourage the use of Generative AI during this course. 

That being said, we believe Generative AI can be a useful tool for experienced programmers. Towards the end of the course, we will come back to discuss how to best use Generative AI in your future programming careers.   


## Courseware structure

Our materials are structured as follows:

* The `Chapters` folder contains our primary teaching material. Every week, you will work through a subset of these interactive notebooks. We expect you to look at the material in preparation for the lectures. If you get stuck with an assignment, first see if you can find the solution in the Chapters.

* The `Assignments` folder contains the assignments that you will be asked to complete during the course. These assignments will be self/auto-graded. Each assignment will have a specific feedback session to go over student-led questions about the assignments. 

* The `Extra_Material` folder contains some extra reading about the Python theory, which you may use for future reference. It also contains some information specifically related to natural language processing, and examples on how to organize your code and how to create a Flask website.

* The `Data` folder contains all data used in this course and more, as well as the scripts used to obtain this data. (So you can see what techniques we used.)

This file serves as the syllabus and a general reference for this course.

## Assignments and Grading

The course is worth 6 ECTS and will consist of **4 self/auto-graded assignments**, **1 midterm exam** and **1 final exam**. 
Each assignment is tied to one block (see below). It is very important that you do the assignments within their respective block. 
Each block as session dedicated to going over the assignment and to discuss issues students encountered during the assignment. 
You will only get something out of these sessions if you come prepared (i.e., having done the assignment). **Full solutions for the assignments will not be provided!**

The assignments and the exams are weighted as follows:

| Part           | weight %             |  
|----------------|----------------------|
| Assignment 1   | self/auto-graded     |  
| Assignment 2   | self/auto-graded     | 
| Midterm Exam   | 30 %                 |
| Assignment 3   | self/auto-graded     |   
| Assignment 4   | self-graded          |    
| Exam           | 70 %                 |
| **Total**      | 100 %                |	


Even though the assignments do not need to be submitted, and do not weight directly in your final grade, the final exam will contain a 
number of exercises extracted directly or adapted from the assignments. The 70% of the final exam can be decomposed in the following way: 
40% (new questions) + 30% (assignment-based questions).

As such, keeping up with assignments and making use of the auto-grading system (when available) is a great way to ensure you do well in this course!

### Midterm exam (and Resit)
The midterm exam will assess the basics of Python syntax and over the content covered in Block 1 and Block 2. As 
preparation for this exam, please work through the material of the blocks and complete Assignment 1 and 2. Passing 
the midterm exam ensures that you are ready for the more advanced component of the course. It will be a TestVision 
(computer) exam with no external tools allowed. You will need a minimum grade of 5.5 (out of 10) to pass the midterm. 
If you fail the midterm you will be allowed a resit during the course.  See the schedule for details. 

### Final exam (and Resit)
The exam tests your knowledge of the syntax of Python, and your knowledge of the standard library. It serves as an 
opportunity to show what you've learned and will ensure that you have sufficient knowledge to tackle your own code 
projects and continue improving your python skills by yourself. You cannot pass the course without a passing grade 
on the exam. But don't worry: if you are able to finish the assignments, you will be fine on the exam. Please note 
that the format of the final exam is computer-based, but you will **not have access to a python interface or the 
internet** (just like in the midterm exam). You will need a minimum grade of 5.5 (out of 10) to pass the final exam. 
The resit for the exam follows the official schedule. Please see https://rooster.vu.nl/ for details.

**Note:** It is highly recommended to aim for a passing grade at the regular exam dates. Please only make use of a 
resit exam if you fail a regular exam or were dealing with exceptional circumstances (e.g. exam date conflict, illness).


## Schedule

The course is built around four blocks. Each block is tied to one assignment. Even though assignments
not count directly towards your final grade, it is highly recommend that you complete them in preparation for each respective block. 
This will allow you to maximise your learning experience as each block as reserved lectures 
to discuss the assignments in class and provide feedback.  This is not the type of course one can easily cram before the exam. 
If you feel you are falling behind, please approach the lecturers as soon as possible. 
They can help you make a plan to get back on track.


### Planning
There are 4 Blocks with associated chapters and assignments:

| Block   | Chapters BA | Chapters MA | Assignment BA | Assignment MA |
|---------|---------|---------|-----|----|
| I | Chapters 1-4 | Chapters 1-4 |	 Assignment 1 | Assignment 1 |
| II |Chapters 5-11  |  Chapters 5-11 |Assignment 2 | Assignment 2 |
| III |Chapters 12-15 | Chapters 12-15 |	Assignments 3a and 3b (Exercises 3 and 4 of Assignment 3b are excluded for BA students)	| Assignments 3a and 3b	|
| IV |Chapters 16, 17, 22 | Chapters 16-18 | Assignments 4a and 4b-BA | Assignments 4a and 4b-MA |

The content of the exam only covers the content of the chapters treated in the course. Chapters 19, 20, and 21 will not be tested in the Assignments (nor on the exam). They serve as additional resources.

The schedule for the entire course follows the same structure, illustrated below.

 ### Block structure

**First Lecture**

In the first lecture of each block, we explain and practice the basics of the block. It is highly recommended to go 
through the chapter notebooks **in preparation** for the classes. Feel free to watch the additional video material 
provided on Canvas to understand the basic notions. After the first lecture, you are expected to start working on the 
assignment and consult the chapters for things that are unclear to you. 

Please be aware that the level of the assignments is a little bit higher than the level of the exercises provided at 
the end of each chapter. Solving the assignments requires taking some extra steps; you will have to combine notions 
from different chapters and most likely go through several cycles of trial and error. Therefore, please take into 
account that the assignments can most likely not be completed in a single day. Also, solving code problems is much 
easier if you have **sufficient time for breaks**.

**Middle Lectures**

In the middle lectures of each block (either one or two), we will further highlight some of the theory, and you will 
have time to practice more advanced notions with the support of the lecturers. Ideally, we can prepare the lecture in 
such a way that it will help you finalize the block's assignment. You should aim to finish the assignment between 
during the middle lectures (so you can use the lecture to ask for questions).

**Last Lecture**

Finally, the last lecture of each block is a feedback session where we will discuss some of the main problems that 
were encountered in the assignments. We will repeat this cycle multiple times (for each assignment). Please note that 
we will use a single feedback lecture for Blocks 1 and 2 (see course schedule below). 

**Office Hours**

Office hours are held most Thursdays, from 17:30. This session is indented to help students solve problems or to 
answer questions. The lecturers will also try to answer any emails sent to the course email this session. 
It is preferred that you ask questions in class or come to this session instead of using the email.  

**This session is scheduled on rooster but attendance is completely optional.** 
If no students are present during the session, the session will end early. If you want to use this session make sure you 
let the lecturer know during the Thursday lecture (or by email, if you can't make it to the lecture for some reason).


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
    <td class="tg-kwiq">Tuesday 2025-09-01<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Introduction theory</td>
  </tr>
  <tr>
    <td class="tg-kwiq">lecture</td>
    <td class="tg-kwiq">Thursday 2025-09-03<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Theory and work time</td>
  </tr>
  <tr>
    <td class="tg-uzvj" rowspan="4">2</td>
    <td class="tg-kwiq">lecture</td>
    <td class="tg-kwiq">Tuesday 2025-09-08<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Introduction theory</td>
  </tr>
  <tr>
    <td class="tg-kwiq">lecture</td>
    <td class="tg-kwiq">Thursday 2025-09-10<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Theory and work time</td>
  </tr>
  <tr>
    <td class="tg-kwiq"><b>MIDTERM</b></td>
    <td class="tg-kwiq"><b>Monday 2025-09-14<br>18:45 - 21:00</b></td>
    <td class="tg-kwiq"><b>(check rooster for location)</b></td>
  </tr>
  <tr>
    <td class="tg-kwiq">lecture</td>
    <td class="tg-kwiq">Tuesday 2025-09-15<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Feedback Midterm/Assignments</td>
  </tr>
  <tr>
    <td class="tg-uzvj" rowspan="3">3</td>
    <td class="tg-kwiq">lecture</td>
    <td class="tg-kwiq">Thursday 2025-09-17<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Introduction theory</td>
  </tr>
  <tr>
    <td class="tg-kwiq">lecture</td>
    <td class="tg-kwiq">Tuesday 2025-09-22<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Theory and work time</td>
  </tr>
  <tr>
    <td class="tg-kwiq">lecture</td>
    <td class="tg-kwiq">Thursday 2025-09-24<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Feedback assignment</td>
  </tr>
  <tr>
    <td class="tg-uzvj" rowspan="6">4</td>
    <td class="tg-kwiq">lecture</td>
    <td class="tg-kwiq">Tuesday 2025-09-29<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Introduction theory</td>
  </tr>
  <tr>
    <td class="tg-kwiq">lecture</td>
    <td class="tg-kwiq">Thursday 2025-10-01<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Introduction theory</td>
  </tr>
  <tr>
    <td class="tg-kwiq">MA lecture</td>
    <td class="tg-kwiq">Thursday 2025-10-06<br>13:30 - 15:15</td>
    <td class="tg-kwiq">Theory and work time</td>
  </tr>
  <tr>
    <td class="tg-kwiq">BA lecture</td>
    <td class="tg-kwiq">Thursday 2025-10-06<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Theory and work time</td>
  </tr>
  <tr>
    <td class="tg-kwiq">BA lecture</td>
    <td class="tg-kwiq">Thursday 2025-10-08<br>13:30 - 15:15</td>
    <td class="tg-kwiq">Theory and work time</td>
  </tr>
  <tr>
    <td class="tg-kwiq">MA lecture</td>
    <td class="tg-kwiq">Thursday 2025-10-08<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Theory and work time</td>
  </tr>
  <tr>
    <td class="tg-uzvj" rowspan="4">Exam Preparation</td>
    <td class="tg-kwiq">MA lecture</td>
    <td class="tg-kwiq">Thursday 2025-10-13<br>13:30 - 15:15</td>
    <td class="tg-kwiq">Feedback assignment/Exam preparation</td>
  </tr>
  <tr>
    <td class="tg-kwiq">BA lecture</td>
    <td class="tg-kwiq">Thursday 2025-10-13<br>15:30 - 17:15</td>
    <td class="tg-kwiq">Feedback assignment/Exam preparation</td>
  </tr>
 <tr>
    <td class="tg-kwiq"><b>RESIT</b></td>
    <td class="tg-kwiq"><b>Tuesday 2025-10-15<br>15:30 - 17:15</b></td>
    <td class="tg-kwiq"><b>Resit for Midterm Exam</b> (no class)</td>
  </tr>
  <tr>
    <td class="tg-kwiq"><b>EXAM</b></td>
    <td class="tg-kwiq"><b>Tuesday 2024-10-20<br>8:30-11:15 (11:45, extra time)</b></td>
    <td class="tg-kwiq"><b>(check rooster for location)</b></td>
  </tr>
</tbody>
</table>





## Plagiarism
Cheating is serious; it is considered fraud and can lead to being excluded from your studies (https://vu.nl/en/student/your-faculty/examination-board). It is also harmful; not only for yourself (you can fool yourself and fail to learn this useful skill), but also for other students (if multiple students do better because of cheating, teachers may think a grading scheme is fair, even though it needs to be adjusted).

How to avoid plagiarism, while making use of online sources and collaborating with fellow students:

For the assignments, let us know in the comments if you have worked together with a class mate or if you used code from online sources, such as [stackoverflow](http://stackoverflow.com/). If you found some useful code online, do try to understand what that piece of code does. If it looks 'complicated', we expect you to provide in-line comments in the code explaining what it does.

We highly discourage relying on ChatGPT (or similar tools) in this course. While code support can be useful later on, we know that it has a negative impact on the learning process early on. Students who rely too much on such tools fail to progress to more advanced coding assignments. If you use code generated by a model, please provide:

* your prompt (what you provided as input)
* the code generated by the model
* your comments explaining what the code does and how you adapted it

If you use code you found online in an assignment, please indicate it in the following way:

```
### Taken from [link] [date]

[code]

\###
```

Please use a similar format to indicate that you have worked with a classmate (e.g. mention the name instead of the link). Make sure to provide your own comments to show that you understood and indicate what you did yourself, e.g. by commenting your partial solution out (we cannot give credits for copy-pasting full answers from classmates, but you may get full points for a partial individual solution and well commented working one with components from a classmate). If you work on a solution together, also indicate this and make sure to provide individual explanations.
