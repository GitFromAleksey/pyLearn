
knight = {'gallahad': 'the pure', 'robin': 'the brave'}

for k,v in knight.items():
    print(k,v)

for i,v in enumerate(['tic','tac','toe']):
    print(i,v)

en = enumerate(['tic','tac','toe'])
print('en',type(en))
for i,v in en:
    print(i,v)

questions = ['name','quest','favorite color']
ansvers = ['lancelot','the holy grail','blue']
for q,a in zip(questions, ansvers):
    print('what is your {0}? It is {1}'.format(q,a))

for i in reversed(range(1,10,2)):
    print(i)

basket = ['apple','orange','apple','pear','orange','banana']
for f in sorted(set(basket)):
    print(f)
