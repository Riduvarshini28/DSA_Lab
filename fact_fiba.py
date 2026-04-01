def fact_rec(n):
    if n <= 1: return 1
    return n * fact_rec(n-1)

print(fact_rec(5))

def fact_iter(n):
    res = 1
    for i in range(1, n+1): res *= i
    return res

print(fact_iter(5))

def fib_rec(n):
    if n <= 1: return n
    return fib_rec(n-1) + fib_rec(n-2)

print([fib_rec(i) for i in range(6)])

def fib_iter(n):
    a,b=0,1
    for _ in range(n):
        print(a,end=" ")
        a,b=b,a+b

fib_iter(6)