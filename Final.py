from startscreen import *
from coverDesign import *
from build import *
from convertNodes import *
from cycles import *
from tkinter import *
import random
import math
import copy

def almostEqual(d1, d2, epsilon=10**-7):
    return (abs(d2 - d1) < epsilon)

def init(data):
    data.startscreen = Startscreen(data)
    data.design1 = Design1(data)
    data.design2 = Design2(data)
    data.build = Build(data)
    data.hamilton = Hamilton(data)
    data.mode = "startScreen" 
    data.backX = data.width//10-data.width//50
    data.backY = data.height//20
    data.backRX = data.width//15
    data.backRY = data.height//30
    data.nodeR = data.width//80
    data.nodes = dict()
    data.mapNodes = dict()
    data.degrees = dict()
    data.allEdges = dict()
    data.edges = [ ]
    data.redEdges = dict()
    data.blueEdges = dict()
    data.lightNodes = [ ]
    data.numNodes = 0
    data.nextNode = 0
    data.numEdges = 0
    data.nextEdge = 0
    data.highlight = [ ]
    data.erase = [ ]
    data.removedRedEdges = dict()
    data.removedBlueEdges = dict()
    data.lines = [ ]
    data.level = None
    

def mousePressed(event, data):
    if data.mode == "startScreen":
        mousePressedStart(event, data)

    elif data.mode == "cycles":
        mousePressedCycles(event, data)
    elif data.mode == "build":
        mousePressedBuild(event, data)

def keyPressed(event, data):
    if event.keysym == "n":
        data.build.mode = "node"
    elif event.keysym == "r":
        data.build.mode = "red edge"
    elif event.keysym == "b":
        data.build.mode = "blue edge"
    elif event.keysym == "e":
        data.build.mode = "eraser"
    if data.build.enterWeight == True:
        keyPressedWeight(event, data)

def timerFired(data):
    if data.mode == "startScreen":
        data.design1.timerFired(data)
        data.design2.timerFired(data)

    if data.build.mode == "searchDFS":
        timerDFS(data)
    elif data.build.mode == "searchBFS":
        timerBFS(data)
    
def redrawAll(canvas, data):
    if data.mode == "startScreen":
        canvas.create_rectangle(0,0,data.width, data.height, fill = "sky blue")
        data.design1.redrawAll(canvas, data)
        data.design2.redrawAll(canvas, data)
        data.startscreen.draw(canvas, data)
    elif data.mode == "build":
        data.build.draw(canvas, data)
        data.hamilton.drawHamilton(canvas, data)
        redrawBuild(canvas, data)
    elif data.mode == "cycles":
        data.cycles.draw(canvas, data)
    




def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 
    root = Tk()
    init(data)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    root.mainloop()  

run(1000,800)
