#This Code Basically Converts Orginal Img To An Pencil / Sketch Img
import cv2
image = cv2.imread('Sample.jpg')
grayImg = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invertedimg = 225 - grayImg
blurred = cv2.GaussianBlur(invertedimg, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(grayImg, inverted_blurred, scale=256.0)
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch of Sample Img", pencil_sketch)
cv2.waitKey(0)