import cv2

source = "img.png"
destination = "newimg.jpeg"
#percent by which the image is resized
scale_percent = 50


src_img= cv2.imread(source)
# cv2.imshow('Displaying Images', image)
# cv2.waitKey(0)


#calculate the 50 percent of the original dimensions
new_width = int(src_img.shape[1] * scale_percent/100)
new_height = int(src_img.shape[0] * scale_percent/100)

#resize image
output = cv2.resize(src_img, (new_width, new_height))

cv2.imwrite(destination, output)
cv2.waitKey(0)