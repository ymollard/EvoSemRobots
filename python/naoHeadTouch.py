# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
import time


class NaoHeadTouch(object):

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

        # Set memoryproxy
        try:
            self.memoryProxy = ALProxy("ALMemory", ipAdd, port)
        except Exception as e:
            print "Could not create proxy to ALMotion"
            print "Error was: ", e

    def wait_for_headtouch(self, delay=0.5):
        while self.memoryProxy.getData("Device/SubDeviceList/Head/Touch/Middle/Sensor/Value") < 0.5:
            time.sleep(delay)

    def headYesOrNo(self, delay=0.5):
        while True:
            if self.memoryProxy.getData("Device/SubDeviceList/Head/Touch/Front/Sensor/Value") > 0.5:
                return 1
            elif self.memoryProxy.getData("Device/SubDeviceList/Head/Touch/Rear/Sensor/Value") > 0.5:
                return 0
            time.sleep(delay)
