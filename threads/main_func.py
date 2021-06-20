from threading import Thread as th
import time




def prescript(name, num, t):
    for i in range(num):
        print(name)
        time.sleep(t)


def main():
    print(dir(th))

    for item in dir(th):
        print(item,type(item))

    # target - функция, которая определяет поведение потока
    # args - список аргументов
    # var = th(target = function_name, args = (arg1, arg2,))

    thr_1 = th(target = prescript, args = ('f1.txt', 10, 1.3))
    thr_2 = th(target = prescript, args = ('f2.txt', 10, 2))
    thr_3 = th(target = prescript, args = ('f3.txt', 10, 3))

    thr_1.start()
    thr_2.start()
    thr_3.start()

    thr_1.join()
    thr_2.join()
    thr_3.join()

    print('End of program')

if __name__ == '__main__':
    main()
