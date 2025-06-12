import cv2 as cv
import numpy as np

#RESİZE AN IMAGE

img2 = cv.imread('zoo.jpg') 
cv.imshow('original', img2)
print(img2.shape) #(height, width, channel) tuple

#Downscale with aspect ratio

scale_percent = 50 #%50 of the original size
width = int(img2.shape[1] * scale_percent / 100) 
height = int(img2.shape[0] * scale_percent / 100)
dim = (width, height) # dimension ple
resized1 = cv.resize(img2, dim, interpolation = cv.INTER_AREA)
cv.imshow('resized1', resized1) #resized image

print(resized1.shape) 

# #Upscale with aspect ratio
# scale_percent = 150    #%150 of the original size
# width = int(img2.shape[1] * scale_percent / 100) 
# height = int(img2.shape[0] * scale_percent / 100)
# dim = (width, height) 
# resized2 = cv.resize(img2, dim, interpolation = cv.INTER_AREA)
# cv.imshow('resized2', resized2) #resized image

# print(resized2.shape)


# #change width only
# width = int(img2.shape[1])
# height = 150 
# dim = (width, height) 
# resized3 = cv.resize(img2, dim, interpolation = cv.INTER_AREA)
# cv.imshow('resized3', resized3) #resized image

# print(resized3.shape)

# #custom size
# width = 300
# height = 300
# dim = (width, height)
# resized4 = cv.resize(img2, dim, interpolation = cv.INTER_AREA)
# cv.imshow('resized4', resized4) #resized image


cv.waitKey(0)
cv.destroyAllWindows()