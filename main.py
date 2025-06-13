import cv2 as cv

Orig_img=cv.imread('messi.jpg')

cv.imshow('image',Orig_img)
flipped_img=cv.flip(Orig_img,1) #1 is for horizontal flip
flipped_img2=cv.flip(Orig_img,0) #0 is for vertical flip
flipped_img3=cv.flip(Orig_img,-1) #-1 is for both horizontal and vertical flip
cv.imshow('flipped_img',flipped_img)
cv.imshow('flipped_img2',flipped_img2)
cv.imshow('flipped_img3',flipped_img3)
cv.waitKey(0)
cv.destroyAllWindows()




