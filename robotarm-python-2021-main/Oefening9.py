from RobotArm import RobotArm

ro = RobotArm('exercise 9')

for x in range(4):
    for l in range(4):
        ro.grab()
        for y in range(5):
            ro.moveRight()
        ro.drop()
        for y in range(5):
            ro.moveLeft()
    ro.moveRight()

ro.wait()
