import web
import datetime
from threading import Thread
from flask import Flask
import sys
import time
import math
import IMU
import datetime
import os

# If the IMU is upside down (Skull logo facing up), change this value to 1
IMU_UPSIDE_DOWN = 0

RAD_TO_DEG = 57.29578
M_PI = 3.14159265358979323846
G_GAIN = 0.070  # [deg/s/LSB]  If you change the dps for gyro, you need to update this value accordingly
AA = 0.40  # Complementary filter constant
MAG_LPF_FACTOR = 0.4  # Low pass filter constant magnetometer
ACC_LPF_FACTOR = 0.4  # Low pass filter constant for accelerometer
ACC_MEDIANTABLESIZE = 9  # Median filter table size for accelerometer. Higher = smoother but a longer delay
MAG_MEDIANTABLESIZE = 9  # Median filter table size for magnetometer. Higher = smoother but a longer delay

################# Compass Calibration values ############
# Use calibrateBerryIMU.py to get calibration values
# Calibrating the compass isnt mandatory, however a calibrated
# compass will result in a more accurate heading value.

# real measured values
# run callibrateIMU.py for new values
magXmin =  -845
magYmin =  -769
magZmin =  -1303
magXmax =  1489
magYmax =  1563
magZmax =  350

# Variables for simpler measurement calculations/filters
gyroXangle = 0.0
gyroYangle = 0.0
gyroZangle = 0.0
CFangleX = 0.0
CFangleY = 0.0
CFangleXFiltered = 0.0
CFangleYFiltered = 0.0
oldXMagRawValue = 0
oldYMagRawValue = 0
oldZMagRawValue = 0
oldXAccRawValue = 0
oldYAccRawValue = 0
oldZAccRawValue = 0

# used for loop period calculation in berechnung()
a = datetime.datetime.now()

# Detect if BerryIMUv1 or BerryIMUv2 is connected
IMU.detectIMU()
# Initialise the accelerometer, gyroscope and compass
IMU.initIMU()

urls = (
    '/', 'index'
)

class index:

    def berechnung(self):
        while True:
            global gyroXangle
            global gyroYangle
            global gyroZangle
            global a
            global oldXMagRawValue
            global oldYMagRawValue
            global oldZMagRawValue
            global oldXAccRawValue
            global oldYAccRawValue
            global oldZAccRawValue
            global CFangleX
            global CFangleY

            # Read the accelerometer,gyroscope and magnetometer values
            ACCx = IMU.readACCx()
            ACCy = IMU.readACCy()
            ACCz = IMU.readACCz()
            GYRx = IMU.readGYRx()
            GYRy = IMU.readGYRy()
            GYRz = IMU.readGYRz()
            MAGx = IMU.readMAGx()
            MAGy = IMU.readMAGy()
            MAGz = IMU.readMAGz()

            # Apply compass calibration
            MAGx -= (magXmin + magXmax) / 2
            MAGy -= (magYmin + magYmax) / 2
            MAGz -= (magZmin + magZmax) / 2

            # Calculate loop Period(LP). How long between Gyro Reads
            b = datetime.datetime.now() - a
            a = datetime.datetime.now()
            LP = b.microseconds / (1000000 * 1.0)
            #print("Loop Time | %5.2f|" % (LP),)

            ###############################################
            #### Apply low pass filter ####
            ###############################################
            MAGy = MAGy * MAG_LPF_FACTOR + oldYMagRawValue * (1 - MAG_LPF_FACTOR)
            MAGz = MAGz * MAG_LPF_FACTOR + oldZMagRawValue * (1 - MAG_LPF_FACTOR)
            MAGx = MAGx * MAG_LPF_FACTOR + oldXMagRawValue * (1 - MAG_LPF_FACTOR)

            oldXMagRawValue = MAGx
            oldYMagRawValue = MAGy
            oldZMagRawValue = MAGz
            oldXAccRawValue = ACCx
            oldYAccRawValue = ACCy
            oldZAccRawValue = ACCz

            # Convert Gyro raw to degrees per second
            rate_gyr_x = GYRx * G_GAIN
            rate_gyr_y = GYRy * G_GAIN
            rate_gyr_z = GYRz * G_GAIN

            # Calculate the angles from the gyro.
            gyroXangle += rate_gyr_x * LP
            gyroYangle += rate_gyr_y * LP
            gyroZangle += rate_gyr_z * LP

            # Convert Accelerometer values to degrees

            if not IMU_UPSIDE_DOWN:
                # If the IMU is up the correct way (Skull logo facing down), use these calculations
                AccXangle = (math.atan2(ACCy, ACCz) * RAD_TO_DEG)
                AccYangle = (math.atan2(ACCz, ACCx) + M_PI) * RAD_TO_DEG
            else:
                # Us these four lines when the IMU is upside down. Skull logo is facing up
                AccXangle = (math.atan2(-ACCy, -ACCz) * RAD_TO_DEG)
                AccYangle = (math.atan2(-ACCz, -ACCx) + M_PI) * RAD_TO_DEG

            # Change the rotation value of the accelerometer to -/+ 180 and
            # move the Y axis '0' point to up.  This makes it easier to read.
            if AccYangle > 90:
                AccYangle -= 270.0
            else:
                AccYangle += 90.0

            # Complementary filter used to combine the accelerometer and gyro values.
            CFangleX = AA * (CFangleX + rate_gyr_x * LP) + (1 - AA) * AccXangle
            CFangleY = AA * (CFangleY + rate_gyr_y * LP) + (1 - AA) * AccYangle

            if IMU_UPSIDE_DOWN:
                MAGy = -MAGy  # If IMU is upside down, this is needed to get correct heading.
            # Calculate heading
            heading = 180 * math.atan2(MAGy, MAGx) / M_PI

            # Only have our heading between 0 and 360
            if heading < 0:
                heading += 360

            ####################################################################
            ###################Tilt compensated heading#########################
            ####################################################################
            # Normalize accelerometer raw values.
            if not IMU_UPSIDE_DOWN:
                # Use these two lines when the IMU is up the right way. Skull logo is facing down
                accXnorm = ACCx / math.sqrt(ACCx * ACCx + ACCy * ACCy + ACCz * ACCz)
                accYnorm = ACCy / math.sqrt(ACCx * ACCx + ACCy * ACCy + ACCz * ACCz)
            else:
                # Us these four lines when the IMU is upside down. Skull logo is facing up
                accXnorm = -ACCx / math.sqrt(ACCx * ACCx + ACCy * ACCy + ACCz * ACCz)
                accYnorm = ACCy / math.sqrt(ACCx * ACCx + ACCy * ACCy + ACCz * ACCz)

            # Calculate pitch and roll
            pitch = math.asin(accXnorm)
            roll = -math.asin(accYnorm / math.cos(pitch))

            # Calculate the new tilt compensated values
            magXcomp = MAGx * math.cos(pitch) + MAGz * math.sin(pitch)

            # The compass and accelerometer are orientated differently on the LSM9DS0 and LSM9DS1 and the Z axis on the compass
            # is also reversed. This needs to be taken into consideration when performing the calculations
            magYcomp = MAGx * math.sin(roll) * math.sin(pitch) + MAGy * math.cos(roll) + MAGz * math.sin(
                    roll) * math.cos(
                    pitch)  # LSM9DS1

            # Calculate tilt compensated heading
            tiltCompensatedHeading = 180 * math.atan2(magYcomp, magXcomp) / M_PI

            if tiltCompensatedHeading < 0:
                tiltCompensatedHeading += 360

            ############################ END ##################################

            #print a new line
            print("")
            print(str(gyroXangle) + "," + str(gyroYangle))

            #slow program down a bit, makes the output more readable
            time.sleep(0.03)


    def threading(self):
        t1 = Thread(target=self.berechnung)
        t1.start()

#configure server
app = Flask(__name__)
@app.route('/')
def hello_world():
    global gyroXangle
    global gyroYangle
    global AccXangle
    global AccYangle
    global AccZangle
    return str(gyroXangle) + "," + str(gyroYangle)

if __name__ == "__main__":
    t = index()
    t.threading()
    app.run(host='0.0.0.0', port=8080)
