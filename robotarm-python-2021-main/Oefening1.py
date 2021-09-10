from RobotArm import RobotArm

robotArm = RobotArm('exercise 1')
#robotArm.speed = 2

robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()

robotArm.wait()