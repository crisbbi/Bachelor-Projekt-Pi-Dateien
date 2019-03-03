# This class starts the Server.py as Server and berryIMU.py as berryIMU as separate threads.
# This way it's possible to both calculate on the Raspberry Pi and provide the kalmanX and kalmanY values to a client.
# It includes globalKalman.py as globalKalman to provide kalmanX and kalmanY as shared variables for both threads

import berryIMU
import globalKalman
from Server import initServer

globalKalman.initGlobalKalmanX()
# debugging
print("globalKalman.X")
globalKalman.initglobalKalmanY()
# debugging
print("globalKalman.Y")

berry = berryIMU.CalculationClass()
berry.start()
# debugging
print("berry start")
initServer()