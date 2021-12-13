import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')

cv.imshow('Park', img)

# Translation: essentially shifting an image along the x and y axis so up down left right or any combo 
# if you use negative values for x you move left negative y values moves up
# -x --> left
# -y --> up
# x --> right
# y -->down
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(img, -90)
cv.imshow('Rotated_Rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (250,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping an image, passing a 1 creates a mirror image(horizontal flip)
flip = cv.flip(img, 1)
cv.imshow('Flip', flip)

# cropping
cropped = img[50:150,10:250]
cv.imshow('Cropped', cropped)



cv.waitKey(0)