# -*- coding: utf-8 -*-
from naoqi import ALProxy

managerProxy = ALProxy("ALBehaviorManager", "192.168.1.109", 9559)
print managerProxy.getInstalledBehaviors()
# managerProxy.runBehavior("basicbehaviors-ed8454/Stand Up")
# managerProxy.runBehavior("animations/Stand/Waiting/LookHand_1")

#leds = ALProxy("ALLeds", "192.168.1.109", 9559)
#leds.off("FaceLeds")
