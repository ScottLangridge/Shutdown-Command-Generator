import os
import time
from VirtualKeyboard import VirtualKeyboard


def getTimeInSecs(time):
    if time == '': time = '0'
    time = time.split(".")

    seconds = 0

    i = len(time) - 1
    place = 0
    mult = 60 ** (i)

    while i >= 0:
        seconds += int(time[place]) * mult
        i -= 1
        place += 1
        mult = int(mult / 60)

    return seconds


def tab_and_playpause():
    vk.hold_keys('#alt_tab#')
    vk.key_stroke('space')
    vk.hold_keys('#alt_tab#')


SHUTDOWN = "shutdown -s -t"
CANCEL = "shutdown -a"
vk = VirtualKeyboard()

print("")
print("--- Shutdown Time Calculator ---");
totalSecs = getTimeInSecs(input("Input total time in the"
                                + " form [hr.min.sec] :\n"))
currentSecs = getTimeInSecs(input("Input current time in the"
                                  + " form [hr.min.sec] :\n"))

while True:
    shutdownCommand = SHUTDOWN + " " + str(totalSecs - currentSecs)
    input("\n> Ensure you will alt tab into media player then hit enter to start program.")
    start_time = time.time()
    tab_and_playpause()
    print(shutdownCommand)
    os.system(shutdownCommand)
    first = False
    print("")

    input("> Hit enter to pause shutdown.")
    currentSecs -= int(start_time - time.time())
    tab_and_playpause()
    print(CANCEL)
    os.system(CANCEL)
    print("")
