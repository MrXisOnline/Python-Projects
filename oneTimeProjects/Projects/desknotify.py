import notify2
import os

def main():
	icon_img = os.getcwd() + "/ter.ico"
	notify2.init("Desk Notify")
	n = notify2.Notification()
	n.summary = "Jarvis"
	n.icon = icon_img
	n.message = "Hey Suraj, You Got A Notification.\nSuraj Wants To Meet You."
	n.set_urgency(notify2.URGENCY_NORMAL)
	n.show()
	n.set_timeout(3000)


if __name__ == '__main__':
	main()

