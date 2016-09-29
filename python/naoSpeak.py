#!/usr/bin/env python
from naoqi import ALProxy


class NaoSpeak():
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
        self.ip = ipAdd
        self.port = port

        # Init proxies.
        try:
            self.ttsProxy = ALProxy("ALTextToSpeech", ipAdd, port)
        except Exception, e:
            print "Could not create proxy to ALTextToSpeech"
            print "Error was: ", e

    def say(self, speech):
        self.ttsProxy.say(speech)


if __name__ == "__main__":
    naoSpeak = NaoSpeak()
    naoSpeak.say("hello!")
