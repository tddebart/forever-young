from RobotArm import RobotArm

ro = RobotArm('exercise 7')

for x in range(5):
    for y in range(6):
        ro.moveRight()
        ro.grab()
        ro.moveLeft()
        ro.drop()
    ro.moveRight()
    ro.moveRight()


ro.wait()