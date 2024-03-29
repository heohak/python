"""Ex14."""


from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    """
    Make the robot move, doesnt matter how much, just as long as it has moved from the starting position.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(30)
    robot.sleep(2)
    robot.set_wheels_speed(0)
    robot.done()


def drive_to_line(robot: FollowerBot):
    """
    Drive the robot until it meets a perpendicular black line, then drive forward 25cm.

    There are 100 pixels in a meter.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    if robot.get_line_sensors() == 0:
        robot.set_wheels_speed(0)
        robot.sleep(2)
    else:
        robot.set_wheels_speed(10)
        robot.sleep(20)


def follow_the_line(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track.

    :param FollowerBot robot: instance of the robot that you need to make move
    """



def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
