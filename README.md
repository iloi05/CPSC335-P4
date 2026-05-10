# CPSC335-P4
---
## Algorithm 1: The Stock Purchase Maximization Problem

### Exhaustive Approach
This algorithm solves the stock selection problem by evaluating every single possible combination of stocks to find the one that maximizes the total value without exceeding the available budget. Our exhaustive approach treats the problem similarly to a 0/1 Knapsack problem where each stock entry is either included or not included. Using the itertools.combinations library, our exhaustive approach iterates over all the subsets of stocks and calculates the total cost and value for each combination. If a combination fits the budget and exceeds our current best, we make it the new best candidate. This approach does guarantee an optimal solution, but has higher computational cost with a time complexity of O(2^n), making it impractical for large inputs.

### Dynamic Approach
Solving the same stock selection problem, we instead build a 2D table where each dpTable[i][j] stores the best achievable value considering only the first i stocks with a budget of j. For each stock, the algorithm checks whether to keep it by adding its value to the best result achievable or throw it away by continuing with the previous best. By storing and reusing these results, we can avoid redundant recalculation with the optimal stock selection and its total value being stored directly in the last cell of the 2D table. With a time complexity of O(n x W) where n is the number of stocks and W is the budget, this approach is significantly faster for large inputs compared to the exhaustive approach. 

---
## Algorithm 2: Duplicate Detection Using Hashing
