# Making Change

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

* Prototype: `def makeChange(coins, total)`
* Return: fewest number of coins needed to meet `total`
    * If `total` is `0` or less, return `0`
    * If `total` cannot be met by any number of coins you have, return `-1`
* `coins` is a list of the values of the coins in your possession
* The value of a coin will always be an integer greater than `0`

## My Implementation

* Compiled using: `python3`

* Language: Python 3.4.3

In this example im using Memoization to solve the problem. The idea is to create a table of size `total + 1` and initialize all values in table as `0`. One by one we pick coins one by one and update the table[] values after the index greater than or equal to the value of the picked coin. The base case of recursion will be when `total` is equal to `0`. For example, for `total` 4 and coins `{1,2,3}`, there are 4 solutions: `{1,1,1,1},{1,1,2},{2,2},{1,3}`. So output should be `4`. For `total` 10 and coins `{2,5,3,6}`, there are 5 solutions: `{2,2,2,2,2},{2,2,3,3},{2,2,6},{2,3,5}` and `{5,5}`. So the output should be `5`.
