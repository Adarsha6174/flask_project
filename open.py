import cv2
import numpy as np
# a=np.zeros([100,100],dtype=np.uint8)
# b=np.ones([100,100],dtype=np.uint8)*255
# print(a)
# cv2.imshow('black',a)
# cv2.imshow('bl',b)   #matrix is a class in opencv
# print(b[5,5])
# img=cv2.imread('F:\python\241452293_233440835460418_2138771756921495623_n.jpg')
# cv2.imshow('onw',img)
# hist=cv2.equalizeHist(img)
# cv2.imshow('abc',hist)
# cv2.waitKey(50000)
# cv2.destroyAllWindows()
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    ret,frame=cap.read()
    cv2.imshow('one',frame)
    if cv2.waitKey(20)==32:
        break
cap.release()