# Publication Requirements
By **Antske Fokkens**, originally appeared on [the CLTL website](www.cltl.nl).


At CLTL, we strive for sharing resources and software and making sure our research results are replicable. We therefore have the following guidelines. Principles 1. and 2. are required for any publication by a member of the CLTL group.
Principles

1. All publications are indicated on the CLTL website with a link to the actual publication (if permitted).
2. All published experiments must be replicable. For any experiment, the following should be stored and made accessible where possible:
    * Your original research question and hypothesis
    * Data
    * Resources
    * Software
    * Results
    * Readme with necessary instructions
3. Ideally, the historic development of the experiment is also provided.
    * Your research question and hypotheses may change during the course of your research. You should always be open about your original hypothesis, if your questions and hypotheses change, explain why.

# Recommended Workflow

1. Define your research question and hypothesis (or hypotheses). (**obligatory**)
2. Before you start working on an experiment, create a directory in your favorite version control system that you can use to run your experiment. (recommended)
3. Setup the experiment in this directory, so that it contains all code, scripts and data created especially for the experiment and points clearly to all other code and resources you use. (recommended)
4. Add a file called *notes.txt* where you briefly describe the steps you take, reasons for adapting code or rerunning the experiment. (recommended)
5. Check in your setup and results after each run. (recommended)
6. When you are done and have the results you’ll describe in a paper, publish the experiment carefully checking the points listed below. (**obligatory**)

## Publishing experiments

For any published experiment, all materials required to repeat the experiment must be archived and, whenever possible, made accessible.

Software, resources and datasets can be stored at the CLTL github and CLTL SciStor.

The following components are typically required to ensure replicability of an experiment. To be on the safe side, ask a colleague to carry out the experiment from scratch to verify if you have provided all components and described all steps clearly.

1. Results
    * Don’t just provide the numbers, but **provide the actual output of your system** on the evaluation data. This allows other researchers to better compare their results to yours and identify errors if they fail to replicate your experiment.
2. Data, software and other resources
    * Include both training and evaluation data.
    * Make sure you report the **exact version** of data, software and resources you use. Preferably using the version identifier from a version control system.
    * If you cannot point to a version from a version control system, you may want to include a copy of the resource or data while publishing the experiment (if permitted). Some researchers make minor corrections to software and resources without upgrading to a new version.
    * If you cannot make the resource you used available, make sure you **document any changes you have made**. Preferably provide a script so that researchers who have the data can create your version from the original.
    * **Provide documentation**. At the very least, this should contain explanations of how to use your software or explain the structure of your data or resource.
    * No matter how certain you are that all people who’ll ever look at your documentation or code know your preferred language, make sure all comments, notes and documentation are in English.
3. Experimental setup
    * Make sure you document the **exact settings** you used for running your experiment. If you use a script to call your programs with specific options, provide it. Also include any configuration files that you used for your experiment.

## Accessibility

Unless project partners require otherwise, all software, data and resources developed at CLTL should be publicly available.
We generally release software and resources under the Apache license.

If you use data, software or resources you cannot make available:

* Make sure you clearly indicate what you used (including the version) and how one may gain access to it (e.g. where to get the license).
* If you made any changes, make sure that anyone who has the original data/software/resource can recreate the version you used either by running a script you provide or by following a detailed description.

## Historic development

Our 8-page limited papers are typically too short to provide all experimental details. The steps that were taken to get to a final (reported) experiment can provide useful insights to other researchers and help prevent errors in your own experiment.

A full report of the historic development starts with the hypothesis that inspired the research, including a brief explanation of where you based your hypothesis on. It reports each step that was taken, including errors.

Ideally, there would be:

1. A brief overview of how you got to your original research question and hypothesis (if applicable). You want to keep a record of your steps as soon as you start looking at, or playing with, data.
2. A version control system recording the experiment, starting with the earliest version including all intermediate results and trials.
3. A technical report including a description of decisions and their motivations, errors and their solutions and additional intermediate results.

If you setup a version control system for your experiment when you begin working, it will be less work to publish the experiment once your done (and you’re probably dealing with deadline stress…).
