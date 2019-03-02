#usr/bin/python

import numpy as np
import random
##################################
# Functions #



#################################
# Classes #

class object:
    numofobjects = 0

    def __init__(self, position):
        self.position = position




class Agent:

    numofagents = 0
    gtick = 0
    instances = set()

    def __init__(self,name,position,tick, lp, vel, dmg, att, attspeed, vtd):
        self.position = np.array(position)
        self.lp = int(lp)
        self.vel = int(vel)
        self.dmg = int(dmg)
        self.tick = int(tick)
        self.vtd = int(vtd)
        self.att = int(att)
        self.attspeed = int(attspeed)
        self.name = str(name)

        Agent.numofagents += 1
        Agent.instances.add(self)

    def move(self,direction):
        dist = int(round(np.linalg.norm(np.array(direction))))
        if dist <= 2 :
            self.position += direction
        else:
            self.position += np.array(direction)
            self.tick += int(round(((np.linalg.norm(direction)-2)*5.0/self.vel).clip(min = 0)))

    def attack(self, target):
        if round(np.linalg.norm(self.position - target.position)) <= 1:
            if (random.randint(1,20) + random.randint(1,20) + self.att) > target.vtd:
                target.lp -= self.dmg + random.randint(1,6)
                print(target.lp)
                self.tick += self.attspeed
            else:
                self.tick += self.attspeed


A=Agent("hans",(1,1),2,10,7,2,9,5,20)
B=Agent("franz",(2,0),5,10,7,2,9,5,30)



#########################################
#   Game loop #

run = True
while run:
  #  print(Agent.gtick)
    for figure in Agent.instances:
        if (figure.tick - Agent.gtick) <= 0:
            print(figure.name)
            action = str(input("input: "))
            print(action)
            if action == "attack":
                lot = [x for x in Agent.instances] 
                print("Possible targets: ",lot )
                target = str(input(" "))
                figure.attack(eval(target))
            if action == "move":
                xdir = int(input("x: "))
                ydir = int(input("y: "))
                figure.move((xdir,ydir))
            if action == "look":
                for x in Agent.instances:
                    print(x.name,", LP: ",x.lp , ", pos: " , x.position)
    Agent.gtick += 1
    for x in Agent.instances:
        if x.lp <= 0:
            run = False

