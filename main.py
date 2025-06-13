import cv2 as cv
import numpy as np

img3 = cv.imread('cat.jpg')

cv.imshow('original', img3)


# #ROTATE 90 DEGREES clockwise
# image_rotate_90 = cv.rotate(img3, cv.ROTATE_90_CLOCKWISE)
# cv.imshow('rotate 90', image_rotate_90)

# #ROTATE 90 DEGREES counterclockwise
# image_rotate_90 = cv.rotate(img3, cv.ROTATE_90_COUNTERCLOCKWISE)
# cv.imshow('rotate counterclockwise', image_rotate_90)

# #ROTATE 360 DEGREES
# image_rotate_360 = cv.rotate(img3, cv.ROTATE_180)
# cv.imshow('rotate 360', image_rotate_360)


#Rotattion matrix 2d, rotate from center of the image
rows, cols, channels = img3.shape
center = (cols/2, rows/2)
print(center)
M = cv.getRotationMatrix2D(center, 45, 1)
image_rotate = cv.warpAffine(img3, M, (cols, rows))
cv.imshow('rotate 45', image_rotate)
















cv.waitKey(0)
cv.destroyAllWindows()







