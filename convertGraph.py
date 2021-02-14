# converts dictionaries of edges and nodes into one that maps each node to  
# another dictionary mapping a connecting node to the weight between the two

from convertNodes import *

def convertToCoord2(num, nodes): # converts node to its x/y coordinates
    for node in nodes:
        if num == node:
            return (nodes[node][0], nodes[node][1])

def getNodeDict(dict1, dict2): 
    # returns dictionary mapping each node to the nodes it connects to
    nodeMap = mapNodes(dict1)
    nodeDict = convertToNode(nodeMap, dict2)
    return nodeDict

def findWeight(node1, node2, dict1, dict2): 
    # returns weight between node1 and node2
    for edge in dict1:
        coord1 = convertToCoord2(node1, dict2)
        coord2 = convertToCoord2(node2, dict2)
        if ((coord1, coord2) == (dict1[edge][0], dict1[edge][1])) or \
            ((coord1, coord2) == (dict1[edge][1], dict1[edge][0])):
            return dict1[edge][2]

def usefulGraph(dict1, dict2): 
    # returns dictionary as described on line 1
    newDict = dict()
    nodeDict = getNodeDict(dict1, dict2)
    for node in dict2:
        for mapNode in nodeDict[node]:
            if node not in newDict:
                newDict[node] = {mapNode: findWeight(node, mapNode, dict1, dict2)}
            else:
                newValue = {mapNode: findWeight(node, mapNode, dict1, dict2)}
                newDict[node].update(newValue)
    return newDict
