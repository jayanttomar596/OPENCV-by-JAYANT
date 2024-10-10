import cv2
cap = cv2.VideoCapture("lanetest.mp4")

def getContours(img):
    countours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in countours:
        area = cv2.contourArea(cnt)
        if area>9:
            cv2.drawContours(imgContour,cnt,-1,(0,255,0),2)


while True:
    success , img = cap.read()
    if not success:
        print("Failed to read frame or end of video reached")
    imgContour = img.copy()

    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
    imgCanny = cv2.Canny(imgBlur,300,500)
    getContours(imgCanny)
    cv2.imshow("Video",imgContour)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

      

