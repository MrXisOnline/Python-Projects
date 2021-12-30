import cv2

# detect face in image

# giving trained data to cv2 it returns the trained data
trained_face_data = cv2.CascadeClassifier("data.xml")

# # choose img
# img = cv2.imread("test_img.jpg")
# img2 = cv2.imread("test_img2.jpg")

# # greyscale images
# greyscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # detect faces and give coordinates
# face_cor = trained_face_data.detectMultiScale(greyscale_img)
# # print(face_cor)

# # draw rectangle around face
# for (x,y,w,h) in face_cor:
# 	cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255) ,2)

# cv2.imshow("Face Detector", img)
# cv2.waitKey()

# detect face in video

# creating webcam object
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# iterating over frames
try:
	while True:
		# reading frames
		suc_frame, frame = webcam.read()
		# greyscale images
		greyscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# detect faces and give coordinates
		face_cor = trained_face_data.detectMultiScale(greyscale_img)
		# print(face_cor)

		# draw rectangle around face
		for (x,y,w,h) in face_cor:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255) ,2)

		cv2.imshow("Face Detector", frame)
		key = cv2.waitKey(1)

		if key == 81 or key == 113:
			break
except KeyboardInterrupt:
	print("DONE")
finally:
	webcam.release()