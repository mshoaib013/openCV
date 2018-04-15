import cv2
img = cv2.imread("a.png")
crop_img = img[0:250, 0:50]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
