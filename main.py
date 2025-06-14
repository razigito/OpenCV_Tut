import cv2 as cv  
cap = cv.VideoCapture(0) #capture the video from the webcam,
                        #you can change the 0 to the video file name
                        #to capture the video from the video file

while True:
    
    ret, frame = cap.read()
    
    
    if not ret:
        print("Error: Could not read frame")
        break
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #convert the frame to gray
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    cv.putText(frame, 'Razi', (50, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 250), 3)
    cv.imshow('original', frame)    #show the original frame
    cv.imshow('gray',gray_frame)    #show the gray frame
    cv.imshow('hsv', hsv_frame)

    
  
    if cv.waitKey(1) == ord('q'):
        break
# Release the webcam resource
cap.release()
# Close all OpenCV windows
cv.destroyAllWindows()


