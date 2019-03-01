from threading import Thread
import time


class Test:
    global numbers
    print("TEEEEST")
    def timer(self, thread, delay):
        number = 1
        while True:
            number+=1
            time.sleep(1)
            print(str(time.ctime(time.time())) + " " + thread)

    def getTimer(self):
        return self.numbers

    def Main(self):
        t1 = Thread(target=self.timer, args=("TEST1", 3))
        t1.start()
        t2 = Thread(target=self.timer, args=("TEST2232", 6))
        t2.start()

    def __init__(self):
        self.numbers = 10

if __name__ == "__main__":
    test = Test()
    test.Main()
