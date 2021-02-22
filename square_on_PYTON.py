# периметр + площядь квадрата
import math
from math import sqrt
#пользователь вводит
first = float(input(' введите сторону в см 1:'))
second  = float(input('введите сторонув см 2:'))
print('.')

if second == first:
    print('числа одинаковые')
    print('.')
else:
    print('числа разные')
    print('.')
    
def pip4(num,num0):
    return num * num0

hello = pip4(first,second)
print('площядь = ' + str(hello) + ' см^2')
print('.')
def square(num1 , num2):
    return  2*(num1  + num2) 

z  =  square(first , second)
print('периметр = ' + str(z) + ' см')
print('.')

def d (num18 , num88):
    return sqrt(num18**2 + num88**2)

f = d(first,second)
print('диагональ = ' + str(f) + ' см')
print('.')

def ball(hill1):
    return hill1/2

gg = ball(first)
print('R вписаной окружности = '+str(gg) + ' см')

def k (jj):
    return 3,14 * jj**2

ll=k(gg)
print('S вписаной окружности =' + str(ll)+'см^2')
print('.')

def R(green):
    return sqrt(green**2+green**2)/2

hh = R(first)
print('R oписаной окружности =' + str(hh)+' см')


def o(w):
    return 3,14 * w**2

rr = o(hh)
print('S описаной окружности =' + str(rr)+'см^2')

input('готово')
