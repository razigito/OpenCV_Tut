                        #READ, DISPLAY, & SAVE AN IMAGE


import cv2 as cv                          #importing the open cv library with alias cv

img = cv.imread('parrot.jpg')             #reading the image
#img1 = cv.imread('parrot.jpg',0)         #reading the image in grey scale

cv.imshow('Parrot', img)                  #displaying the image
#cv.imshow('Parrot-grey', img1)



#cv.imwrite('grey-parrot.jpg', img1)      #save the image


cv.waitKey(5000)                          #image will be displayed for 5 seconds

#cv.waitKey(0)
#cv.destroyAllWindows                     #image will disappear when any key pressed

