# holds code for implementing Dijkstra's algorithm on a user-created graph

from convertGraph import *
from convertNodes import *
from visualDFS import *

def initDijkstra(data):
    data.choosePoints = None
    data.start = None
    data.search = None

def neighbors(node, graph, visited, unvisited):
    answer = dict()
    for node in visited:
        for key in graph:
            if node == key:
                for pos in graph[key]:
                    if pos not in visited:
                        answer[pos] = graph[key][pos]
    return answer
        
def dijkstra(graph, start, end, dict1, current = None): 
    min = float("inf")
    if current == None:
        current = start
    path = dict()
    nodes = set()
    visited = [ ]
    unvisited = dict()
    for key in range(len(dict1)):
        unvisited[key] = None
        unvisited[start] = 0
        path[key] = [0]
    while True: 
        currentCost = unvisited[current]
        currentPath = path[current]
        min = float("inf")
        posNodes = neighbors(current, graph, visited, unvisited)
        for node in posNodes:
            newCost = currentCost+posNodes[node]
            newPath = currentPath+[node]
            if unvisited[node] == None or unvisited[node] > newCost:
                unvisited[node] = newCost
                path[node] = newPath
        visited.append(current)
        if current == end:
            return unvisited, path
        for node in posNodes:
            if posNodes[node] < min:
                min = posNodes[node]
                current = node

def setPoints(event, data):
    if data.build.mode == "dijkstra" and data.start == None:
        data.choosePoints = "start"
        data.start = chooseStartNode(event, data)
        data.choosePoints = "search"
    elif data.build.mode == "dijkstra" and data.start != None and \
        data.search == None:
        data.choosePoints = "search"
        data.search = chooseSearchNode(event, data)
        data.choosePoints = "done"
    elif data.build.mode == "dijkstra" and data.start != None and \
        data.search != None:
        data.choosePoints = "done"
        
def edgesDict(node, dict1, data, list = None, edgeDict = None): 
    # return list of edges between the nodes in the path 
    if edgeDict == None:
        edgeDict = [ ]
    if list == None:
        for key in dict1:
            if key == node:
                list = dict1[key]
    if len(list) == 1:
        return edgeDict
    while len(list) >= 2:
        edgeDict.append(((convertToCoord(list[0], data), convertToCoord(list[1], data))))
        temp = edgesDict(node, dict1, data, list[1:], edgeDict)
        return temp
            
def redrawDijkstra(canvas, data):
    graph = usefulGraph(data.allEdges, data.nodes)
    (unvisited, path) = dijkstra(graph, data.start, data.search, data.nodes)
    canvas.create_text(data.width//2, data.height//5-data.height//20, 
        text = "Shortest path length = " + str(unvisited[data.search]))
    (startX, startY) = convertToCoord(data.start, data)
    canvas.create_oval(startX-data.build.bigNodeR, startY-data.build.bigNodeR,
        startX+data.build.bigNodeR, startY+data.build.bigNodeR,
        fill = "yellow")
    for node in path[data.search]:
        (x, y) = convertToCoord(node, data)
        canvas.create_oval(x-data.build.bigNodeR, y-data.build.bigNodeR,
            x+data.build.bigNodeR, y+data.build.bigNodeR, fill = "yellow")
    drawEdges = edgesDict(data.search, path, data)
    for edge in drawEdges:
        canvas.create_line(edge[0], edge[1], width = 5, fill = "yellow")
            
def drawDijkstra(canvas, data):
    if data.start == None:
        canvas.create_text(data.width//2, data.height//5-data.height//20, 
            text = "Choose a starting vertex")
    if data.start != None and data.search == None:
        canvas.create_text(data.width//2, data.height//5-data.height//20, 
            text = "Choose a vertex to search for")
    if data.start != None and data.search != None: 
        # check that all edges have edge weights
        for edge in data.allEdges:
            if data.allEdges[edge][2] == None:
                canvas.create_text(data.width//2, 
                    data.height//5-data.height//20, 
                    text = "Please enter edge weights on all edges")
                return None
        redrawDijkstra(canvas, data)
        
        
        
    
    

    
