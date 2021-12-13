import cv2 as cv

# make use of cv.imread method
# returns image as a matrix of pixels

# img = cv.imread('Photos/dbz.jpg')
# could provide absolute paths but these files are in the directory.

# reading videos here and lines: 
capture = cv.VideoCapture('Videos/carvid.mp4')
# if using webcam or live camera connected to pc you would use an integer such as 0 , 1
# in most cases a webcam is referenced as 0 and 1 would reference the first camera connected to the computer etc.
# in reading a video we use a while loop to loop through each frame.
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
# in line 16 i pass the video with parameter of frames. so I can loop in each frame and view them seperately and read individually.
# using the capture.read method on line 15. I display each frame using the cv.imshow methos on line 16. and I break out of the loop
# I used a waitkey and if the letter d is pressed we break out and stop displaying. finally we realease the captured device and destory the windows created.
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
   
# cv.imshow('Dbz', img)
# /basically displays the images as a new Window

cv.waitKey(0)
# tells the application to wait indefinitely until a keyboard key is pressed
# when I sun this it currently doesnt allow scrolling and the image is too large.
# the reason for this is that image is greater in size than the monitor currently being used
# resizing and rescaling frames was needed to correct this issue.