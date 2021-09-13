from RobotArm import RobotArm

ro = RobotArm()
ro.randomLevel(1,7)
ro.speed = 3

positionfree = 1
position = 0

for x in range(7):
    ro.grab()
    scan = ro.scan()
    if scan == "":
        break
    while position != positionfree:
        ro.moveRight()
        position += 1
    ro.drop()
    while position != 0:
        ro.moveLeft()
        position-=1
    positionfree+=1





ro.wait()