def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    a = [None] * (n + 1)
    a[1] = 1
    a[2] = 2
    for x in range(3, n+1):
        a[x] = a[x-1] + a[x-2]
    return a[n]


print(climbStairs(6))
# Dynamic Programming
