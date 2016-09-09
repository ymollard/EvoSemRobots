from experiments import Teacher
from naoGestures import NaoGestures

if __name__ == '__main__':
    c_name = ['red', 'green', 'blue']
    p_name = ['left', 'right']

    teacher = Teacher(c_name, p_name)

    for i in [1,2,3,4,5]:
        teacher.step()
        time.sleep(5)
