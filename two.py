import numpy as np
import cv2

img = cv2.imread('t.jpg',0)
cv2.imshow('aha',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('tanvir.png',img)
    