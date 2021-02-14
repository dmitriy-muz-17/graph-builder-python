# animates DFS searching on a graph

import copy
from tkinter import *

from dfs import *
from convertNodes import *

def initDFS(data):
    data.endPoints = { "start": None, "search": None }
    data.choose = None
    data.graph = createNodeGraph(data)
    data.DFSvisited = dfsSearch(data.graph, data.endPoints["start"], 
        data.endPoints["search"])
    data.found = False
    data.startNode = None
    data.firstStart = None
    (data.startNodeX, data.startNodeY) = (None, None)
    data.endNode = None 
    (data.endNodeX, data.endNodeY) = (None, None)
    (data.tempX1, data.tempY1) = (None, None)
    data.highlightedEdges = [ ]
    data.move = dict()
    data.moving = [ ]
    data.alreadyVisited = set()
    data.finished = False
    data.visited = [ ]
    data.solution = True

def searchDFS(event, data): 
    if data.width//8-80 <= event.x <= data.width//8+80:
        if data.height//8+(data.height*4)//10-20 <= event.y <= \
            data.height//8+(data.height*4)//10+20:
            data.build.mode = "searchDFS"
            
def convertToCoord(num, data):
    for node in data.nodes:
        if num == node:
            return (data.nodes[node][0], data.nodes[node][1])
            
def updateCoords(data):
    data.startNode = data.DFSvisited[0]
    for node in data.nodes:
        if node == data.startNode:
            data.startNodeX = data.nodes[node][0]
            data.startNodeY = data.nodes[node][1]
    data.endNode = data.DFSvisited[1]
    for node in data.nodes:
        if node == data.endNode:
            data.endNodeX = data.nodes[node][0]
            data.endNodeY = data.nodes[node][1]
    (data.tempX1, data.tempY1) = (data.startNodeX, data.startNodeY)
    data.move = {"start":(data.startNodeX, data.startNodeY), \
        "end":(data.endNodeX, data.endNodeY)}
    data.moving = [((data.startNodeX, data.startNodeY), \
        (data.tempX1, data.tempY1))]
            
def setStart(event, data):
    if data.build.mode == "searchDFS" and data.choose != "search" and \
        data.choose != "done":
        data.endPoints["start"] = chooseStartNode(event, data)
        data.firstStart = chooseStartNode(event, data)
        if data.endPoints["start"] != None:
            data.choose = "search"

def setEnd(event, data):
    if data.build.mode == "searchDFS":
        if data.choose == "search":
            data.endPoints["search"] = chooseSearchNode(event, data)
            if data.endPoints["search"] != data.endPoints["start"]:
                data.choose = "done"
            data.graph = createNodeGraph(data)
            data.DFSvisited = dfsSearch(data.graph, data.endPoints["start"], 
                data.endPoints["search"])
        if data.choose == "done":
            try:
                updateCoords(data)
            except:
                data.solution = False
            
def chooseStartNode(event, data):
    for node in data.nodes:
        (x, y) = (data.nodes[node][0], data.nodes[node][1])
        if ((x-data.nodeR) <= event.x <= (x+data.nodeR)) and \
            (y-data.nodeR) <= event.y <= (y+data.nodeR):
            return node
            
def chooseSearchNode(event, data):
    for node in data.nodes:
        (x, y) = (data.nodes[node][0], data.nodes[node][1])
        if ((x-data.nodeR) <= event.x <= (x+data.nodeR)) and \
            (y-data.nodeR) <= event.y <= (y+data.nodeR):
            return node

def createNodeGraph(data):
    nodeMap = mapNodes(data.allEdges)
    return convertToNode(nodeMap, data.nodes)

def nextLeg(data):
    data.highlightedNodes.add((data.endNodeX,data.endNodeY))
    if (data.startNodeX, data.startNodeY) != (data.endNodeX, data.endNodeY):
        data.highlightedEdges.append(((data.startNodeX, \
            data.startNodeY), (data.endNodeX, data.endNodeY)))
    data.alreadyVisited.add(convertCoord((data.endNodeX, \
        data.endNodeY), data.nodes))
    if data.endNode in data.graph[data.startNode] and data.finished == False:
        element = data.DFSvisited.pop(0)
        data.DFSvisited.append(element)
        updateCoords(data)
    if data.startNode == data.endPoints["search"]:
        data.finished = True
    if data.endNode not in data.graph[data.startNode] and \
        data.finished == False:
        data.startNode  = data.startNode - 1
        for node in data.nodes:
            if node == data.startNode:
                data.startNodeX = data.nodes[node][0]
                data.startNodeY = data.nodes[node][1]
        data.endNode = data.DFSvisited[1]
        for node in data.nodes:
            if node == data.endNode:
                data.endNodeX = data.nodes[node][0]
                data.endNodeY = data.nodes[node][1]
        (data.tempX1, data.tempY1) = (data.startNodeX, data.startNodeY)
        data.move = {"start":(data.startNodeX, data.startNodeY), \
            "end":(data.endNodeX, data.endNodeY)}
        data.moving = [((data.startNodeX, data.startNodeY), \
            (data.tempX1, data.tempY1))]
        
        
def edgeInDict(x0, y0, x1, y1, dict):
    for key in dict:
        if ((x0, y0) in dict[key]) and ((x1, y1) in dict[key]):
            return True
    return False
    
def connectedNode(data):
    # Case 1: next node is directly connected to current node
    if (data.move["end"][0] >= data.move["start"][0]) and \
        (data.move["end"][1] >= data.move["start"][1]):
        speedX = (data.move["end"][0]-data.move["start"][0])/25
        speedY = (data.move["end"][1]-data.move["start"][1])/25
        data.tempX1 += speedX
        data.tempY1 += speedY
        if (data.tempX1 >= data.move["end"][0]) and \
            (data.tempY1 >= data.move["end"][1]):
            data.tempX1 -= speedX
            data.tempY1 -= speedY
            nextLeg(data)
    elif (data.move["end"][0] <= data.move["start"][0]) and \
        (data.move["end"][1] >= data.move["start"][1]):
        speedX = (data.move["start"][0]-data.move["end"][0])/25
        speedY = (data.move["end"][1]-data.move["start"][1])/25
        data.tempX1 -= speedX
        data.tempY1 += speedY
        if (data.tempX1 <= data.move["end"][0]) and \
            (data.tempY1 >= data.move["end"][1]):
            data.tempX1 += speedX
            data.tempY1 -= speedY
            nextLeg(data)
            
def unconnectedNode(data):
    # Case 2: next node is not connected to current node
    data.startNode  = data.startNode - 1
    for node in data.nodes:
        if node == data.startNode:
            data.startNodeX = data.nodes[node][0]
            data.startNodeY = data.nodes[node][1]
    data.endNode = data.DFSvisited[1]
    for node in data.nodes:
        if node == data.endNode:
            data.endNodeX = data.nodes[node][0]
            data.endNodeY = data.nodes[node][1]
    (data.tempX1, data.tempY1) = (data.startNodeX, data.startNodeY)
    data.move = {"start":(data.startNodeX, data.startNodeY), \
        "end":(data.endNodeX, data.endNodeY)}
    data.moving = [((data.startNodeX, data.startNodeY), \
        (data.tempX1, data.tempY1))]
    connectedNode(data)
    
def mousePressedDFS(event, data):
    setStart(event, data)
    setEnd(event, data)
        
def timerDFS(data):
    data.timerDelay = 100
    if data.build.mode == "searchDFS" and data.choose == "done":
        try:
            # Case 1
            if edgeInDict(data.move["start"][0], data.move["start"][1], \
                data.move["end"][0], data.move["end"][1], data.allEdges):
                connectedNode(data)
            # Case 2
            if not edgeInDict(data.move["start"][0], data.move["start"][1], \
                data.move["end"][0], data.move["end"][1], data.allEdges):
                unconnectedNode(data)
        except:
            data.solution = False

def redrawDFSAnimated(canvas, data): 
    if data.solution == False:
        canvas.create_text(data.width//2, data.height//5, text = "No Solution")
    else:
        if data.finished == True:
            canvas.create_text(data.width//2, data.height//5-data.height//20, 
                text = "Found!")
        startNode = convertToCoord(data.endPoints["start"], data)
        canvas.create_oval(startNode[0]-data.build.bigNodeR, 
            startNode[1]-data.build.bigNodeR, startNode[0]+data.build.bigNodeR,
            startNode[1]+data.build.bigNodeR, fill = "yellow")
        canvas.create_line(data.startNodeX, data.startNodeY, data.tempX1,
            data.tempY1, fill = "yellow", width = 5)
        for edge in data.highlightedEdges:
            canvas.create_line(edge[0], edge[1], fill = "yellow", width = 5)
            canvas.create_oval(edge[0][0]-data.build.bigNodeR,
                edge[0][1]-data.build.bigNodeR, edge[0][0]+data.build.bigNodeR,
                edge[0][1]+data.build.bigNodeR, fill = "yellow")
            canvas.create_oval(edge[1][0]-data.build.bigNodeR,
                edge[1][1]-data.build.bigNodeR, edge[1][0]+data.build.bigNodeR,
                edge[1][1]+data.build.bigNodeR, fill = "yellow")

def drawDFS(canvas, data):
    if data.choose != "search" and data.choose != "done":
        canvas.create_text(data.width//2, data.height//5-data.height//20, 
            text = "Choose a starting vertex")
    if data.choose == "search":
        canvas.create_text(data.width//2, data.height//5-data.height//20, 
            text = "Choose a vertex to search for")
    if data.build.mode == "searchDFS" and data.choose == "done":
        redrawDFSAnimated(canvas, data)
