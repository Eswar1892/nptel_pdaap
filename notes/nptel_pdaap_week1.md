## Week 1, Lecture 1 - Algorithms and programming: simple GCD

### What is an algorithm?

- It is a description of system steps to perform a task
- Programming languages describes the steps
  - What is a step? What is the level of detail?
- Focus of course: computer algorithms that typical manipulate information. (Anything that looks at information and manipulates information)
  - Compute numerical functions
  - Reorganize data - ascending or descending
  - Optimization - find the shortest route
  - And more ...

### GCD: Greatest common divisor

- Note: a divisior is a number that divides another number with a remainder 0.
  - Example: 4 is a divisor of 16. 9 is a divisor of 63 etc.,
- gcd(m,n):

  - Largest k such that k divides m and k divides n.
  - Example: gcd(8,12) = 4. gcd(18,25) = 1
  - Since 1 divides any number, then will definitely a gcd for 2 sets od numbers.

- How to compute thr gcd of m,n?
  - Naive way:
    - List out all the factors of m
    - List out all the factors of n
    - Among these, find a common factor that is highest between the two lists.
- Is it a valid algorithm?

  - Finite representation of the recipe
  - Terminates after a finite number of steps:
    - The process of listing the steps/ computation make take a long time, however, we need to be guaranteed that we get the answer after a finite number of steps

- Some points to note:
    - Use names to remember intermediate values
    - Values can be single items or collections (a.k.a Data structure)

## Week 2, Lecture 2 - Improving naive gcd

### Can we make our naive algorithm better?
- Instead of scanning the factors for m,n separately, we can do it on one scan in `for i in range(1, max(m,n)+1)` and factors to respective lists
- Even Better: only if i divided both m & n then take i into a list (instead of storing factors and then taking out the common factors)
- Even better: Since factor of any number x, lie between 1 & x (inclusive) and doesn't go beyond X. So instead of scanning for factors till max(m,n), we should infact scan it till min(m,n)



