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

---

## Week 1, Lecture 2 - Improving naive gcd

### Can we make our naive algorithm better?

- Instead of scanning the factors for m,n separately, we can do it on one scan in `for i in range(1, max(m,n)+1)` and factors to respective lists
- Even Better: only if i divided both m & n then take i into a list (instead of storing factors and then taking out the common factors)
- Even better: Since factor of any number x, lie between 1 & x (inclusive) and doesn't go beyond X. So instead of scanning for factors till max(m,n), we should infact scan it till min(m,n)

- Even better: We don't need any lists as only need the largest divisor. we can assign i to a variable and return it. As we are traversing from smallest to largest it will automatically return whatever is the largest.

- Even better: Scan Backwards! Since we are looking for the largest divisor, we can traverse from largest to the smallest. assign i to a new variable, break once the if condition satisfies.
- Even though these algorithms are efficient. Then still take time propotional to m and n. The time complexitiy is `o(n)`
- `while loops`: A while loop run `while` a condition is true.
- `while loop` is useful if we don't know in advance how many times we need repeat the loop.
  - We should know in advance that the condition becomes False and the loop terminates

#### Exercise:

- Find the gcd of n different given numbers. Here n is variable.
- What is the time complexity of the above gcd?
  - It is `O(n)` since in the worst case I need to scan all way from min(m,n) to 1.

### Week 1, Lecture 3 - Euclid's algorithm for gcd

- Euclids Algorithm for computing gcd is as follows:
- If d is the GCD of m,n => it divides m, and it also divides n. Let say m > n, then d should also divide m-n. so finding gcd of m,n is equivalent to finding gcd(n, m-n) since that the greatest divisor of n, it should be greatest divisor both n,m-n can possibly have. [Note: we can also say that it is same as gcd(m,m-n) but we preder gcd(n,m-n) since n is smaller implying lesser computation time]
- Now to compute the gcd euclids way, you can follow the below steps:

  - check if m>n, else swap m&n
  - Check if n divides m, if it divides then n is greatest divisor that m,n can possibly have
  - If not, compute gcd(n, m-n).

- What is the time complexity of the euclid's algorithm?
- (14,11) -> (11,3) -> (8,3) -> (5,3) -> (3,2) -> (2,1): 5 steps
- (14,11) -> scan 11,....5,4,3,2,1 - 11 steps
- **Note**: In the recursive step if we use gcd(m,m-n) we might run into infinite recursion

- Note: Whenever we call a function inside another function, the calling function waits until there is a return value from the called function. The called function passes back a value to the calling function.. Hence, there needs to be a return statement in such kinds of functions.

