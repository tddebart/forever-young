from RobotArm import RobotArm

ro = RobotArm('exercise 3')
ro.speed = 3

for x in range(4):
    ro.grab()
    ro.moveRight()
    ro.drop()
    ro.moveLeft()

ro.wait()