'''
import web
from threading import Thread


urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return str(23)


class indexVar:
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
'''
from threading import Thread
import web
import time


urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return str(23)
    pass


#class myClassB(Thread):

    def test(self, thread, delay):
        while True:
            print('B')
            time.sleep(2)



    def Main(self):
        t1 = Thread(target=self.test, args=("Thread",2))
        t1.start()

if __name__ == "__main__":
    t = index()
    t.Main()
    app = web.application(urls, globals())
    app.run()



