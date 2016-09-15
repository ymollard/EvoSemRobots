#!/usr/bin/env python
from naoqi import ALProxy


class NaoInit():
    def __init__(self):
        # Get the Nao's IP and port
        ipAdd = None
        port = None
        try:
            ipFile = open("ip.txt")
            lines = ipFile.read().replace("\r", "").split("\n")
            ipAdd = lines[0]
            port = int(lines[1])
        except Exception as e:
            print "Could not open file ip.txt"
            ipAdd = raw_input("Please write Nao's IP address... ")
            port = raw_input("Please write Nao's port... ")

        # Init proxies.
        try:
            self.motionProxy = ALProxy("ALMotion", ipAdd, port)
        except Exception, e:
            print "Could not create proxy to ALMotion"
            print "Error was: ", e

        try:
            self.postureProxy = ALProxy("ALRobotPosture", ipAdd, port)
        except Exception, e:
            print "Could not create proxy to ALRobotPosture"
            print "Error was: ", e

    def initPosition(self):
        self.StiffnessOn(self.motionProxy)
        self.postureProxy.goToPosture("Crouch", 0.9)
        self.motionProxy.changeAngles("HeadPitch", 0.5, 0.1)

    def StiffnessOn(self, proxy):
        # We use the "Body" name to signify the collection of all joints
        pNames = "Body"
        pStiffnessLists = 1.0
        pTimeLists = 1.0
        proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


if __name__ == "__main__":
    naoInit = NaoInit()
    naoInit.initPosition()
