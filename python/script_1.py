# -*- encoding: UTF-8 -*-
# Get an image from NAO. Display it and save it using PIL.

import numpy as np
import cv2

import sys
import time

# Python Image Library
import Image

from naoqi import ALProxy


def showNaoImage(IP, PORT):
    """
    First get an image from Nao, then save it on disc.
    """

    camProxy = ALProxy("ALVideoDevice", IP, PORT)
    resolution = 2    # VGA
    colorSpace = 11   # RGB

    videoClient = camProxy.subscribe(
        "python_client", resolution, colorSpace, 5)

    t0 = time.time()

    # Get a camera image.
    # image[6] contains the image data passed as an array of ASCII chars.
    naoImage = camProxy.getImageRemote(videoClient)

    t1 = time.time()

    # Time the image transfer.
    print "acquisition delay ", t1 - t0

    # print naoImage

    camProxy.unsubscribe(videoClient)

    # Now we work with the image returned and save it as a PNG  using ImageDraw
    # package.

    # Get the image size and pixel array.
    imageWidth = naoImage[0]
    imageHeight = naoImage[1]
    array = naoImage[6]

    # Create a PIL Image from our pixel array.
    im = Image.frombytes("RGB", (imageWidth, imageHeight), array)

    # Save the image.
    im.save("camImage.png", "PNG")


def recognizeBall():
    img = cv2.imread("camImage.png",0)
    img = cv2.medianBlur(img,5)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                                param1=50,param2=30,minRadius=0,maxRadius=100)

    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    cv2.imwrite("proImage.png", cimg)


    is_recognized = False
    if len(circles) > 1:
        is_recognized = True

        print len(circles)

    return is_recognized


def recognizeYellowRectangle():
    image = cv2.imread("camImage.png")

    # image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # blue hsv
    # upper = np.array([100,50,50])
    # lower = np.array([150,255,255])


    # # blue
    # upper = np.array([255, 100, 100])
    # lower = np.array([150, 60, 60])

    # pink
    # upper = np.array([255,222,243])
    # lower = np.array([20,130,150])

    # yellow
    # upper = np.array([255, 255, 100])
    # lower = np.array([170, 170, 0])

    # mask = cv2.inRange(image, lower, upper)

    # find contours in the masked image and keep the largest one
    # find the blue color game in the image
    upper = np.array([255, 100, 100])
    lower = np.array([150, 0, 0])
    mask = cv2.inRange(image, lower, upper)

    # find contours in the masked image and keep the largest one
    (_, cnts, _) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
    # res = cv2.bitwise_and(frame,frame, mask= mask)

    # kernel = np.ones((5, 5), np.uint8)




    for c in cnts:
            
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.05 * peri, True)

        # draw a red bounding box surrounding the object
        cv2.drawContours(image, [approx], -1, (0, 0, 255), 4)


    is_recognized = False
    if cnts:
        c = max(cnts, key=cv2.contourArea)

        print c
        print len(c)
        # approximate the contour


    cv2.imwrite("proImage.png", image)
    # cv2.imwrite("resImage.png", res)

    return is_recognized


def sayText(text, IP, PORT):
    tts = ALProxy("ALTextToSpeech", IP, PORT)
    tts.say(text)


if __name__ == '__main__':
    IP = "192.168.1.104"  # Replace here with your NaoQi's IP address.
    PORT = 9559

    # Read IP address from first argument if any.
    if len(sys.argv) > 1:
        IP = sys.argv[1]

    starttime = time.time()
    x = 0
    # while True:
    while x < 5:
        x += 1
        showNaoImage(IP, PORT)

        is_recognized = recognizeYellowRectangle()
        # is_recognized = recognizeBall()

        if is_recognized:
            print 'a'
            sayText("recognized blue object", IP, PORT)
        else:
            print 'b'
            # sayText("not recognized", IP, PORT)

        time.sleep(2.0 - ((time.time() - starttime) % 2.0))
