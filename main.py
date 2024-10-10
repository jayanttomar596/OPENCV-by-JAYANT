import cv2 

img = cv2.imread("dtu.jpg")
height, width, channels = img.shape

new_width = width // 2
new_height = height // 2

imgResize = cv2.resize(img,(new_width,new_height))

cv2.imshow("Image",imgResize)
cv2.waitKey(0)