import colorsys
from object_detection import detect_objects_from_nao
from naoSpeak import NaoSpeak
import time
import random

# names: ['red', 'blue', 'green']
# names starts being [['red', 'blue', 'green'], ['red', 'blue', 'green'],
# ['red', 'blue', 'green']]

# color-names: (name, name, name)


def colorIndex(detected):

    # detected: (float, float, float)
    return detected.index(max(detected))


def nameColor(detected, names):

    return random.choice(names[colorIndex(detected)])

# colorsys.hsv_to_rgb(x)


def reinforce(detected, chosen, answer, names):

    c_index = colorIndex(detected)

    if answer:
        names[c_index] = [chosen]
    else:
        names[c_index].remove(chosen)

    return names


# TEACHER ROBOT

# p_name: <name, name>

def nameObject(c_detected, p_detected, c_name, p_name):

    color = c_name[colorIndex(c_detected)]

    if p_detected == 'left':
        position = p_name[0]
    else:
        position = p_name[1]

    return random.choice([color, position])


class Teacher(object):

    def __init__(self, c_name, p_name):
        self.ns = NaoSpeak()
        self.c_name = c_name
        self.p_name = p_name

    def step(self):

        detected = detect_objects_from_nao()

        if not detected:
            self.ns.say("not recognized")
        else:
            c_detected = detected[0]
            p_detected = detected[1]

            name = nameObject(c_detected, p_detected, self.c_name, self.p_name)
            self.ns.say(name)

# to teach, create a teacher:
    # teacher = Teacher(c_name, p_name)
# and teach as many times as waned:
    # teacher.step()


# class Learner(object):

# 	def __init__(self, ):
# 		self.ns = NaoSpeak()
# 		self.c_name = c_name

# 	def step(self):

# 		detected = detect_objects(img)

# 		c_detected = detected[0][0]
# 		p_detected = detected[0][1]

# 		name = nameObject(c_detected, p_detected, self.c_name, self.p_name)
# 		self.ns.say(name)


if __name__ == '__main__':
    c_name = ['red', 'green', 'blue']
    p_name = ['left', 'right']

    random.seed()

    teacher = Teacher(c_name, p_name)

    for i in [1, 2, 3, 4, 5]:
        teacher.step()
        time.sleep(5)
