import cv2
cap = cv2.VideoCapture("lanetest.mp4")

while True:
    success , img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break