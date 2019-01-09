import glob
from builtins import type, list

pathes = glob.glob("C:\WorkSpa*\ma*\*")


print(type(pathes))
print(pathes.__len__())
for path in pathes:
    print(path)
print(path)


conf = {
    'src': {'pth':['0_Sm', '0_Src'], 'tgt':'main'},
    'tst': {'pth':['tests'], 'tgt':'test_'},
    }

print(type(conf))

def print_dict(dict_):
    for key, val in dict_.items():
        print(type(key), type(val))
        if type(key) == dict:
            print_dict(key)
        elif type(key) == list:
            for l in key:
                print(l)

print_dict(conf)


def ret(list):
    return (v for v in list)

list = 'Privet blia!'

r = ret(list)
print(type(r))
for v in r:
    print(v)
