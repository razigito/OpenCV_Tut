import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# img=plt.imread('badminton.jpg') #plt.imread() is used to read the image in matplotlib library
# plt.imshow(img)
# plt.show()


img=cv.imread('badminton.jpg')


# # #1. draw a line
# cv.line(img,(192,100),(276,163),(0,0,255),3)    #(192,100) is the starting point and (276,163) is the ending point
#                                                 #(0,0,255) is the color of the line and 3 is the thickness of the line
#                                                #OpenCV's cv2.line() only accepts pixel coordinates as tuples of integers. Floats are invalid because a pixel can’t be partially between two locations.
# cv.imshow('line',img)

# #2. draw a rectangle
# cv.rectangle(img,(240,125),(325,200),(0,255,0),3) #(240,125) is the starting point and (325,200) is the ending point, diagonal points
#                                                 #(0,255,0) is the color of the rectangle and 3 is the thickness of the rectangle
# cv.imshow('rectangle',img)

# #3. draw a circle
# cv.circle(img,(280,160),50,(0,0,255),3) #(280,160) is the center of the circle and 50 is the radius of the circle
# cv.imshow('circle',img)

# #fill the circle
# cv.circle(img,(280,160),50,(0,0,255),-1) #-1 , give -ve thickness to fill the circle
# cv.imshow('filled circle',img)

   





cv.waitKey(0)
cv.destroyAllWindows()




