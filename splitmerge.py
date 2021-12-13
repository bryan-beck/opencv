import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)
# sets the color components not selected in the code line to black so only the color selected will appear
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
# the darker the saturation the less the color space selected the lighter the saturation the more like 
# the color chosen. i.e. in the blue output image the lightest section is the sky where the most blue 
# is located and the darkest is the tree area where little or no blue is located.
# the reason output images are coming as grayscale is because the shape of grayscale img is 1
merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)