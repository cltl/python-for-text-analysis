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

## Useful techniques

* Using Argparse.
* Logging your runs.
* Seeding the randomization function.
* Testing your code.
* Documenting as you write.
