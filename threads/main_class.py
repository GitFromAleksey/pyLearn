import time
import threading




class MyThread(threading.Thread):
    
    def __init__(self, num, pause):
##        super().__init__(self, name = 'threddy' + num)
        super().__init__(name = 'threddy' + num)
        self.num = num
        self.pause = pause
        self.thread_enble = True

    def run(self):
        while(self.thread_enble):
            time.sleep(self.pause)
            print('thr_', self.num)
        print('threddy' + self.num + 'stop')

    def stop(self):
        self.thread_enble = False



def main():
    thr_1 = MyThread('1', 1)
    thr_2 = MyThread('2', 2)

    thr_1.start()
    thr_2.start()

    time.sleep(10)
    thr_1.stop()
    thr_2.stop()

    thr_1.join()
    thr_2.join()
    
    print('end of program')
    pass

if __name__ == '__main__':
    main()
