# produces dictionary mapping each node to the nodes it connects to

import math
from tkinter import *

def convertCoord(coord, dict): 
    # converts a coordinate to its corresponding node
    for node in dict:
        if coord == (dict[node][0], dict[node][1]):
            return node

def mapNodes(dict):
    # 
    nodeMap = {}
    for edge in dict:
        firstNode = dict[edge][0]
        secondNode = dict[edge][1]
        if firstNode not in nodeMap:
            nodeMap[firstNode] = [dict[edge][1]]
        else:
            nodeMap[firstNode].append(dict[edge][1])
        if secondNode not in nodeMap:
            nodeMap[secondNode] = [dict[edge][0]]
        else:
            nodeMap[secondNode].append(dict[edge][0])
    return nodeMap
    
def convertToNode(dict, dict2): 
    converted = {}
    for elem in dict:
        node = convertCoord(elem, dict2)
        for map in dict[elem]:
            mapNode = convertCoord(map, dict2)
            if node not in converted:
                converted[node] = [mapNode]
            else:
                converted[node].append(mapNode)
    return converted
