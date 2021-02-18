from robot import Robot


def main() -> None:
    robot = Robot("Andrew")
    print(robot)
    robot.execute("forward right forward")
    print(robot)
    robot.execute("left backward left forward")
    print(robot)
    # NOTE: Intentionally make a typo, causing an error
    robot.execute("right forward forward favard")
    print(robot)

if __name__ == '__main__':
    main()