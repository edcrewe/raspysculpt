# modules
from picozero import Servo  # importing Servo class to easily control the servo motor
from time import sleep

# creating a Servo object
servos = [Servo(1), Servo(2), Servo(3), Servo(4), Servo(5), Servo(6)]
angles = [0, 0.2, 0.4, 0.6, 0.8, 1]
clockwise = [True, True, True, True, True, True]
step = 0.05

# continuously swing the servo arm to min, mid, and max positions (for a duration of 1 sec each)
while True:
    # swinging the servo arm to its min position
    for i, servo in enumerate(servos):
        servo.value = angles[i]

    # swinging the servo arm to its mid position
    for i, servo in enumerate(servos):
        if clockwise[i]:
            angles[i] = angles[i] + 0.05
        else:
            angles[i] = angles[i] - 0.05           
        if angles[i] > 1.5 or angles[i] < -0.5:
            clockwise[i] = not clockwise[i]
        servo.value = angles[i]

    sleep(0.3)
