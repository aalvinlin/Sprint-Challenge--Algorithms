#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The while condition is written to stop when n is n^3, but a is being increased by a sum of n^2 every loop. In order to determine the ratio of how much faster n is increasing, 

b)

This section of code has a "for" loop going through n elements, and inside this loop there is a "while" loop that goes through half as many elements. The inner "while" loop doubles j every time, so j will approach n much more quickly than j will increase. The inner "while" loop therefore has a O(log n) runtime, and the outer loop must do this n times. As a result, the total runtime is O(n log n).


c)

This recursive function has a constant time base case and a recursive case that invokes a single recursive call. The recursive call is added to a constant term. Since addition of a constant is O(1) time, the runtime of the recursive call dominates the overall runtime of the function. The number of recursive calls increases in direct proportion to the size of n, so the runtime for the total number of recursive calls, and hence the overall runtime, will be O(n).

## Exercise II

Another way to rephrase the problem is to guess the value of an unknown number from 0 to n. After each guess, information will be provided whether the unknown number is actually higher or lower than the guess. If the egg breaks, then the guess was too high. If the egg doesn't break, the guess was too low.

To minimize the number of broken eggs, a binary search with a runtime of O(log n) should be used. By repeatedly guessing the midpoint of the current working range, half of the possibilities will be eliminated on each turn. If the egg breaks, choose the lower half; if the egg doesn't break, choose the upper half. The solution is found when the current working range is so small that it can be seen that an egg doesn't break on floor f but breaks on floor (f - 1).