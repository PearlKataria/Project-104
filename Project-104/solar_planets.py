import cv2

img=cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(10,220),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,0,0))
cv2.putText(img, "Mercury",(110,240),fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5,color=(200,162,200) )
cv2.putText(img,"Venus",(190,170),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(200,200,81))
cv2.putText(img,"Earth",(280,260),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(191,228,118))
cv2.putText(img,"Mars",(380,170),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(251,182,205))
cv2.putText(img,"Jupiter",(560,390),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(193,179,215))
cv2.putText(img,"Saturn",(770,130),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(191,213,232))
cv2.putText(img,"Uranus",(970,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(254,235,201))
cv2.putText(img,"Neptune",(1100,140),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(240,128,128))
cv2.imshow("Display Image",img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)