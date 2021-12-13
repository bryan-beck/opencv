import cv2 as cv
import numpy as np

# blank image to work with drawing or adding text to
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)
# 1: paint image with a unique color
# blank[:] references all the pixels
# you can select a range of puxels and modify only those as well as all the pixels
# i.e. blank[200:300]

blank[0:500, 245:255] = 0,255,0
cv.imshow('Aqua', blank)

# 2:draw a rectangle on the blank image
# thickness=2 on line 17 sets the lines thickness and can be set to cv.filled or "-1" to fill the rectangle with color.
cv.rectangle(blank, (5,100), (500,250), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)
# instead of using fixed values like (500,250) we can use
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)
# this created a shape with half the dimensions as the original image


# 3. Draw a circle on the blank image
cv.circle(blank, (250,250), 40, (0,0,255),thickness=-1)
cv.imshow('Circle', blank)

# 4: Draw a line on the blank image

cv.line(blank, (300,450), (300,375), (255,255,255), thickness=3)
cv.imshow('Line', blank)
# creates a line that starts at (300,450) which reference the starting point and end points.


# 5: create text on a image

cv.putText(blank, 'Hello Dev Friends', (50,245), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blank)
cv.waitKey(0)