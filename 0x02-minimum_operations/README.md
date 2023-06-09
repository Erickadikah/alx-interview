# Minimum Operations

This code  i used prime factorization to compute the minimum number of operations. For example, to get n=12 H's, we can compute its prime factorization n=2*2*3 and see that we can first copy all (1 operation) and then paste 2 times (2 operations) to get 4 H's. Then, we copy the 4 H's (1 operation) and paste 3 times (3 operations) to get 12 H's. Thus, the total number of operations is 1+2+1+3=7. Similarly, for n=4 H's, we can compute its prime factorization n=2*2 and see that we can copy all and paste once to get 2 H's (2 operations), and then copy the 2 H's and paste once more to get 4 H's (2 operations). Thus, the total number of operations is 2+2=4.

## Tasks

### 0. Minimum Operations

Write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

- Prototype: `def minOperations(n)`
- Returns an integer
- If n is impossible to achieve, return 0

## Author

ERICK ADIKAH