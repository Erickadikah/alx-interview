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

In this example im using a greedy algorithm to solve the problem. The algorithm is as follows:

1. Sort the coins in descending order
2. Iterate through the coins
3. If the current coin is less than the total, add the quotient of the total divided by the current coin to the number of coins
4. Set the total to the remainder of the total divided by the current coin
5. If the total is 0, return the number of coins
6. If the total is not 0, return -1

## File Descriptions

- `0-making_change.py`: contains the function `makeChange`
