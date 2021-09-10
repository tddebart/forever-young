from RobotArm import RobotArm

ro = RobotArm('exercise 6')
ro.speed = 2
for x in range(8):
    ro.moveRight()

for x in range(1,10):
    ro.grab()
    ro.moveRight()
    ro.drop()
    ro.moveLeft()
    ro.moveLeft()

ro.wait()