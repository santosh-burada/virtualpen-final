import virtualpen  #provides the virtual paint to have you must have cv2,numpy in your sysytem
import cv2

framewidth = 2000

frameheight = 2000

cap = cv2.VideoCapture(0)  #this line access the webcam
cap.set(3, framewidth)  #adjusting the height and wifth of output window
cap.set(4, frameheight)
cap.set(10, 100)  # This line Adjust the Brightness



myColors = [[57,56,0,100,255,255]]  #hsv lower and upper values h_min, h_max, s_min, s_max, v_min, v_max.
myValues = [ [0,255,0]]  #bgr values
myPoints = []

while True :

    success, img = cap.read()
    imgresult = virtualpen.copyimage(img)  #gives copy of the image
    newPoints = virtualpen.findcolor(img, myColors, myValues, imgresult)  #detects the color of the your object and detect the center point with colored circle and detects the coordinates of your object in output window
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        virtualpen.drawOnCanvas(myPoints, myValues,imgresult)  #draws the color along the cooordinates.
    cv2.imshow("img", imgresult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
