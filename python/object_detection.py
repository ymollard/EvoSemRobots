# -*- encoding: UTF-8 -*-
# Get an image from NAO. Display it and save it using PIL.

import numpy as np
import cv2

from naoInit import NaoInit
from naoGestures import NaoGestures
import random


import sys
import time

# Python Image Library
import Image

from naoqi import ALProxy

import Image

class Position(object):
    """docstring for Direction"""
    def __init__(self, name, id, vertical, horizontal):
        super(Direction, self).__init__()
        self.name = name
        self.id = id
        self.vertical = vertical
        self.horizontal = horizontal

def detect_position(x, y, image):
    vertical_center = 240

    left_limit = 220
    right_limit = 420

    vertical = "up"
    if y > vertical_center:
        vertical = "down"

    horizontal = "left"
    if x < left_limit:
        horizontal = "left"
    elif x > right_limit:
        horizontal = "right"

    return (horizontal, vertical)

def get_average_color_of_circle((x, y), n, image):
#     """ Returns a 3-tuple containing the RGB value of the average color of the
#     given circle bounded area of radius = n whose center
#     is (x, y) in the given image"""

    width, height, _ = image.shape

    print (x, y), n
    r, g, b = 0, 0, 0
    count = 0
    for s in range(x - n, x + n + 1):
        for t in range(y - n, y + n + 1):
            if ((s- x)**2 + (t- y)**2 <= n**2):
                if s < height - 1 and s > 1  and t < width - 1 and t > 1:
                    pixlr, pixlg, pixlb = image[t, s]
                    r += pixlr
                    g += pixlg
                    b += pixlb
                    count += 1

    if count == 0:
        count = 1

    print ((r/count), (g/count), (b/count)), count
    return ((r/count), (g/count), (b/count))


def save_nao_image(IP, PORT, file):
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
    im.save(file, "PNG")


def detect_circle(IP, PORT, file, output):
    img = cv2.imread(file,0)
    img = cv2.medianBlur(img,5)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                                param1=50,param2=30,minRadius=0,maxRadius=0)

    img2 = cv2.imread(file)

    naoGestures = NaoGestures()

    is_recognized = False
    if circles is not None:
        is_recognized = True
        print circles

        circles = np.uint16(np.around(circles))
        # for i in circles[0,:]:
        #     color = get_average_color_of_circle((i[0],i[1]),i[2], img2)
        #     horizontal, _ = detect_position(i[0], i[1], img2)
        #     # print position
        #     print "color", color

        #     naoGestures.doGesture(horizontal)
        #     # ---
        #     # say that recognized
        #     # say_text(color, IP, PORT)
        #     # say_text(position, IP, PORT)
        #     # end
        #     # ----

        #     # draw the outer circle
        #     cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        #     # draw the center of the circle
        #     cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)


        #     cv2.circle(img2,(i[0],i[1]),i[2],color, -1)

        circle = random.choice(circles[0])

        print circle

        color = get_average_color_of_circle((circle[0],circle[1]),circle[2], img2)
        horizontal, _ = detect_position(circle[0], circle[1], img2)
        # print position
        print "color", color

        naoGestures.doGesture(horizontal)
        cv2.circle(img2,(circle[0],circle[1]),circle[2],color, -1)

        print len(circles)
    else:
        cv2.imwrite(output, cimg)
        

    cv2.imwrite(output, img2)
    # cv2.imwrite(output, cimg)

    print [color, horizontal]

    return [color, horizontal]


def detect_objects_from_nao():
    IP = "192.168.1.104"  # Replace here with your NaoQi's IP address.
    PORT = 9559

    # Read IP address from first argument if any.
    if len(sys.argv) > 1:
        IP = sys.argv[1]

    naoInit = NaoInit()
    naoInit.initPosition()

    file = "test.png"
    output = "test_result.png"


    # save_nao_image(IP, PORT, file)

    circle = detect_circle(IP, PORT, file, output)

    # if is_recognized:
    #     print 'a'
    #     # say_text("recognized blue object", IP, PORT)
    # else:
    #     print 'b'
    #     say_text("not recognized", IP, PORT)

    # time.sleep(2.0 - ((time.time() - starttime) % 2.0))

    return circle

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


def say_text(text, IP, PORT):
    tts = ALProxy("ALTextToSpeech", IP, PORT)
    tts.say(text)

class Color(object):
    """docstring for Color"""
    def __init__(self, lowH, lowS, lowV, upH, upS, upV, name):
        super(Color, self).__init__()
        self.lowH = lowH
        self.lowS = lowS
        self.lowV = lowV
        self.upH = upH
        self.upS = upS
        self.upV = upV
        self.name = name


if __name__ == '__main__':
    # IP = "192.168.1.104"  # Replace here with your NaoQi's IP address.
    # PORT = 9559

    # # Read IP address from first argument if any.
    # if len(sys.argv) > 1:
    #     IP = sys.argv[1]

    # naoInit = NaoInit()
    # naoInit.initPosition()

    # naoGestures = NaoGestures()

    # file = "test.png"
    # output = "test_result.png"

    # starttime = time.time()
    # x = 0
    # # while True:
    # while x < 1:
    #     x += 1
    #     save_nao_image(IP, PORT, file)

    #     is_recognized = detect_circles(IP, PORT, file, output)

    #     if is_recognized:
    #         print 'a'
    #         # say_text("recognized blue object", IP, PORT)
    #     else:
    #         print 'b'
    #         say_text("not recognized", IP, PORT)

    #     time.sleep(2.0 - ((time.time() - starttime) % 2.0))

    detect_objects_from_nao()