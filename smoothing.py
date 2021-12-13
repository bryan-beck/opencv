import cv2 as cv

img = cv.imread('Photos/dbz.jpg')
cv.imshow('Dbz', img)

# Averaging:takes the average of the blur effect from the surrounding pixels
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# median blur: find the median of the surrounding
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral blurring is the most effective because it applies blur to the image but retains the edges in the image
bilateral = cv.bilateralFilter(img, 15, 15, 30)
cv.imshow('Bilateral Blur', bilateral)



cv.waitKey(0)
