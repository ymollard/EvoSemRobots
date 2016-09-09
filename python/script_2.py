from naoqi import ALProxy


def walk_and_speak(IP, PORT):
    motion = ALProxy("ALMotion", IP, PORT)
    tts = ALProxy("ALTextToSpeech", IP, PORT)
    motion.moveInit()
    motion.post.moveTo(-0.1, 0, 0)
    # tts.say("I'm walking")


if __name__ == '__main__':
    IP = "192.168.1.104"  # Replace here with your NaoQi's IP address.
    PORT = 9559

    walk_and_speak(IP, PORT)
