def factorial(x):
    if x < 2 : return 1
    return x*factorial(x-1)

myFunc = lambda x, n: (x**n) / factorial(n)

def exp_x(x, n):
    total = 0
    for i in range(0, n):
        total = total + myFunc(x,n)
    return total

y = 0
def myOtherFunc(n):
    global y
    if n > 0:
        y += ((-1)**(n+1)) / n
        myOtherFunc(n-1)
    return

print(factorial(5))

print(exp_x(2,2))

myOtherFunc(2)
print(y)