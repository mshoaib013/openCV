import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('t.jpg',-1)#0 for gray style
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('Tanvir',img)#1st tamvir is windowl title

# cv2.waitKey(0)
k = cv2.waitKey(0)
if k == 27:
	cv2.destroyAllWindows()
if k == ord('s'):
	cv2.imwrite('tan.png',img)
	
