import math


number  = int(input('enter a big number:'))
number1 = int(input('enter a second big number'))

f = 1
h = 1

def factorial(n):
    if n==0:
       return 1 

    global f
    i = 0
    while i < n:
        i += 1
        f = f * i

    return f

print('факториал числа {n}равен {f}'.format
( n=number ,  f = factorial(number)))

def fac(d):
    if d==0:
        return 2 

    global h
    g = 0
    while g < d :
        g += 1
        h = h * g

    return h

print('факториал числа {d}равен {h}'.format
( d = number1 ,  h = fac(number1)))

def gg (a,b):
    return  a + b 

jj = gg(f, h)
print('.')
print("сумма факториалов = "  + str(jj))
input()
