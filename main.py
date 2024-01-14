# modules
 # importing Servo class to easily control the servo motor - picozero same as gpiozero
from picozero import Servo 
from time import sleep

# creating a Servo object
servos = [Servo(1), Servo(2), Servo(3), Servo(4), Servo(5), Servo(6)]
angles = [0, 1, 0, 1, 0, 1]


for x in range(0, 20):
    plusminus = [1, -1, 1, -1, 1, -1]
    for i, servo in enumerate(servos):
        servo.value = angles[i]

    # swinging the servo arm to its mid position
    for i, servo in enumerate(servos):
        angles[i] = angles[i] + (0.2 * plusminus[i])
        if angles[i] > 1:
            angles[i] = 0
            plusminus[i] = -1
        if angles[i] < 0:
            angles[i] = 1
            plusminus[i] = 1
        servo.value = angles[i]

    sleep(0.5)


for x in range(0, 3):
    for x in range(0, 5):
        servos[x].min()
        servos[x + 1].max()
        sleep(1)
        servos[x].mid()
        servos[x + 1].mid()
        sleep(1)
        servos[x].max()
        servos[x + 1].min()


for x in range(0, 20):
    angles = [0, 0.2, 0.4, 0.6, 0.8, 1]

    # swinging the servo arm to its min position
    for i, servo in enumerate(servos):
        servo.value = angles[i]

    # ticking the servos around at same rate
    for i, servo in enumerate(servos):
        angles[i] = angles[i] + 0.05
        if angles[i] > 1:
            angles[i] = 0
        servo.value = angles[i]

    sleep(0.3)
