
dic = {'dict': 1, 'dictionary': 2}

print(type(dic))
print(dic)

dic = dict(short='dist', long='dictionary')

print(type(dic))
print(dic)

dic = dict([(1,1),(2,4)])

print(type(dic))
print(dic)

dic = dict.fromkeys(['a','b'])

print(type(dic))
print(dic)

dic = dict.fromkeys(['a','b'], 100)

print(type(dic))
print(dic)

dic = {a: a**2 for a in range(7)}

print(type(dic))
print(dic)

print('\nadd and extract')
dic = {1: 2, 2: 4, 3: 9}
print(dic)
print(dic[1])
dic[4] = 4**2
print(dic)

print('keys:',dic.keys())
print('values:', dic.values())

print('\nprint keys')
for key in dic.keys():
    print ('key:', key, ' val:', dic.get(key))

print('\nprint items')
for item in dic.items():
    print (item)

print('\ndic.pop():')
dic.pop(1)
print(dic)



