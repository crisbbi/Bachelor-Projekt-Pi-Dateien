import threading
import time
import ServerTest.index
c = threading.Condition()      #shared between Thread_A and Thread_B
globalKalmanX = None

class Thread_A(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global flag
        global globalKalmanX     #made global here
        while True:
            c.acquire()
            globalKalmanX = ServerTest.index.getKalmanX()
            time.sleep(0.1)
            c.notify_all()
            c.release()