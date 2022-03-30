## FOR VİDEO
import cv2

face_cascade = cv2.CascadeClassifier(
    r"haarcascades/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(r"") #video path

while cap.isOpened():
    _,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    faces = face_cascade.detectMultiScale(gray,1.1,4)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0),3)

    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()








## FOR IMAGE
# img = cv2.imread(r"photos\the-walking-dead-yaraticisi-rick-grimes-filminin-diziden-farkli-olacagini-soyluyor131515_0.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# faces = face_cascade.detectMultiScale(gray,1.1,4)

# for(x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0),3)

# cv2.imshow('img',img)
# cv2.waitKey(0)