import IMU
import time
import csv
import datetime

IMU.initIMU()

with open("werte.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Zeit", "AccX", "AccY", "AccZ"])
    while True:
        AccX = IMU.readACCx()
        AccY = IMU.readACCy()
        AccZ = IMU.readACCz()
        GyrX = IMU.readGYRx()
        GyrY = IMU.readGYRy()
        GyrZ = IMU.readGYRz()
        #     # print("AccX " + str(AccX) + "\n" +
        #     #       "AccY " + str(AccY) + "\n" +
        #     #       "AccY " + str(AccZ) + "\n" +
        #     #       "GyrX " + str(GyrX) + "\n" +
        #     #       "GyrY " + str(GyrY) + "\n" +
        #     #       "GyrZ " + str(GyrZ))
        #
        writer.writerow([datetime.datetime.now().strftime("%H:%M:%S"), AccX, AccY, AccZ])
        # print("AccX " + str(GyrZ))
        time.sleep(0.5)


