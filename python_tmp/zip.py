

s = 'abcd'

t = (1,2,3,4)

c = [1,2,3,4]

z = zip(s,t,c)

print(type(s))
print('s', s)

print(type(t))
print('t', t)

print(type(z))
print('z', z)
print()

def print_zip(z):
    print('z - ', type(z))
    for zz in z:
        print(' ',type(zz))
        print (' ',zz)
        for zzz in zz:
            print('  ',type(zzz))
            print('  ',zzz)


z2 = list(zip(s,t,c))

z3 = zip(z,z2)

#print_zip(z)
#print_zip(z2)
print_zip(z3)
