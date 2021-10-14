![FCB-Python-autograding](../../actions/workflows/fcb_autograding.yml/badge.svg)

# Assignment 3 - FCB 2020
### Deadline: 22/10/2021 - 23:59

## Submission procedure

This assignment has to be submitted using GitHub Classroom. This
means that you should have cloned the GitHub repo of this assignment from
the organization account for FCB in the academic year 2021-22 at
[https://github.com/funcompbio2021](https://github.com/funcompbio2021)
using the submission link provided at the FCB Moodle site.

Once you have cloned the GitHub repo which has `assignment-3` and your
GitHub username as repo name, then you can work on it in your local disk
and _push_ your changes whenever you like, but make sure that you have pushed
the last version of your assignment before the deadline. There is no
_submit_ button or any other specific submission procedure or action than
just pushing your changes to you GitHub assignment repo. When correcting the
assignment, the version available at the deadline will be retrieved. If the
first version available is posterior to the deadline, then the mark of the
assignment will have a penalty.

## Description

The goal of this assignment is to implement a program in Python that
**asks for two positive integer numbers and decides whether they are
friends or not, saying 'friends' when they are, and 'no friends' when
they are not.**

According to the Wikipedia [page](https://en.wikipedia.org/wiki/Friendly_number)
two positive integer numbers are friends if they have the same ratio
between the sum of their
[divisors](https://en.wikipedia.org/wiki/Divisor) and the number itself.
For instance, the divisors of 6 are 1, 2, 3 and 6, and therefore they
add up to 12, while the divisors of 28 are 1, 2, 4, 7, 14 and 28, and
therefore they add up to 56. Because 12/6=2 and 56/28=2, 12 and 56 one
says that they are _friends_. If we consider the number 12, its divisors
are 1, 2, 3, 4, 6 and 12, which add up to 28, and therefore because
28/12=14/6=7/3 is different to 2, 12 cannot be _friends_ with 6 nor 28.

This assignment incorporates an autograding feature using a so-called
[GitHub Actions Worflow](https://github.com/features/actions), which will
help you to automatically test whether your Python program is
correctly working after every _push_. To work with this feature you
need to edit your program in the existing file `src/friends.py` and
leave the rest of the files and directory structure intact. Within the
file `src/friends.py` please follow the instructions written in comments
and put your code exactly in the indicated lines. You can test your
program on your own computer by changing your current working directory
into the `src` directory of this GitHub repo and typing:

```
$ python friends.py
```

Your assignment repo should have the following two files:

  1. This `README.md` file.
  2. The `src` directory with the initial files of the assignment repo.
  3. The `test` directory with the initial files of the assignment repo.

Eventually, you may encounter that Python automatically creates a directory called
`__pycache__`, you may ignore that directory since this template is already
prepared to ignore that directory by including it into a `.gitignore` file that
informs Git to avoid putting certain files under version control. In any case,
**you should only be editing the file `src/friends.py`**.

## Evaluation rubric

The rubric to evaluate this assignment consists of the following items:

  * Does the assignment contain the required files?
  * Does the Python program `src/friends.py` runs without errors?
  * Does the Python program `src/friends.py` identifies friends and no friends numbers correctly?
  * Does the Python program `src/friends.py` passes all autograding tests?
