# Factorial



In mathematics, the factorial of a non-negative integer `n`, 
denoted by `n!`, is the product of all positive integers less 
than or equal to `n`. For example:

```
5! = 5 * 4 * 3 * 2 * 1 = 120
```

| n     | n!                          | 
| ----- | --------------------------: |
| 0     | 1                           |
| 1     | 1                           |
| 2     | 2                           |
| 3     | 6                           |
| 4     | 24                          |
| 5     | 120                         |
| 6     | 720                         |
| 7     | 5 040                       |
| 8     | 40 320                      |
| 9     | 362 880                     |
| 10    | 3 628 800                   |
| 11    | 39 916 800                  |
| 12    | 479 001 600                 |
| 13    | 6 227 020 800               |
| 14    | 87 178 291 200              |
| 15    | 1 307 674 368 000           |

## References

[Wikipedia](https://en.wikipedia.org/wiki/Factorial)

# Fibonacci Numbers


The fibonnaci sequence takes the sum of the two previous positive integers to generate the next one. It has two base cases: 0, and 1 (neither of which have 2 previous positive integers). Every other integer has a fibbonaci value, as demonstrated in the following table:


| n     | Nth Fibonacci Number        | 
| ----- | --------------------------: |
| 0     | 0                           |
| 1     | 1                           |
| 2     | 1                           |
| 3     | 2                           |
| 4     | 3                           |
| 5     | 5                           |
| 6     | 8                           |
| 7     | 13                          |
| 8     | 21                          |
| 9     | 34                          |
| 10    | 55                          |

## References

[Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number)
=======
# Bubble Sort

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

Example:
First Pass:
( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

Second Pass:
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.

Third Pass:
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )

## References

[Geek For Geeks](https://www.geeksforgeeks.org/bubble-sort/)

# Stack

Stack in first in last out algorithms (FILO) that any thing get in first then it will get to out side last when we want to add data to stack we need to append and when we want to get data we need to pop data from stack

[includehelp](https://www.includehelp.com/data-structure-tutorial/stack-using-c-and-cpp-data-structure-tutorial.aspx)

