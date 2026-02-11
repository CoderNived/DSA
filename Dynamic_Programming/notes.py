# def climbStairs(n):
#     if n==1:
#         return 1
#     if n==2:
#         return 2
#     return climbStairs(n-1)+climbStairs(n-2)
# climbStairs(5)
# print(climbStairs(6))
# This is a recursive solution to the problem of climbing stairs. The function `climbStairs` takes an integer `n` as input, which represents the number of stairs. The function returns the number of distinct ways to climb to the top of the stairs.
# The base cases are defined for `n=1` and `n=2`, where there is only one way to climb one stair and two ways to climb two stairs (either taking one step twice or taking two steps at once). For `n` greater than 2, the function calls itself recursively to calculate the number of ways to climb the stairs by summing the results of climbing `n-1` and `n-2` stairs. This is because to reach the nth stair, you can either take a single step from the (n-1)th stair or take a double step from the (n-2)th stair.
# The output of `climbStairs(5)` will be 8, and the output of `climbStairs(6)` will be 13, which are the number of distinct ways to climb 5 and 6 stairs, respectively. 

#Memoization

memo={}
def climbStairs(n):
    if n in memo:
        return memo[n]
    if n==1:
        return 1
    if n==2:
        return 2
    result = climbStairs(n-1)+climbStairs(n-2)
    memo[n]=result
    return result

print(climbStairs(6))

# Memoization is a technique used to optimize recursive functions by storing the results of expensive function calls and returning the cached result when the same inputs occur again. In this implementation, we use a dictionary called `memo` to store the results of previously computed values of `climbStairs(n)`. When the function is called, it first checks if the result for `n` is already in the `memo` dictionary. If it is, it returns that value immediately, avoiding redundant calculations. If not, it computes the result recursively and stores it in the `memo` dictionary before returning it. This optimization significantly reduces the time complexity from exponential to linear, making it much more efficient for larger values of `n`.
# Memoization is particularly effective in this problem because the number of ways to climb stairs grows exponentially without it, but with memoization, we can compute the result in linear time.
# Memoization is a powerful technique that can be applied to many recursive problems, especially those that involve overlapping subproblems, such as the Fibonacci sequence, dynamic programming problems, and more. By caching results, we can avoid redundant calculations and improve the performance of our algorithms significantly.
# Memoization is basically recusrssion with memory. It is a top-down approach to solving problems, where we start with the original problem and break it down into smaller subproblems, storing the results of those subproblems to avoid redundant calculations. This is in contrast to a bottom-up approach, where we would start with the smallest subproblems and build up to the original problem iteratively. Both approaches can be effective, but memoization can often be more intuitive and easier to implement for certain types of problems.
# In summary, memoization is a powerful technique that can significantly improve the performance of recursive functions by caching results and avoiding redundant calculations. It is particularly effective in problems with overlapping subproblems, such as the climbing stairs problem, and can be applied to a wide range of recursive algorithms to optimize their performance.

