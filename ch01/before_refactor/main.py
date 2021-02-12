from robot import Robot


def main():
    robot = Robot("Andrew")
    robot.order(0) # walk
    robot.order(1) # stop 
    robot.order(2) # jump


if __name__ == '__main__':
    main()
