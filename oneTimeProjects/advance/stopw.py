import time
import os


def as_ki():
    assert KeyboardInterrupt


laps = {}
lap_num = 1

while True:
    try:
        print("Press Enter or Ctrl^C")
        a = input()
        print("recording lap...")
        start = float(time.time())
        print("Press to Stop Lap...")
        os.system("pause")
        end = float(time.time())
        as_ki()
        avg_time = end - start
        laps[lap_num] = avg_time
        print("lap :", lap_num, " <=> ", "{:.2f}".format(avg_time), "s", sep="")
        lap_num = lap_num + 1
    except KeyboardInterrupt:
        print("\ndone\n")
        for i in laps.keys():
            print("Lap :", i, " <=> " + "{:.2f}".format(laps[i]) + "s")
        break
