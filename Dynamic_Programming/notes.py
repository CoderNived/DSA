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

# memo={}
# def climbStairs(n):
#     if n in memo:
#         return memo[n]
#     if n==1:
#         return 1
#     if n==2:
#         return 2
#     result = climbStairs(n-1)+climbStairs(n-2)
#     memo[n]=result
#     return result

# print(climbStairs(6))

# Memoization is a technique used to optimize recursive functions by storing the results of expensive function calls and returning the cached result when the same inputs occur again. In this implementation, we use a dictionary called `memo` to store the results of previously computed values of `climbStairs(n)`. When the function is called, it first checks if the result for `n` is already in the `memo` dictionary. If it is, it returns that value immediately, avoiding redundant calculations. If not, it computes the result recursively and stores it in the `memo` dictionary before returning it. This optimization significantly reduces the time complexity from exponential to linear, making it much more efficient for larger values of `n`.
# Memoization is particularly effective in this problem because the number of ways to climb stairs grows exponentially without it, but with memoization, we can compute the result in linear time.
# Memoization is a powerful technique that can be applied to many recursive problems, especially those that involve overlapping subproblems, such as the Fibonacci sequence, dynamic programming problems, and more. By caching results, we can avoid redundant calculations and improve the performance of our algorithms significantly.
# Memoization is basically recusrssion with memory. It is a top-down approach to solving problems, where we start with the original problem and break it down into smaller subproblems, storing the results of those subproblems to avoid redundant calculations. This is in contrast to a bottom-up approach, where we would start with the smallest subproblems and build up to the original problem iteratively. Both approaches can be effective, but memoization can often be more intuitive and easier to implement for certain types of problems.
# In summary, memoization is a powerful technique that can significantly improve the performance of recursive functions by caching results and avoiding redundant calculations. It is particularly effective in problems with overlapping subproblems, such as the climbing stairs problem, and can be applied to a wide range of recursive algorithms to optimize their performance.

# Tabulation
def climbStairs(n):
    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 2
    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]
    return ways[n]
print(climbStairs(6))

#Tabulation is a dynamic programming technique that uses a bottom-up approach to solve problems. In this implementation of the `climbStairs` function, we create an array called `ways` where `ways[i]` will store the number of distinct ways to climb `i` stairs. We initialize the base cases for 1 and 2 stairs, and then we iteratively fill in the array for all values from 3 to `n` using the relation that the number of ways to climb `i` stairs is the sum of the ways to climb `i-1` and `i-2` stairs. Finally, we return the value at `ways[n]`, which gives us the number of distinct ways to climb `n` stairs. This approach has a time complexity of O(n) and a space complexity of O(n) due to the array used for tabulation.
# Tabulation is an efficient way to solve problems that can be broken down into smaller subproblems, and it avoids the overhead of recursive function calls by using an iterative approach. It is particularly useful for problems like the climbing stairs problem, where the number of ways to climb a certain number of stairs can be expressed in terms of the number of ways to climb smaller numbers of stairs. By filling in the `ways` array iteratively, we can compute the result in linear time and space, making it a practical solution for larger values of `n`.
# Tabulation is a powerful technique that can be applied to a wide range of problems, especially those that involve optimization or counting. It allows us to build up solutions iteratively and can often lead to more efficient algorithms compared to recursive approaches, especially when dealing with large input sizes. By using tabulation, we can avoid the overhead of recursive calls and achieve better performance while still maintaining clarity in our code.
# Tabulation is a bottom-up approach to solving problems, where we start with the smallest subproblems and build up to the original problem iteratively. This is in contrast to a top-down approach, where we would start with the original problem and break it down into smaller subproblems recursively. Both approaches can be effective, but tabulation can often be more efficient for certain types of problems, especially when dealing with large input sizes, as it avoids the overhead of recursive function calls. In summary, tabulation is a powerful technique that can significantly improve the performance of algorithms by building up solutions iteratively and avoiding redundant calculations.
# In summary, both memoization and tabulation are powerful techniques in dynamic programming that can significantly improve the performance of algorithms by avoiding redundant calculations. Memoization is a top-down approach that uses recursion and caching, while tabulation is a bottom-up approach that builds up solutions iteratively. The choice between the two techniques depends on the specific problem being solved and the programmer's preference for code clarity and maintainability.

# Tribonacci Number Problem
def tribonacci(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
print(tribonacci(4))

#  Min Cost Climbing Stairs Problem
