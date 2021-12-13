import cv2 as cv
img = cv.imread('Photos/dbz.jpg')
cv.imshow('Dbz', img)

def rescaleFrame(frame, scale=0.5):
    # images, videos and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
resized_image = rescaleFrame(img)
cv.imshow('image', resized_image)


# def changeRes(width, height):
#     # only works with live video does not work with stored or existing video files.
#     capture.set(3,width)
#     capture.set(4,height)


# Videos:
capture = cv.VideoCapture('Videos/carvid.mp4')
# if using webcam or live camera connected to pc you would use an integer such as 0 , 1
# in most cases a webcam is referenced as 0 and 1 would reference the first camera connected to the computer etc.
# in reading a video we use a while loop to loop through each frame.
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale =.2)
# can use (frame, scale=.2) or any (.numnber) to change the size of the second screen
    cv.imshow('Video', frame)

    cv.imshow('Videos Resized', frame_resized)
# in line 16 i pass the video with parameter of frames. so I can loop in each frame and view them seperately and read individually.
# using the capture.read method on line 15. I display each frame using the cv.imshow methos on line 16. and I break out of the loop
# I used a waitkey and if the letter d is pressed we break out and stop displaying. finally we realease the captured device and destory the windows created.
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()   

cv.waitKey(0)