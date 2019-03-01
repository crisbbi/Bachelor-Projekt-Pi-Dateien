import smbus2
import time

from LSM9DS1 import *

bus = smbus2.SMBus(1)


def detectIMU():
    # Detect which version of BerryIMU is connected.
    # BerryIMUv2 uses the LSM9DS1
    try:
        # Check for LSM9DS1
        # If no LSM9DS1 is conencted, there will be an I2C bus error and the program will exit.
        # This section of code stops this from happening.
        WHO_XG_response = (bus.read_byte_data(GYR_ADDRESS, WHO_AM_I_XG))
        WHO_M_response = (bus.read_byte_data(MAG_ADDRESS, WHO_AM_I_M))

    except IOError as f:
        print
        ''  # need to do something here, so we just print a space
    else:
        if (WHO_XG_response == 0x68) and (WHO_M_response == 0x3d):
            print
            "Found LSM9DS1"

    time.sleep(1)


def writeAG(register, value):
    bus.write_byte_data(ACC_ADDRESS, register, value)
    return -1


def writeACC(register, value):
    bus.write_byte_data(ACC_ADDRESS, register, value)
    return -1


def writeMAG(register, value):
    bus.write_byte_data(MAG_ADDRESS, register, value)
    return -1


def writeGRY(register, value):
    bus.write_byte_data(GYR_ADDRESS, register, value)
    return -1


def readACCx():
    acc_l = bus.read_byte_data(ACC_ADDRESS, OUT_X_L_XL)
    acc_h = bus.read_byte_data(ACC_ADDRESS, OUT_X_H_XL)
    acc_combined = (acc_l | acc_h << 8)

    return acc_combined if acc_combined < 32768 else acc_combined - 65536


def readACCy():
    acc_l = bus.read_byte_data(ACC_ADDRESS, OUT_Y_L_XL)
    acc_h = bus.read_byte_data(ACC_ADDRESS, OUT_Y_H_XL)
    acc_combined = (acc_l | acc_h << 8)

    return acc_combined if acc_combined < 32768 else acc_combined - 65536


def readACCz():
    acc_l = bus.read_byte_data(ACC_ADDRESS, OUT_Z_L_XL)
    acc_h = bus.read_byte_data(ACC_ADDRESS, OUT_Z_H_XL)
    acc_combined = (acc_l | acc_h << 8)

    return acc_combined if acc_combined < 32768 else acc_combined - 65536


def readMAGx():
    mag_l = bus.read_byte_data(MAG_ADDRESS, OUT_X_L_M)
    mag_h = bus.read_byte_data(MAG_ADDRESS, OUT_X_H_M)
    mag_combined = (mag_l | mag_h << 8)
    return mag_combined if mag_combined < 32768 else mag_combined - 65536


def readMAGy():
    mag_l = bus.read_byte_data(MAG_ADDRESS, OUT_Y_L_M)
    mag_h = bus.read_byte_data(MAG_ADDRESS, OUT_Y_H_M)
    mag_combined = (mag_l | mag_h << 8)

    return mag_combined if mag_combined < 32768 else mag_combined - 65536


def readMAGz():
    mag_l = bus.read_byte_data(MAG_ADDRESS, OUT_Z_L_M)
    mag_h = bus.read_byte_data(MAG_ADDRESS, OUT_Z_H_M)
    mag_combined = (mag_l | mag_h << 8)

    return mag_combined if mag_combined < 32768 else mag_combined - 65536


def readGYRx():
    gyr_l = bus.read_byte_data(GYR_ADDRESS, OUT_X_L_G)
    gyr_h = bus.read_byte_data(GYR_ADDRESS, OUT_X_H_G)
    gyr_combined = (gyr_l | gyr_h << 8)

    return gyr_combined if gyr_combined < 32768 else gyr_combined - 65536


def readGYRy():
    gyr_l = bus.read_byte_data(GYR_ADDRESS, OUT_Y_L_G)
    gyr_h = bus.read_byte_data(GYR_ADDRESS, OUT_Y_H_G)
    gyr_combined = (gyr_l | gyr_h << 8)

    return gyr_combined if gyr_combined < 32768 else gyr_combined - 65536


def readGYRz():
    gyr_l = bus.read_byte_data(GYR_ADDRESS, OUT_Z_L_G)
    gyr_h = bus.read_byte_data(GYR_ADDRESS, OUT_Z_H_G)
    gyr_combined = (gyr_l | gyr_h << 8)

    return gyr_combined if gyr_combined < 32768 else gyr_combined - 65536


def writeACC(register, value):
    bus.write_byte_data(ACC_ADDRESS, register, value)
    return -1


def writeMAG(register, value):
    bus.write_byte_data(MAG_ADDRESS, register, value)
    return -1


def writeGRY(register, value):
    bus.write_byte_data(GYR_ADDRESS, register, value)
    return -1


def readACCx():
    acc_l = bus.read_byte_data(ACC_ADDRESS, OUT_X_L_XL)
    acc_h = bus.read_byte_data(ACC_ADDRESS, OUT_X_H_XL)

    acc_combined = (acc_l | acc_h << 8)
    return acc_combined if acc_combined < 32768 else acc_combined - 65536


def readACCy():
    acc_l = bus.read_byte_data(ACC_ADDRESS, OUT_Y_L_XL)
    acc_h = bus.read_byte_data(ACC_ADDRESS, OUT_Y_H_XL)

    acc_combined = (acc_l | acc_h << 8)
    return acc_combined if acc_combined < 32768 else acc_combined - 65536


def readACCz():
    acc_l = bus.read_byte_data(ACC_ADDRESS, OUT_Z_L_XL)
    acc_h = bus.read_byte_data(ACC_ADDRESS, OUT_Z_H_XL)

    acc_combined = (acc_l | acc_h << 8)
    return acc_combined if acc_combined < 32768 else acc_combined - 65536


def readMAGx():
    mag_l = bus.read_byte_data(MAG_ADDRESS, OUT_X_L_M)
    mag_h = bus.read_byte_data(MAG_ADDRESS, OUT_X_H_M)

    mag_combined = (mag_l | mag_h << 8)
    return mag_combined if mag_combined < 32768 else mag_combined - 65536


def readMAGy():
    mag_l = bus.read_byte_data(MAG_ADDRESS, OUT_Y_L_M)
    mag_h = bus.read_byte_data(MAG_ADDRESS, OUT_Y_H_M)

    mag_combined = (mag_l | mag_h << 8)
    return mag_combined if mag_combined < 32768 else mag_combined - 65536


def readMAGz():
    mag_l = bus.read_byte_data(MAG_ADDRESS, OUT_Z_L_M)
    mag_h = bus.read_byte_data(MAG_ADDRESS, OUT_Z_H_M)

    mag_combined = (mag_l | mag_h << 8)
    return mag_combined if mag_combined < 32768 else mag_combined - 65536


def readGYRx():
    gyr_l = bus.read_byte_data(GYR_ADDRESS, OUT_X_L_G)
    gyr_h = bus.read_byte_data(GYR_ADDRESS, OUT_X_H_G)

    gyr_combined = (gyr_l | gyr_h << 8)
    return gyr_combined if gyr_combined < 32768 else gyr_combined - 65536


def readGYRy():
    gyr_l = bus.read_byte_data(GYR_ADDRESS, OUT_Y_L_G)
    gyr_h = bus.read_byte_data(GYR_ADDRESS, OUT_Y_H_G)

    gyr_combined = (gyr_l | gyr_h << 8)
    return gyr_combined if gyr_combined < 32768 else gyr_combined - 65536


def readGYRz():
    gyr_l = bus.read_byte_data(GYR_ADDRESS, OUT_Z_L_G)
    gyr_h = bus.read_byte_data(GYR_ADDRESS, OUT_Z_H_G)

    gyr_combined = (gyr_l | gyr_h << 8)
    return gyr_combined if gyr_combined < 32768 else gyr_combined - 65536


def initIMU():
    # initialise the gyroscope
    writeGRY(CTRL_REG4, 0b00111000)  # z, y, x axis enabled for gyro
    writeGRY(CTRL_REG1_G, 0b10111000)  # Gyro ODR = 476Hz, 2000 dps
    writeGRY(ORIENT_CFG_G, 0b00111000)  # Swap orientation

    # initialise the accelerometer
    writeACC(CTRL_REG5_XL, 0b00111000)  # z, y, x axis enabled for accelerometer
    writeACC(CTRL_REG6_XL, 0b00101000)  # +/- 16g

    # initialise the magnetometer
    writeMAG(CTRL_REG1_M, 0b10011100)  # Temp compensation enabled,Low power mode mode,80Hz ODR
    writeMAG(CTRL_REG2_M, 0b01000000)  # +/-12gauss
    writeMAG(CTRL_REG3_M, 0b00000000)  # continuos update
    writeMAG(CTRL_REG4_M, 0b00000000)  # lower power mode for Z axis
