import copy
import math

def removeEdges(node, dict): 
    # removes elements in edge dictionary containing the node
    copyDict = copy.copy(dict)
    for key in copyDict:
        if (node[0], node[1]) == (dict[key][0][0], dict[key][0][1]):
            del dict[key]
        elif (node[0], node[1]) == (dict[key][1][0], dict[key][1][1]):
            del dict[key]
            
def reverseDict(dict):
    maxKey = len(dict)-1
    newDict = {}
    while maxKey >= 0:
        newDict[maxKey] = dict[maxKey]
        maxKey -= 1
    return newDict
    
def removeEdgeByNode(x, y, node, edge, event, dict, data):
    # removes edges connected to node
    copyDict = copy.copy(dict)
    for otherEnd in copyDict[edge]:
        if (x, y) == (otherEnd[0], otherEnd[1]):
            removeEdges((data.nodes[node][0], 
                data.nodes[node][1]), data.allEdges)
            dict[edge].remove(otherEnd)
    if (x, y) == (edge[0], edge[1]):
        removeEdges((data.nodes[node][0], data.nodes[node][1]), 
            data.allEdges)
        del dict[edge]
            
def mousePressedEraseNode(event, data):
    # erase node and edges connected to the node
    copyNodes = copy.copy(data.nodes)
    (copyRed, copyBlue) = (copy.copy(data.redEdges),copy.copy(data.blueEdges))
    for node in copyNodes:
        (x, y) = (copyNodes[node][0], copyNodes[node][1])
        if (x-data.nodeR) <= event.x <= (x+data.nodeR):
            if (y-data.nodeR) <= event.y <= (y+data.nodeR):
                for edge in copyRed:
                    removeEdgeByNode(x, y, node, edge, event, 
                        data.redEdges, data)
                for edge in copyBlue:
                    removeEdgeByNode(x, y, node, edge, event,
                        data.blueEdges, data)
                del data.nodes[node]
                data.numNodes -= 1
    

def lineEquation(x0, y0, x1, y1): # finds slope and y-intercept of a line
    if x1 == x0:
        slope = 10000000
        b1 = x0
    else:
        slope = (y1-y0)/(x1-x0)
        b1 = y0-slope*x0
    return (slope, b1)

def solveLines(slope1, slope2, b1, b2, data): # finds intersection of two lines
    a = (b2-b1)/(slope1-slope2)
    b = slope1*a+b1
    return (a,b)

def distance(x0, y0, x1, y1): # finds distance between two points
    return math.sqrt((x1-x0)**2+(y1-y0)**2)
    
def calculateEdge(edge, otherEnd, dict, event, data):
    # calculates which edge you clicked on and erases it
    copyAll = copy.copy(data.allEdges)
    (x0, y0) = (edge[0], edge[1])
    (x1, y1) = (otherEnd[0], otherEnd[1])
    (slope, b1) = lineEquation(x0,y0,x1,y1)
    perpSlope = -1/slope
    b2 = event.y-perpSlope*event.x
    intersectX, intersectY = solveLines(slope, perpSlope, b1, b2, data)
    clickDistance = distance(event.x, event.y, intersectX, intersectY)
    if clickDistance <= 5:
        for edges in copyAll:
            if (edge, otherEnd) == (copyAll[edges][0], copyAll[edges][1]) or \
                (edge, otherEnd) == (copyAll[edges][1], copyAll[edges][0]):
                del data.allEdges[edges]
        dict[edge].remove(otherEnd)
        
def eraseEdge(event, data):
    # erases clicked on edge
    for edge in data.redEdges:
        for otherEnd in data.redEdges[edge]:
            calculateEdge(edge, otherEnd, data.redEdges, event, data)
            
    for edge in data.blueEdges:
        for otherEnd in data.blueEdges[edge]:
            calculateEdge(edge, otherEnd, data.blueEdges, event, data)