import web
import math
from threading import Thread
# import calibrateBerryIMU
import time
import MTTEst
from MTTEst import Test
import IMU
#from Median import Median


urls = (
    '/', 'index'
)

def get_y_rotation(x, y, z):
    radians = math.atan2(x, dist(y, z))
    return -math.degrees(radians)


def get_x_rotation(x, y, z):
    radians = math.atan2(y, dist(x, z))
    return math.degrees(radians)


def dist(a, b):
    return math.sqrt((a*a)+(b*b))

class index:
    test = Test()
    numberIndex = test.getTimer()
    def GET(self):
        #numer = self.test.number

        gyr_x = IMU.readACCx()
        gyr_y = IMU.readACCy()
        gyr_z = IMU.readACCz()
        """
        #return str(get_x_rotation(gyr_x,gyr_y,gyr_z)) + " " + str(get_y_rotation(gyr_x,gyr_y,gyr_z))
        #return " " + str(IMU.readGYRx()) + " " + str(IMU.readGYRy()) + " " + str(IMU.readGYRz())
        #return " " + str(berryIMU.gyroXangle) + " " + str(berryIMU.gyroYangle) + " " + str(berryIMU.gyroZangle)
        berryIMU.gyroXangle
        """
        return "TEST"

    def time(self, thread, delay):
        while True:
            print("TEST")
            time.sleep(2)

    def Main(self):
        t1 = Thread(target=self.time, args=("Thread",2))
        t1.start()

if __name__ == "__main__":
    #t = index()
    #t.Main()
    app = web.application(urls, globals())
    app.run()
