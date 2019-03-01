#usr/bin/python

import numpy as np

##################################
# Functions #

def normalize(v):
    return np.divide(v,np.linalg.norm(v))


#################################
# Classes #

class Agent:

    numofagents = 0

    def __init__(self, tick, position, lp, vel, dmg):
        self.position = np.array(position)
        self.lp = int(lp)
        self.vel = int(vel)
        self.dmg = int(dmg)
        self.tick = int(tick)
    def move(self,direction):
        dist = int(round(np.linalg.norm(np.array(direction))))
        if dist <= 2 :
            self.direction += direction
        else:
            self.position += np.array(direction)
            self.tick += int(round(((np.linalg.norm(direction)-2)*5.0/self.vel).clip(min = 0)))
            print(direction)
            print(5.0/self.vel)


A=Agent(0,(3,1),10,2,1)
B=Agent(0,(0,0),10,3,1)

print("pos: ",A.position)
print("tick: ",A.tick)
A.move((2,0))
print("pos: ",A.position)
print("tick: ",A.tick)
