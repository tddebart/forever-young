from RobotArm import RobotArm

ro = RobotArm('exercise 8')

ro.moveRight()
for x in range(7):
    ro.grab()
    for y in range(8):
        ro.moveRight()
    ro.drop()
    for y in range(8):
        ro.moveLeft()

ro.wait()