class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        position=[0,0]
        origin=[0,0]
        direction=[0,1]
        n=len(instructions)
        for j in range(0,4):
            for i in range(0,n):
                if instructions[i]=="G":
                    position[0]+=direction[0]
                    position[1]+=direction[1]
                elif instructions[i]=="L":
                    temp=direction[0]
                    direction[0]=(-1)*direction[1]
                    direction[1]=temp
                elif instructions[i]=="R":
                    temp=direction[1]
                    direction[1]=(-1)*direction[0]
                    direction[0]=temp
        if position==origin:
            return True
        else:
            return False