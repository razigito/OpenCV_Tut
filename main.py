import cv2 as cv
import matplotlib.pyplot as plt
# img = plt.imread('messi.jpg')

# plt.imshow(img)
# plt.show()

img = cv.imread('messi.jpg')      # Read the image
cropped = img[10:168, 100:250]   # Crop: [y1:y2, x1:x2]
cv.imshow("Original", img)
cv.imshow("Cropped", cropped)     # Show cropped part
cv.waitKey(0)
cv.destroyAllWindows()
