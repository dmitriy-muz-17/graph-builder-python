# function for depth-first search

from tkinter import *

def initDFS(data):
    data.animateDFS = True
    data.highlightDFS = [ ]
    data.dfs = dfsSearch(graphBuilder(), 0, 7)

def graphBuilder():
    return {0:[1, 2, 3],
            1:[0, 4],
            2:[0, 5, 6],
            3:[0, 7],
            4:[1],
            5:[2],
            6:[2],
            7:[3]}

def depthMoves(graph, current, visited):
    # returns list of possible moves
    moves = [ ]
    for move in graph[current]:
        if move not in visited:
            moves.append(move)
    return moves
    
def dfsSearch(graph, start, search, current=None, visited=None):
    if current == None:
        current = start
    if visited == None:
        visited = [ ]
        visited.append(start)
    # Base Case:
    if current == search:
        return visited
    # Recursive Case:
    for move in depthMoves(graph, current, visited):
        visited.append(move)
        current = move
        temp = dfsSearch(graph, start, search, current, visited)
        if temp != None:
            return temp
    return None


# Animating dfs - learn mode
# draw a graph and highlight the nodes it has checked

# def DFSSampleNodes(data):
#     level1Height = data.height//12+data.height//20
#     level2Height = data.height//8+data.height//10+data.height//20
#     level3Height = data.height//8+(data.height*2.5)//10+data.height//20
#     node1 = (data.width//4, level1Height)
#     node2 = (data.width//4-data.width//8, level2Height)
#     node3 = (data.width//4, level2Height)
#     node4 = (data.width//4+data.width//8, level2Height)
#     node5 = (data.width//4-data.width//6, level3Height)
#     node6 = (data.width//4-data.width//20, level3Height)
#     node7 = (data.width//4+data.width//20, level3Height)
#     node8 = (data.width//4+data.width//6, level3Height)
#     
#     return (node1, node2, node3, node4, node5, node6, node7, node8)
#     
# def DFSDict(data):
#     nodeDict = dict()
#     (node1,node2,node3,node4,node5,node6,node7,node8) = DFSSampleNodes(data)
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
# def DFSSampleEdges(data):
#     (node1,node2,node3,node4,node5,node6,node7,node8) = DFSSampleNodes(data)
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
# def DFSTimer(data):
#     data.timerDelay = 1000
#     graph = graphBuilder()
#     element = data.dfs.pop(0)
#     data.highlightDFS.append(element)
#     data.dfs.append(element)
#     if len(data.highlightDFS) > 8:
#         data.highlightDFS = [0]
#         
# def DFSDescription(canvas, data):
#     canvas.create_text(data.width//4, (data.height*4)//5, text = "Description")
#     
# def redrawDFS(canvas, data):
#     edges = DFSSampleEdges(data)
#     for edge in edges:
#         canvas.create_line(edge, width = 3)
#     nodes = DFSSampleNodes(data)
#     for node in nodes:
#         canvas.create_oval(node[0]-data.nodeR, node[1]-data.nodeR,
#             node[0]+data.nodeR, node[1]+data.nodeR, fill = "black")
#     nodeDict = DFSDict(data)
#     for num in data.highlightDFS:
#         for node in nodeDict:
#             if num == node:
#                 canvas.create_oval(nodeDict[node][0]-data.nodeR, 
#                     nodeDict[node][1]-data.nodeR,
#                     nodeDict[node][0]+data.nodeR, 
#                     nodeDict[node][1]+data.nodeR, fill = "yellow")
#     canvas.create_text(data.width//4, data.height//8+(data.height*4)//10, 
#         text = "DFS Searching", font = "Georgia 16")
#     DFSDescription(canvas, data)
#         
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# # Animating dfs - build mode
# # user-built graph; highlight nodes and edges it's checking lol fuck
#     
