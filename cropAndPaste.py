import cv2
import numpy as np

img = cv2.imread('201804160304301tan.png',cv2.IMREAD_COLOR)
#px = img[0,0]
#img [hight 0 to 150 (virtical) ,  width 100 to 150 (horizontal)]
img[0:150,100:150] = [255,255,255]
print(img.shape)
print(img.size)
print(img.dtype)


watch_face = img[50:350,367:567]#copy image poertion to variable
img[0:300,0:200] = watch_face #paste copied image in this portion

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()