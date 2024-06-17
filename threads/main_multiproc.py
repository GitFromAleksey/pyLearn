import time
import multiprocessing as mp


def ProcFunc(proc_name:str='', val:int=0):
    t_start = time.time()
    for i in range(val):
        pass
    print(f'Process: {proc_name} stopped. Time: {time.time()-t_start}.')

def main():
    cpu_count = mp.cpu_count()
    print(f'cpu_count: {cpu_count}')

    proc_list = []
    # запуск потоков на всех ядрах
    for proc_index in range(cpu_count):
        proc = mp.Process(target=ProcFunc, args=(str(proc_index), 1000000))
        proc.start()
        proc_list.append(proc)
        # proc.join()

    # ожидание окончания всех потоков
    while len(proc_list) > 0:
        for proc in proc_list:
            if proc.is_alive() == False:
                proc_list.remove(proc)

    print(f'main thread stop.')
    # time.sleep(10)

if __name__ == '__main__':
    main()