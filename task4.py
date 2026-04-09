def fib(n):
    if n == 1: return 0
    if n == 2: return 1
    first = 0
    second = 1
    for i in range(n-2):
        s = first + second
        first = second
        second = s
    return second
print(fib(10))