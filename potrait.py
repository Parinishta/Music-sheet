import cv2
import numpy as np
img=cv2.imread("../../Documents/mep/ts/taylor-Swift-quotes (1).jpg")
width,height =250,350
pts1= np.float32([[19,53],[265,64],[16,317],[260,320]])
pts2= np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix= cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("output",imgOutput)
cv2.waitKey(0)