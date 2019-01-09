import os
import time


def print_files():
    t = time.process_time()
    cnt = 0
    files_list = []
    all_list = []
    print(type(files_list))
    
    f_files = open('files.txt', 'w')
    f_dirs = open('dirs.txt', 'w')
    f_top = open('top.txt', 'w')

    for top,dirs,files in os.walk('c:\\'):
        cnt = cnt + 1
        for _dir in dirs:
            f_dirs.write(_dir + '\n');
        f_top.write(top + '\n')
        all_list.append(top)
        for file in files:
            files_list.append(file)
            all_list.append(file)

    #all_list.sort()
    for file in all_list:
        try:
            f_files.write(file + '\n')
        except Exception:
            print('cnt:',cnt, 'file_name:', file)

    f_files.close();
    f_dirs.close();
    #f_top.close();
    print('count files:',cnt)
    t = time.process_time() - t
    print('count time:', t)
    print('time per file:', t/cnt, 'sec')



my_list = os.walk('c:\\')

print('type my_list:',type(my_list))
print(my_list.throw)

my_tuple = tuple('Hello world!')

for t in my_tuple:
    print(t)

print('count my_tuple:', my_tuple.count(' '))
print('type my_tuple:',type(my_tuple))
print('my_tuple:', my_tuple)
print('my_tuple.__sizeof__():', my_tuple.__sizeof__())



#print_files()
