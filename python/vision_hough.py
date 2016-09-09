# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 04:44:57 2016

@author: spranger
"""

# -*- encoding: UTF-8 -*-
# Get an image from NAO. Display it and save it using PIL.

import sys
import time
import Image
import cv2
import cv2.cv as cv
import numpy

from naoqi import ALProxy
import vision_definitions

# Python Image Library
IP = "192.168.1.109" # Replace here with your NaoQi's IP address.
PORT = 9559

resolution = vision_definitions.kVGA
colorSpace = vision_definitions.kRGBColorSpace
fps = 30

camProxy = ALProxy("ALVideoDevice", IP, PORT)
nameId = camProxy.subscribe("python_GVM", resolution, colorSpace, fps)
print nameId

print 'getting images in remote'
for i in range(1):
    t0 = time.time()
    naoImage = camProxy.getImageRemote(nameId)
    # Get the image size and pixel array.
    imageWidth = naoImage[0]
    imageHeight = naoImage[1]
    array = naoImage[6]
      
    # array_cv = (numpy.reshape(numpy.frombuffer(array[6], dtype = '%iuint8' % array[2]), (array[1], array[0], array[2])))
      
    # Create a PIL Image from our pixel array.
    pil_image = Image.fromstring( "RGB", (imageWidth, imageHeight), array)
    cv_image = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)
    cv2.imshow("window name", cv_image)

    # hough
    img = cv2.medianBlur(cv_image,5)
    circles = cv2.HoughCircles(img,cv.CV_HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

    circles = numpy.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cv_image,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cv_image,(i[0],i[1]),2,(0,0,255),3)

    cv2.imshow('detected circles',cv_image)
    cv2.waitKey(0)
    t1 = time.time()
    print "acquisition delay ", t1 - t0

camProxy.unsubscribe(nameId)
