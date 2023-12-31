# raspysculpt

RaspberryPy servo based kinetic sculpture project.

This repo is to hold the code related to Task 2 - experiment with servo and rasperrypi controller and code

## Task 2 Notes

Normal servos do 90 only (180 with gears)
Can buy continuos 360 servos ie like normal motor (less precise fixed positions)
Pi has 26 GPIOs so can run that many servers directly (or add controller boards or Pis!)

Various Python libs to run this - so easiest solution is get a Pi or two and some 360s plus maybe a few standard servos?

Gearing and various plug on mechanics can turn servo motion into linear up / down etc.

https://www.digikey.co.uk/en/maker/tutorials/2021/how-to-control-servo-motors-with-a-raspberry-pi

Bought Pi and 2 servos for testing out.

Also may want to get distance sensors (only £4) https://thepihut.com/products/dexter-grovepi-and-gopigo-ultrasonic-sensor

See https://gpiozero.readthedocs.io/en/latest/recipes.html

With 4 we could feed distances into controlling kinetics - theremin style, eg. turn flower towards viewer

Note that servos can be strong enough to open doors etc. - expensive if high torque, but the weight of ceramic is no limitation - although MVP design would be cheaper / easier with card, wood, plastic or other lightweight materials instead.

There are simulators to test out basics of the program https://wokwi.com/projects/new/micropython-pi-pico

## Wokwi simulator code

Currently this repository just holds the simulator code for running servos

MVP experimental code for various kinetic actions.

1. opening / closing petal part of sculpture
