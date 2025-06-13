import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# img=plt.imread('badminton.jpg') #plt.imread() is used to read the image in matplotlib library
# plt.imshow(img)
# plt.show()


img=cv.imread('badminton.jpg')

cv.putText(img,'P V Sindhu',(250,100),cv.FONT_HERSHEY_DUPLEX,1,(0,255,255),2) #(250,100) is the starting point of the text
cv.imshow('Text',img)



cv.waitKey(0)
cv.destroyAllWindows()




