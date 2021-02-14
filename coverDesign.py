# draws two identical animated designs on the startscreen 

from tkinter import *
import random
import math

def convertToRadians(num): # converts degrees to radians
    return num*(math.pi/180)

class Design1(object):
    def __init__(self, data):
        self.speed = 1
        self.r = data.width//60
        self.x = random.randint(0, data.width)
        self.y = random.randint(0, data.height)
        self.tempX = self.x
        self.tempY = self.y
        self.created = [ ]
        self.lines = [ ]
        self.angle = convertToRadians(random.randint(0, 360))
        self.length = random.randint(-300, 300)
        if abs(self.length) <= 50:
            self.length = random.randint(-120, 120)
        self.xLength = math.cos(self.angle)*self.length
        self.yLength = math.sin(self.angle)*self.length
        
    def reset(self, data):
        self.x = random.randint(0, data.width)
        self.y = random.randint(0, data.height)
        self.tempX = self.x
        self.tempY = self.y
        self.angle = convertToRadians(random.randint(0, 360))
        self.length = random.randint(-300, 300)
        if abs(self.length) <= 50:
            self.length = random.randint(-300, 300)
        self.xLength = math.cos(self.angle)*self.length
        self.yLength = math.sin(self.angle)*self.length
        
    def resetCoords(self, data):
        self.x = self.tempX
        self.y = self.tempY
        self.tempX = self.x
        self.tempY = self.y
        self.angle = convertToRadians(random.randint(0, 360))
        self.length = random.randint(-300, 300)
        if abs(self.length) <= 50:
            self.length = random.randint(-300, 300)
        self.xLength = math.cos(self.angle)*self.length
        self.yLength = math.sin(self.angle)*self.length
        
    def outOfBounds(x, y, data):
        if x < 0 or x > data.width:
            return True
        if y < 0 or y > data.height:
            return True
        return False
        
    def timerFired(self, data):
        data.timerDelay = 10 
        self.created.append((self.x, self.y))
        self.tempX += self.xLength/50
        self.tempY += self.yLength/50
        if Design1.outOfBounds(self.tempX, self.tempY, data):
            self.lines.append((self.x, self.y, self.tempX, self.tempY))
            Design1.reset(self, data)
        if (int(self.tempX) == int(self.x+self.xLength)) or \
            (int(self.tempY) == int(self.y+self.yLength)):
            self.created.append((self.tempX, self.tempY))
            self.lines.append((self.x, self.y, self.tempX, self.tempY))
            #restart
            Design1.resetCoords(self,data)
            
        
    def redrawAll(self, canvas, data):
        canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, 
            self.y+self.r, fill = "slategray4", outline = "slategray4")
        canvas.create_line(self.x, self.y, self.tempX, self.tempY, width = 4,
            fill = "slategray4")
        for node in self.created:
            canvas.create_oval(node[0]-self.r, node[1]-self.r, node[0]+self.r,
                node[1]+self.r, fill = "slategray4", outline = "slategray4")
        for edge in self.lines:
            canvas.create_line(edge[0], edge[1], edge[2], edge[3], width = 4,
                fill = "slategray4")
                
class Design2(object):
    def __init__(self, data):
        self.speed = 1
        self.r = data.width//60
        self.x = random.randint(0, data.width)
        self.y = random.randint(0, data.height)
        self.tempX = self.x
        self.tempY = self.y
        self.created = [ ]
        self.lines = [ ]
        self.angle = convertToRadians(random.randint(0, 360))
        self.length = random.randint(-300, 300)
        if abs(self.length) <= 50:
            self.length = random.randint(-120, 120)
        self.xLength = math.cos(self.angle)*self.length
        self.yLength = math.sin(self.angle)*self.length
        
    def reset(self, data):
        self.x = random.randint(0, data.width)
        self.y = random.randint(0, data.height)
        self.tempX = self.x
        self.tempY = self.y
        self.angle = convertToRadians(random.randint(0, 360))
        self.length = random.randint(-300, 300)
        if abs(self.length) <= 50:
            self.length = random.randint(-300, 300)
        self.xLength = math.cos(self.angle)*self.length
        self.yLength = math.sin(self.angle)*self.length
        
    def resetCoords(self, data):
        self.x = self.tempX
        self.y = self.tempY
        self.tempX = self.x
        self.tempY = self.y
        self.angle = convertToRadians(random.randint(0, 360))
        self.length = random.randint(-300, 300)
        if abs(self.length) <= 50:
            self.length = random.randint(-300, 300)
        self.xLength = math.cos(self.angle)*self.length
        self.yLength = math.sin(self.angle)*self.length
        
    def outOfBounds(x, y, data):
        if x < 0 or x > data.width:
            return True
        if y < 0 or y > data.height:
            return True
        return False
        
    def timerFired(self, data):
        data.timerDelay = 10 
        self.created.append((self.x, self.y))
        self.tempX += self.xLength/50
        self.tempY += self.yLength/50
        if Design2.outOfBounds(self.tempX, self.tempY, data):
            self.lines.append((self.x, self.y, self.tempX, self.tempY))
            Design2.reset(self, data)
        if (int(self.tempX) == int(self.x+self.xLength)) or \
            (int(self.tempY) == int(self.y+self.yLength)):
            self.created.append((self.tempX, self.tempY))
            self.lines.append((self.x, self.y, self.tempX, self.tempY))
            #restart
            Design2.resetCoords(self,data)
            
        
    def redrawAll(self, canvas, data):
        canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, 
            self.y+self.r, fill = "slategray4", outline = "slategray4")
        canvas.create_line(self.x, self.y, self.tempX, self.tempY, width = 4,
            fill = "slategray4")
        for node in self.created:
            canvas.create_oval(node[0]-self.r, node[1]-self.r, node[0]+self.r,
                node[1]+self.r, fill = "slategray4", outline = "slategray4")
        for edge in self.lines:
            canvas.create_line(edge[0], edge[1], edge[2], edge[3], width = 4,
                fill = "slategray4")


