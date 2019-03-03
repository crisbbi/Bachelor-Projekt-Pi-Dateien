# This class starts the Server.py as Server and berryIMU.py as berryIMU as separate threads.
# This way it's possible to both calculate on the Raspberry Pi and provide the kalmanX and kalmanY values to a client.
# It includes globalKalman.py as globalKalman to provide kalmanX and kalmanY as shared variables for both threads
from _thread import start_new_thread

import berryIMU
import globalKalman
import threading
from Server import initServer

# debugging
print("globalKalman.gyrX")
globalKalman.initGyrXangle()
globalKalman.initGyrYangle()
globalKalman.initGyrZangle()

readValues = berryIMU.Sensor()

print("server start")

readValues.start()
print("readValues start")
# debugging