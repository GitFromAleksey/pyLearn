import os
import sys
import mylife


print (sys.platform)
print ('api_version: ', sys.api_version)

print ('\r\n', 2**8)
print ('the pright side ' + 'of life')

print (mylife.title)

import threenames
dir(threenames)

hello = r"string\nfdadf"
print (hello)
hello = "string\nfdadf"
print (hello)

a, b = 0, 1
while b<10:
    print(b, end=', ')
    a,b=b,b+a

x = int(input("\nInput digit: "))
if x<0:
    x = 0
    print('x<0')
elif x == 0:
    print('x == 0')
elif x == 1:
    print('x == 1')
else:
    print('>')

a = ['cat','window','defenestrate']
for x in a:
    print(x, ' = ',len(x))

print()
for x in a[:]:
    if len(x) > 6:
        a.insert(0,x)
    
for x in a:
    print(x, end = ', ')

print()
for i in range(5):
    print(i, end = ', ')

print()
for i in range(5,10,2):
    print(i, end = ', ')

print()
print()
a = ['Mary','had','a','little','lamb']
for i in range(len(a)):
    print(i, a[i])

print()
print()
for n in range(2,10):
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            print(n, '=', x, '*', n//x)
            break
        else:
            print(n, ' - simple digit')

#while True:
    #pass


