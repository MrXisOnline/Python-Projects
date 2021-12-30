import time
from win10toast import ToastNotifier
remTime = input("Input Time in 24hr format(HH:MM:SS) to set reminder->")
remMssg = input("Enter your message:>")

notify = ToastNotifier()
notify.show_toast("Notification",remMssg)