# function for breadth-first search

from tkinter import *

def initBFS(data):
    data.animateBFS = True
    data.highlightBFS = [ ]
    data.bfs = bfsSearch(graphBuilder(), 0, 7)

def graphBuilder():
    return {0:[1, 2, 3],
            1:[0, 4],
            2:[0, 5, 6],
            3:[0, 7],
            4:[1],
            5:[2],
            6:[2],
            7:[3]}

def breadthMoves(graph, start, seen = None):
    # returns a list of possible moves from left to right, top to bottom
    if seen == None: seen = [start]
    moves = [ ]
    for node in graph:
        for move in graph[node]:
            if move not in seen:
                seen.append(move)
                moves.append(move)
    return moves

def bfsSearch(graph, start, search, current=None, visited=None):
    # iteratively loops through possible moves and checks
    if current == None: current = start
    if visited == None: visited = [start]
    possibleMoves = breadthMoves(graph, start)
    for move in possibleMoves:
        visited.append(move)
        if move == search:
            return visited
    return None
    
    
    
# def BFSSampleNodes(data):
#     level1Height = data.height//12+data.height//20
#     level2Height = data.height//8+data.height//10+data.height//20
#     level3Height = data.height//8+(data.height*2.5)//10+data.height//20
#     node1 = ((data.width*3)//4, level1Height)
#     node2 = ((data.width*3)//4-data.width//8, level2Height)
#     node3 = ((data.width*3)//4, level2Height)
#     node4 = ((data.width*3)//4+data.width//8, level2Height)
#     node5 = ((data.width*3)//4-data.width//6, level3Height)
#     node6 = ((data.width*3)//4-data.width//20, level3Height)
#     node7 = ((data.width*3)//4+data.width//20, level3Height)
#     node8 = ((data.width*3)//4+data.width//6, level3Height)
#     
#     return (node1, node2, node3, node4, node5, node6, node7, node8)
#     
# def BFSDict(data):
#     nodeDict = dict()
#     (node1,node2,node3,node4,node5,node6,node7,node8) = BFSSampleNodes(data)
#     nodeDict[0] = node1
#     nodeDict[1] = node2
#     nodeDict[2] = node3
#     nodeDict[3] = node4
#     nodeDict[4] = node5
#     nodeDict[5] = node6
#     nodeDict[6] = node7
#     nodeDict[7] = node8
#     
#     return nodeDict
# 
# def BFSSampleEdges(data):
#     (node1,node2,node3,node4,node5,node6,node7,node8) = BFSSampleNodes(data)
#     edge1 = (node1, node2)
#     edge2 = (node1, node3)
#     edge3 = (node1, node4)
#     edge4 = (node2, node5)
#     edge5 = (node3, node6)
#     edge6 = (node3, node7)
#     edge7 = (node4, node8)
#     
#     return (edge1, edge2, edge3, edge4, edge5, edge6, edge7)
# 
# def BFSTimer(data):
#     data.timerDelay = 1000
#     graph = graphBuilder()
#     element = data.bfs.pop(0)
#     data.highlightBFS.append(element)
#     data.bfs.append(element)
#     if len(data.highlightBFS) > 8:
#         data.highlightBFS = [0]
#         
# def BFSDescription(canvas, data):
#     canvas.create_text((data.width*3)//4, (data.height*4)//5, 
#         text = "Description")
#     
# def redrawBFS(canvas, data):
#     edges = BFSSampleEdges(data)
#     for edge in edges:
#         canvas.create_line(edge, width = 3)
#     nodes = BFSSampleNodes(data)
#     for node in nodes:
#         canvas.create_oval(node[0]-data.nodeR, node[1]-data.nodeR,
#             node[0]+data.nodeR, node[1]+data.nodeR, fill = "black")
#     nodeDict = BFSDict(data)
#     for num in data.highlightBFS:
#         for node in nodeDict:
#             if num == node:
#                 canvas.create_oval(nodeDict[node][0]-data.nodeR, 
#                     nodeDict[node][1]-data.nodeR,
#                     nodeDict[node][0]+data.nodeR, 
#                     nodeDict[node][1]+data.nodeR, fill = "yellow")
#     canvas.create_text((data.width*3)//4, data.height//8+(data.height*4)//10, 
#         text = "BFS Searching", font = "Georgia 16")
#     BFSDescription(canvas, data)
    
    