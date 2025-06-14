import cv2 as cv  # Import OpenCV and use alias 'cv'

# Open the default webcam (0 is usually the built-in webcam)
cap = cv.VideoCapture(0)

# Loop to continuously capture frames from the webcam
while True:
    # Read a single frame from the webcam
    ret, frame = cap.read()
    
    # If frame is not read correctly, print an error and exit the loop
    if not ret:
        print("Error: Could not read frame")
        break

    # Display the captured frame in a window titled 'video'
    cv.imshow('video', frame)

    # Wait for 1 ms and check if 'q' key is pressed to exit the loop
    if cv.waitKey(1) == ord('q'):
        break

# Close all OpenCV windows
cv.destroyAllWindows()

# Release the webcam resource
cap.release()
