import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
# img = cv2.line(img,(0,0),(511,511),(255,0,0),5)#drawline
# img = cv2.rectangle(img,(384,0),(510,128),(255,255,0),7)#draw rectangle
# img = cv2.circle(img,(447,63), 63, (0,0,255), -1)#draw circle
# img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
#***********************draw
pts = np.array([[10,5],[20,30],[70,20],[50,10],[10,5],[150,255]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],False,(0,255,255))

#Text on image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(0,200), font, 4,(255,255,255),2,cv2.LINE_AA)
#*******************************
cv2.imwrite('tan.png',img)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow("Test",img)



# cv2.waitKey(0)
k = cv2.waitKey(0)
if k == 27:
	cv2.destroyAllWindows()
if k == ord('s'):
	cv2.destroyAllWindows()