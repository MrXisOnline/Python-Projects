import cv2

train_face = cv2.CascadeClassifier("face.xml")
train_smile = cv2.CascadeClassifier("smile.xml")
train_eye = cv2.CascadeClassifier("eye.xml")
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
	suc_fr, frame = cam.read()
	if not suc_fr:
		break
	gray_fr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	face_cor = train_face.detectMultiScale(gray_fr)
	for x,y,w,h in face_cor:
		cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
		crop_img = gray_fr[y:y+h, x:x+w]
		smile_cor = train_smile.detectMultiScale(crop_img, scaleFactor=1.7, minNeighbors=20)
		for _ in smile_cor:
			font = cv2.FONT_HERSHEY_SIMPLEX
			cv2.putText(frame, "Smile", (x,y+h), font, 1, (0,255,0), 2)
		eye_cor = train_eye.detectMultiScale(crop_img)
		for x_, y_, w_, h_ in eye_cor:
			cv2.rectangle(frame, (x_,y_), (x_+w_,y_+h_), (255,255,255), 1)
	cv2.imshow("Smile Detector", frame)
	key = cv2.waitKey(1)
	if key == 81 or key == 113:
		break
cam.release()
cv2.destroyAllWindows()
