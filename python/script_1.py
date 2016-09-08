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
    First get an image from Nao, then show it on the screen with PIL.
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


def recognizeYellowRectangle():
    image = cv2.imread("camImage.png")

    # find the blue color game in the image
    upper = np.array([255, 255, 100])
    lower = np.array([170, 170, 0])
    mask = cv2.inRange(image, lower, upper)

    # find contours in the masked image and keep the largest one
    (_, cnts, _) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)

    print cnts

    if cnts:
        return True
    else:
        return False
    

def sayText(text, IP, PORT):
    tts = ALProxy("ALTextToSpeech", IP, PORT)
    tts.say(text)


if __name__ == '__main__':
    IP = "192.168.1.123"  # Replace here with your NaoQi's IP address.
    PORT = 9559

    # Read IP address from first argument if any.
    if len(sys.argv) > 1:
        IP = sys.argv[1]

    starttime=time.time()
    while True:
        showNaoImage(IP, PORT)

        is_recognized = recognizeYellowRectangle()

        if is_recognized:
            print 'a'
            sayText("recognized yellow", IP, PORT)
        else:
            print 'b'
            sayText("not recognized", IP, PORT)

        time.sleep(1.0 - ((time.time() - starttime) % 1.0))

# import the necessary packages

# from naoqi import ALProxy
# import vision_definitions

# import sys
# import time

# # Python Image Library
# import Image


# IP = "192.168.1.123"
# PORT = 9559

# tts = ALProxy("ALTextToSpeech", IP, PORT)
# tts.say("Hello, world!")

# tts.say("not using choreographe!")

# resolution = vision_definitions.kQVGA
# colorSpace = vision_definitions.kYUVColorSpace
# fps = 5

# videoClient = camProxy.subscribe("python_GVM", resolution, colorSpace, fps)
# print videoClient

# t0 = time.time()

# # Get a camera image.
# # image[6] contains the image data passed as an array of ASCII chars.
# naoImage = camProxy.getImageRemote(videoClient)

# t1 = time.time()

# print "acquisition delay ", t1 - t0

# camProxy.unsubscribe(videoClient)

# imageWidth = naoImage[0]
# imageHeight = naoImage[1]
# array = naoImage[6]

# # Create a PIL Image from our pixel array.
# im = Image.fromstring("RGB", (imageWidth, imageHeight), array)

# # Save the image.
# im.save("camImage.png", "PNG")
