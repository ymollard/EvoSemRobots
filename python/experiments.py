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


# TEACHER ROBOT

# p_name: <name, name>


class Teacher(object):

    def __init__(self, c_name, p_name):
        self.ns = NaoSpeak()
        self.c_name = c_name
        self.p_name = p_name

    def nameObject(self,c_detected, p_detected):

        color = self.c_name[colorIndex(c_detected)]

        if p_detected == 'left':
            position = self.p_name[0]
        elif p_detected == 'center':
            position = self.p_name[1]
        else:
            position = self.p_name[2]

        return [color, position]

    def step(self):

        detected = detect_objects_from_nao()

        if not detected:
            self.ns.say("not recognized")
        else:
            c_detected = detected[0]
            p_detected = detected[1]

            name = self.nameObject(c_detected, p_detected)
            self.ns.say(name[0])
            self.ns.say(name[1])


class Learner(object):

    def __init__(self):
        self.ns = NaoSpeak()
        self.names = [['red', 'blue', 'green'], [
            'red', 'blue', 'green'], ['red', 'blue', 'green']]


    def nameColor(self, detected):
        return random.choice(self.names[colorIndex(detected)])


    def reinforce(self, detected, chosen, answer):

        c_index = colorIndex(detected)

        if answer:
            self.names[c_index] = [chosen]
            for index in [i for i in [0,1,2] if not i==c_index]:
                self.names[index].remove(chosen)
        else:
            self.names[c_index].remove(chosen)


    def step(self):

        detected = detect_objects(img)
        
        if not detected:
            self.ns.say("not recognized")
        else:
            choice = self.nameColor(c_detected)
            ans = raw_input()

            if ans == 'yes':
                answer = 1
            else:
                answer = 0

            self.reinforce(c_detected, chosen, answer)


# LEARNER EXPERIMENT
# if __name__ == '__main__':
#   c_name = ['red', 'green', 'blue']
#   p_name = ['left', 'right']

#   learner = Learner(c_name, p_name)

#   for i in [1,2,3,4,5]:
#       learner.step()
#       time.sleep(5)


# TEACHER EXPERIMENT
if __name__ == '__main__':
    c_name = ['azurro','verde', 'rosso']
    p_name = ['sinistra', 'centro', 'distra']

    random.seed()

    teacher = Teacher(c_name, p_name)

    for i in [1, 2, 3, 4, 5]:
        teacher.step()
        time.sleep(3)
