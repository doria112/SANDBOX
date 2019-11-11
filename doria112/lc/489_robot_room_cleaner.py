# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
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
    def __init__(self):
        self.loc = 0
    
    def nextPos(self, pos, face):
        if face == 0:
            return [pos[0]-1, pos[1]]
        elif face == 1:
            return [pos[0], pos[1]+1]
        elif face == 2:
            return [pos[0]+1, pos[1]]
        elif face == 3:
            return [pos[0], pos[1]-1]
        else:
            raise Exception("wrong face")
        
    def backtrack(self, robot, cleaned, pos, face):
        robot.clean()
        cleaned.append(pos)
        #print(pos, face, cleaned)
        for i in range(4):
            next_pos = self.nextPos(pos, face)
            #print("i={}, face={},next pos={}".format(i,face, next_pos))
            if next_pos not in cleaned:
                if robot.move():
                    #print("moved to {}".format(face))
                    cleaned = self.backtrack(robot, cleaned, next_pos, face)
                    robot.turnLeft()
                    #print("left")
                else:
                    robot.turnRight()
                    #print("right1")
            else: 
                robot.turnRight()
                #print("right2")
            face = (face +1)%4
        robot.turnLeft()
        robot.turnLeft()
        #print("turned back")
        robot.move()
        return cleaned
    
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        cleaned = []
        self.backtrack(robot, cleaned, [0,0], 0)
