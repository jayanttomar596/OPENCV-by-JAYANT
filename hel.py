import cv2

path = 'dtu.jpg'
img = cv2.imread(path)

cv2.imshow("Original",img)
cv2.waitKey(0)