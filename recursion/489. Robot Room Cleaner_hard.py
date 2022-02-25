
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def __init__(self ,):
        self.cleaned = set()
        self.cleaned.add((0, 0))

    def recorder(self, i, j, d):
        if d% 4 == 0:
            i -= 1
        elif d % 4 == 1:
            j -= 1
        elif d % 4 == 2:
            i += 1
        elif d % 4 == 3:
            j += 1
        return i, j

    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def backtrack_robot(robot, x_cor, y_cor, abs_direction):
            robot.clean()
            i, j, d = x_cor, y_cor, abs_direction
            self.cleaned.add((i, j))
            for direction in ('foward', 'left', 'right'):
                if direction == 'foward':
                    psudo_i, psudo_j = self.recorder(i, j, d)
                    if (psudo_i, psudo_j) not in self.cleaned and robot.move():
                        backtrack_robot(robot, psudo_i, psudo_j, d)
                elif direction == 'left':
                    robot.turnLeft()
                    d += 1
                    psudo_i, psudo_j = self.recorder(i, j, d)
                    if (psudo_i, psudo_j) not in self.cleaned and robot.move():
                        backtrack_robot(robot, psudo_i, psudo_j, d)
                    robot.turnRight()
                    d -= 1
                elif direction == 'right':
                    robot.turnRight()
                    d -= 1
                    psudo_i, psudo_j = self.recorder(i, j, d)
                    if (psudo_i, psudo_j) not in self.cleaned and robot.move():
                        backtrack_robot(robot, psudo_i, psudo_j, d)
                    robot.turnLeft()
                    d += 1

            robot.turnRight()
            robot.turnRight()
            d -= 2
            psudo_i, psudo_j = self.recorder(i, j, d)
            if (psudo_i, psudo_j) not in self.cleaned and robot.move():
                backtrack_robot(robot, psudo_i, psudo_j, d)

            else:
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
                d += 2

        backtrack_robot(robot, 0, 0, 0)