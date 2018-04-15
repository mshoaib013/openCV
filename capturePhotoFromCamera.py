import cv2
import time
# Camera 0 is the integrated web cam on my netbook
camera_port = 0 
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)
 
# Captures a single image from the camera and returns it in PIL format
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = camera.read()
 return im
 
# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in range(0,5):
	temp = get_image()
	a=time.strftime("%Y%m%d%H%M%S")
	a +=str(i)
	print (a)
	camera_capture = get_image()
	cv2.imwrite(a+'tan.png', camera_capture)

# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
del(camera)