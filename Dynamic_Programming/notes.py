def climbStairs(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return climbStairs(n-1)+climbStairs(n-2)
climbStairs(5)
print(climbStairs(6))
# This is a recursive solution to the problem of climbing stairs. The function `climbStairs` takes an integer `n` as input, which represents the number of stairs. The function returns the number of distinct ways to climb to the top of the stairs.
# The base cases are defined for `n=1` and `n=2`, where there is only one way to climb one stair and two ways to climb two stairs (either taking one step twice or taking two steps at once). For `n` greater than 2, the function calls itself recursively to calculate the number of ways to climb the stairs by summing the results of climbing `n-1` and `n-2` stairs. This is because to reach the nth stair, you can either take a single step from the (n-1)th stair or take a double step from the (n-2)th stair.
# The output of `climbStairs(5)` will be 8, and the output of `climbStairs(6)` will be 13, which are the number of distinct ways to climb 5 and 6 stairs, respectively. 

#Memoization

memo={}
def climbStairs()