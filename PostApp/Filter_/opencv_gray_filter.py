import cv2
img = cv2.imread("images/images.jpeg")
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', grayscale)
cv2.waitKey(0)


