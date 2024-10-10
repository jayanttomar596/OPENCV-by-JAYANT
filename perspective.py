"""
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
# print(img)
# img[:]= 255,0,0

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img," OPENCV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)

cv2.imshow("Image",img)

cv2.waitKey(0)
"""

import cv2
import numpy as np

img = cv2.imread("card.jpeg")

width,height = 250,350
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)