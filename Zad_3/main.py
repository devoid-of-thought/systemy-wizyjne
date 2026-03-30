import cv2
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
def show_image(img, title):
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()
img = cv2.imread("0000021_00000671ms_t1_21_v1_27_t2_29_v2_212.jpg",cv2.IMREAD_GRAYSCALE)


cropped_image = img[int(24):int(24+510),
                int(46):int(46+652)]
cv2.imshow("Termowizja", cropped_image)
_, thresh_binary = cv2.threshold(cropped_image, 120, 255, cv2.THRESH_BINARY)
show_image(thresh_binary, 'Propagacja prosta ')

thresh_mean = cv2.adaptiveThreshold(
    cropped_image, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    199, 5
)
show_image(thresh_mean, "Propagacja Adaptacyjna")

otsu_threshold, image_result = cv2.threshold(
    cropped_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,
                   )
show_image(image_result, "Propagacja Otsu")
cv2.waitKey(0)
cv2.destroyAllWindows()