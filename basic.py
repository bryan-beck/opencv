import cv2 as cv

img = cv.imread('Photos/park.jpg')

cv.imshow('Park', img)

# Converting to grayscale from BGR
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# Blur modification used to enhance or fix defects in  an image as an example of one use.
# increase the blur effect by increasing the kernal size. (7,7) is much more blurry than (3,3)
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 255)
cv.imshow('Canny Edges', canny)

# we can also pass in previously modified files such as "blur" and this can hide some of the finer details in the canny edge image


# canny = cv.Canny(blur, 125, 255)
# cv.imshow('Canny', canny)


# dilating the images
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding: used to restore an image after, for example, dilation.
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize, when you set the dsize it ignores the aspect ratio, interpolation is helpful when shrinking down 
# to a size smaller than original dimensions, when resizing to larger than the original dimensions you would benefit 
# from cv.INTER_CUBIC or cv.INTER_LINEAR, cubic is the slowest but best image quality
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# cropping: crop an image using array slicing
cropped = img[60:150, 100:200]
cv.imshow('Cropped', cropped)



cv.waitKey(0)


