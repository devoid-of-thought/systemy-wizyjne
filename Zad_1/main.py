import cv2

image = cv2.imread('./pawian Mariusz.jpg')


cv2.circle(image, (240, 170), 40, (0, 0, 255), 2)
cv2.circle(image, (380, 170), 40, (0, 0, 255), 2)

cv2.rectangle(image, (10, 10), (530, 650), (0, 255, 0), 2)

cv2.ellipse(image, (300, 475), (30, 15), 35, 0, 360, (0, 255, 255), 2)
cv2.ellipse(image, (368, 470), (30, 15), -35, 0, 360, (0, 255, 255), 2)

cv2.imwrite('./pawian Mariusz - zakształcony.jpg', image)