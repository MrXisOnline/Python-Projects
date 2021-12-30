import os
import time

def inc_per(pers, ite):
    if pers == 100:
        pers = -1
    else:
        pers = pers + 1
        ite = ite + 1
    op_scr(pers, ite)


def op_scr(pers, ite):
    if pers == -1:
        os.system("echo Attack Successful")
    else:
        msg = "Processing " + str(pers) + "% " + "[" + "".rjust(ite, "=") + "]"
        os.system("echo " + msg)
        time.sleep(0.1)
        os.system("cls")
        os.system("exit")
        inc_per(pers, ite)


it = 0
per = 0
print("Starting Attack ...")
inc_per(per, it)

# print(per)
