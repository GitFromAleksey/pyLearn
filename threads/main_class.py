import time
import threading


class MyThread(threading.Thread):
    
    def __init__(self, num, pause):
##        super().__init__(self, name = 'threddy' + num)
        super().__init__(name = 'thread' + num)
        self.num = num
        self.pause = pause
        self.CallbackExtern = None

    def run(self):
        print('start thread:'+ self.name + '\r\n')
        self.thread_enble = True
        while(self.thread_enble):
            time.sleep(self.pause)
            print(self.name)
            if self.CallbackExtern != None:
                self.CallbackExtern(self.name)
        print('stop thread:' + self.name)

    def stop(self):
        self.thread_enble = False

    def SetCallback(self, Callback):
        self.CallbackExtern = Callback

    def Callback(self, text):
        print(self.name + '.Callback from ' + text)

def PrintActiveThreads():
    print('thread count: %i' % threading.active_count())
    for thread in threading.enumerate():
        print('thread:',thread.getName())

def main():
    print(threading.main_thread())
    PrintActiveThreads()
    
    
    thr_1 = MyThread('1', 1)
    thr_2 = MyThread('2', 2)

    thr_1.SetCallback(thr_2.Callback)
    thr_2.SetCallback(thr_1.Callback)
    
    PrintActiveThreads()
    
    thr_1.start()
    thr_2.start()

    PrintActiveThreads()

    time.sleep(10)
    
    thr_1.stop()
    thr_2.stop()

    thr_1.join()
    thr_2.join()

    PrintActiveThreads()
    
    print('end of program')
    pass

if __name__ == '__main__':
    main()
