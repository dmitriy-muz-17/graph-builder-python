# these functions draw an edge between two clicked on nodes

def mapEdges(edge1, edge2, dict):
    # maps edge 1 to edge 2 and vice versa
    if edge1 not in dict:
        dict[edge1] = [edge2]
    else:
        dict[edge1].append(edge2)
    if edge2 not in dict:
        dict[edge2] = [edge1]
    else:
        dict[edge2].append(edge1)
        
def countMaps(dict):
    # returns total number of values in dict
    numMaps = 0
    for key in dict:
        for value in dict[key]:
            numMaps += 1
    return numMaps
    
def createEdge(dict, data):
    mapEdges((data.edges[0][0], data.edges[0][1]), \
        (data.edges[1][0], data.edges[1][1]), dict)
    data.allEdges[data.nextEdge] = [(data.edges[0][0], \
        data.edges[0][1]),(data.edges[1][0], \
        data.edges[1][1]),None]
    data.numEdges += 1
    data.nextEdge += 1
    data.edges = [ ]
    
def mousePressedEdge(event, data): 
    # create edge between two nodes and highlight node you clicked on
    for node in data.nodes:
        (x, y) = (data.nodes[node][0], data.nodes[node][1])
        if ((x-data.nodeR) <= event.x <= (x+data.nodeR)) and \
            (y-data.nodeR) <= event.y <= (y+data.nodeR):
            data.edges.append([x,y])
            data.highlight.append((x,y,data.nodeR))
            if (len(data.edges) == 2) and ((data.edges[0][0], \
                data.edges[0][1])== (data.edges[1][0], data.edges[1][1])):
                data.edges = [ ]
            else:
                if data.build.mode == "red edge" and len(data.edges) == 2:
                    createEdge(data.redEdges, data)
                elif data.build.mode == "blue edge" and len(data.edges) == 2:
                    createEdge(data.blueEdges, data)
    if len(data.highlight) == 2:
        data.highlight = [ ]
