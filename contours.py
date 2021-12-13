import cv2 as cv
import numpy as np


img = cv.imread('Photos/dbz.jpg')

cv.imshow('Dbz', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
# # returns 10271 contours
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)
# # When using  blur the contours went down from 10271 to 2805
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)
# works with lines 10-17
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# uses the thresh variable
contours, hierarchies = cv.findContours(blur, cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# retr list gets all the contours in the image retr external only find the outside contours.retr tree returns all the 
# hierarchical contours.
# chain_approx_None returns all the contours
# CHAIN_APPROX_SIMPLE takesall the points and gives you the information regarding the beginning and end points.
print(f'{len(contours)} contour(s) located')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)