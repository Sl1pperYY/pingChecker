from ping3 import ping, verbose_ping
from elevate import elevate
import time
elevate()

inputTime = int(input("Please enter how many minutes you want to test for: "))

t_end = time.time() + 60 * inputTime

while time.time() < t_end:
    timeMs = int(1000 * (ping("104.160.141.3")))
    if timeMs > 70:
        print(timeMs)

