from startscreen import *
from coverDesign import *
from build import *
from convertNodes import *
from bfs import *
from dfs import *
from visualDFS import *
from visualBFS import *
from cycles import *
from dijkstra import *
from tkinter import *
import random
import math
import copy

def almostEqual(d1, d2, epsilon=10**-7): # taken from class notes
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
    initDijkstra(data)
    initDFS(data)
    data.animateDFS = True
    data.highlightDFS = [ ]
    data.dfs = dfsSearch(graphBuilder(), 0, 7)
    initBFS(data)
    data.animateBFS = True
    data.highlightBFS = [ ]
    data.bfs = bfsSearch(graphBuilder(), 0, 7)
    

def mousePressed(event, data):
    if data.mode == "startScreen":
        mousePressedStart(event, data)

    elif data.mode == "cycles":
        mousePressedCycles(event, data)
    elif data.mode == "build":
        mousePressedBuild(event, data)
        data.hamilton.mousePressedHamilton(event, data)
        data.hamilton.chooseStartNode(event, data)

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
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed

run(1000,800)
