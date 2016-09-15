# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
import time

IP = "192.168.1.104"
PORT = 9559


class Head(object):

    def __init__(self, IP=IP, PORT=PORT):
        self.memoryProxy = ALProxy("ALMemory", IP, PORT)

    def wait_for_headtouch(self, delay=0.5):
        while self.memoryProxy.getData("Device/SubDeviceList/Head/Touch/Middle/Sensor/Value") < 0.5:
            time.sleep(delay)

    def head_yesorno(self, delay=0.5):
        while True:
            if self.memoryProxy.getData("Device/SubDeviceList/Head/Touch/Front/Sensor/Value") > 0.5:
                return 1
            elif self.memoryProxy.getData("Device/SubDeviceList/Head/Touch/Rear/Sensor/Value") > 0.5:
                return 0
            time.sleep(delay)
