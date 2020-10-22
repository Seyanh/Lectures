## Print String
s = "hello"
print("String=%s" % s)
print("String=%10s" % s) ## ADD SPACE ON THE LEFT SIDE
print("String=%-10sEND" % s)
    
## Print Int
x = 5
print('Num =%d' % x)
print('Num =%5d' % x)
print('Num =%-5dEND' % x)
print('Num =%05d' % x)

## Complex setting
print('Num =%*.*d' % (5,4,x))
print('Num =%*.*d' % (5,4,789))
    
## Print Float
import math
print('PI = %f' % math.pi)
print('PI = %10.3f' % math.pi)
print('PI = %-10.3fEND' % math.pi)


## Print With Format
print('%r %r %r' % (1, 2, 3))
print('%r %r %r' % ('one', 'two', 'three'))

## Print With Position Index
A = 'XP'
B = 'Hello!'
print("{1}, my name is {0}".format(A, B))

## Print With Position Index
print("{HI}, my name is {NAME}".format(NAME=A, HI=B))

## Print With List
person = ['XP', 'Hello!']
print('{PEOPLE[1]}, my name is {PEOPLE[0]}'.format(PEOPLE = person))

## Define a Template
FormatSTR = "{1} and {0} are string types"
FormatSTR.format(A, B)

## USE f-string
C = 1.234
D = 1234
S = f"{B.replace('ello!', 'i')}, my name is '{A}'! \nRound float: {C:.2f} and Exponential Format: {D:e}"
print(S)


## Format OUTPUT
a = 123.456789
print('Float Number:{0:4.2f}'.format(4.1234))
s = 'abc'
print('First method: Number: {:2.1f} and string: {}'.format(24.12, 1231.123))
print('Second method: Number: %2.1f and string: %s' % (24.12, 1231.123))
## align : ^, <, > For Center, Left, Right alignment
print("{0:0.3f} VS ${1:<10s}$".format(a, s))
print("{0:2.2f} VS ${1:>10s}$".format(a, s))
print("{0:5.5f} VS ${1:^10s}$".format(a, s)) ## Question: Where is '8'?