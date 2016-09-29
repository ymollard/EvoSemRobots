# -*- encoding: UTF-8 -*-

# This is just an example script that shows how images can be accessed
# through ALVideoDevice in python.
# Nothing interesting is done with the images in this example.

from naoqi import ALProxy
import vision_definitions
import time

ipFile = open("ip.txt")
lines = ipFile.read().replace("\r", "").split("\n")
IP = lines[0]
PORT = int(lines[1])

####
# Create proxy on ALVideoDevice

print "Creating ALVideoDevice proxy to ", IP

camProxy = ALProxy("ALVideoDevice", IP, PORT)

####
# Register a Generic Video Module

resolution = vision_definitions.kQVGA
colorSpace = vision_definitions.kYUVColorSpace
fps = 30

nameId = camProxy.subscribe("python_GVM", resolution, colorSpace, fps)
print nameId

#print 'getting images in local'
#for i in range(0, 20):
#  camProxy.getImageLocal(nameId)
#  camProxy.releaseImage(nameId)

resolution = vision_definitions.kQQVGA
camProxy.setResolution(nameId, resolution)

print 'getting images in remote'
for i in range(0, 20):
  t0 = time.time()
  camProxy.getImageRemote(nameId)
  t1 = time.time()
  print "acquisition delay ", t1 - t0

camProxy.unsubscribe(nameId)

print 'end of gvm_getImageLocal python script'