import cv2

# Bright image
def brightness_(img, beta_value):
    img_b = cv2.convertScaleAbs(img, beta=beta_value)
    return img_b

img = cv2.imread("images/demogg.jpeg")
scale = brightness_(img, 70)
cv2.imwrite("img_result/scaled_image.jpg", scale)

# Dark image
def darkness_(img, beta_value):
    img_c = cv2.convertScaleAbs(img, beta=beta_value)
    return img_c

img = cv2.imread("images/demogg.jpeg")
scale = darkness_(img, -70)
cv2.imwrite("img_result/dark_scaled.jpg", scale)


