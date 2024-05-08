import cv2

def hdr_(img):
    hdr_e = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
    return hdr_e

image_name = "images/demogg.jpeg"
image = cv2.imread(image_name)
hdr_img = hdr_(image)
cv2.imwrite("img_result/hdr_image.jpg", hdr_img)
