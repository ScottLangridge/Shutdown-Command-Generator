import os

def getTimeInSecs(time):
    time = time.split(".")

    seconds = 0

    i = len(time) - 1
    place = 0
    mult = 60 ** (i)

    while i >= 0:
        seconds += int(time[place]) * mult
        i -= 1
        place += 1
        mult = int(mult/60)

    return seconds



SHUTDOWN = "shutdown -s -t"
CANCEL = "shutdown -a"
first = True
while True:
    print("")
    print("--- Shutdown Time Calculator ---");
    if first:
        totalSecs = getTimeInSecs(input("Input total time in the"
                                        + " form [hr.min.sec] :\n"))
    else:
        newSecs = input("Input total time in the form [hr.min.sec]. Leave"
                        + " blank to use old time:\n")
        if newSecs != "":
            totalSecs = newSecs

    currentSecs = getTimeInSecs(input("Input current time in the"
                                          + " form [hr.min.sec] :\n"))

    shutdownCommand = SHUTDOWN + " " + str(totalSecs - currentSecs)
    input("\n> Hit enter to start shutdown timer.")
    print(shutdownCommand)
    os.system(shutdownCommand)
    print("")
    input("> Hit enter to cancel shutdown.")
    print(CANCEL)
    os.system(CANCEL)
    print("")
    first = False
