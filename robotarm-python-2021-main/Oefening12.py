from RobotArm import RobotArm

ro = RobotArm('exercise 12')
ro.speed = 3

position = 0

for x in range(9):
    ro.grab()
    kleur = ro.scan()
    if kleur == "red":
        prevpos = position
        while position < 9:
            ro.moveRight()
            position+=1
        ro.drop()
        while position != prevpos:
            ro.moveLeft()
            position -= 1
        ro.moveRight()
        position += 1
        x += 1
    else:
        ro.drop()
        ro.moveRight()
        position += 1


ro.wait()