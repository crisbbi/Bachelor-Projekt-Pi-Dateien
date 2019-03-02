import web
import math
from threading import Thread
import calibrateBerryIMU
import time
import IMU


urls = (
    '/', 'Index'
)

def get_y_rotation(x, y, z):
    radians = math.atan2(x, dist(y, z))
    return -math.degrees(radians)


def get_x_rotation(x, y, z):
    radians = math.atan2(y, dist(x, z))
    return math.degrees(radians)


def dist(a, b):
    return math.sqrt((a*a)+(b*b))

class Index:
    def GET(self):
        gyr_x = IMU.readACCx()
        gyr_y = IMU.readACCy()
        gyr_z = IMU.readACCz()

        print(str(get_x_rotation(gyr_x,gyr_y,gyr_z)) + " " + str(get_y_rotation(gyr_x,gyr_y,gyr_z)))

        return str(get_x_rotation(gyr_x,gyr_y,gyr_z)) + " " + str(get_y_rotation(gyr_x,gyr_y,gyr_z))
        return " " + str(IMU.readGYRx()) + " " + str(IMU.readGYRy()) + " " + str(IMU.readGYRz())
        return " " + str(berryIMU.gyroXangle) + " " + str(berryIMU.gyroYangle) + " " + str(berryIMU.gyroZangle)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
