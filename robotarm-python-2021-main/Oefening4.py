from RobotArm import RobotArm

ro = RobotArm('exercise 4')
ro.speed = 3

for y in range(3,0, -1):
    ro.grab()
    for x in range(y):
        ro.moveRight()
    ro.drop()
    for x in range(y):
        ro.moveLeft()
ro.moveRight()
for y in range(1,3):
    for x in range(y):
        ro.moveRight()
    ro.grab()
    for x in range(y):
        ro.moveLeft()
    ro.drop()

ro.wait()