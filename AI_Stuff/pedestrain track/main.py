import cv2

# img = cv2.imread("test_img.jpg")
# # img2 = cv2.imread("test_img2.png")
train_data_car = cv2.CascadeClassifier("cars.xml")
train_data_person = cv2.CascadeClassifier("person.xml")

# grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# car_cor = train_data_car.detectMultiScale(img)
# for (x,y,w,h) in car_cor:
# 	cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)
# person_cor = train_data_person.detectMultiScale(img)
# for (x,y,w,h) in person_cor:
# 	cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),2)
# cv2.imshow("pedestrain tracker", img)
# cv2.waitKey()

video = cv2.VideoCapture("test_video.mp4")
while True:
	suc_fr, img = video.read()
	if suc_fr:
		grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		car_cor = train_data_car.detectMultiScale(grey_img)
		for (x,y,w,h) in car_cor:
			cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)
		person_cor = train_data_person.detectMultiScale(grey_img)
		for (x,y,w,h) in person_cor:
			cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),2)
		cv2.imshow("pedestrain tracker", img)
		key = cv2.waitKey(1)

		if key == 81 or key == 113:
			break
	else:
		break
video.release()