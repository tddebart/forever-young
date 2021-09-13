#11 REGELS
from RobotArm import RobotArm

ro = RobotArm('exercise 10')
ro.speed = 3

for x in range(5):
    ro.grab()
    for y in range(9-2*x):
        ro.moveRight()
    ro.drop()
    for y in range(9-2*x):
        ro.moveLeft()
    ro.moveRight()

ro.wait()
