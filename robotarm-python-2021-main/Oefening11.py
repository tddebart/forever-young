from RobotArm import RobotArm

ro = RobotArm('exercise 11')
ro.speed = 3

for x in range(8):
    ro.grab()
    kleur = ro.scan()
    if kleur == "white":
        ro.moveRight()
        ro.drop()
        ro.moveRight()
        x += 1
    else:
        ro.drop()
        ro.moveRight()


ro.wait()