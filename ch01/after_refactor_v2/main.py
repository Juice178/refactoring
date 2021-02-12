from robot import Robot


def main():
    robot = Robot("Andrew")
    robot.order(Robot.COMAMND_WALK)
    robot.order(Robot.COMAMND_STOP) 
    robot.order(Robot.COMAMND_JUMP)


if __name__ == '__main__':
    main()
