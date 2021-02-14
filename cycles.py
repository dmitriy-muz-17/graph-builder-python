from visualDFS import *
from convertNodes import *

# Hamilton Cycles

class Hamilton(object): 
    def __init__(self, data):
        self.mode = None
        self.graph = None
        self.visited = [ ]
        self.edges = [ ]
        self.start = None
        self.choose = False

    def hamiltonMoves(self, graph, current, visited, data):
        # returns list of possible moves from a given node
        moves = [ ]
        for node in graph[current]:
            nodeCoord = convertToCoord(node, data)
            coord = convertToCoord(current, data)
            if node not in visited:
                if edgeInDict(coord[0], coord[1], \
                    nodeCoord[0], nodeCoord[1], data.allEdges):
                        moves.append(node)
        return moves
        
    def hamilton(self,graph,start,data,current=None,visited=None,edges=None):
        # backtracking function to find a hamilton cycle
        if current == None:
            current = start
        if visited == None:
            visited = [ ]
            visited.append(start)
        if edges == None:
            edges = [ ]
        if len(visited) == len(data.nodes) or len(visited)== len(data.nodes)+1:
            currentCoord = convertToCoord(current, data)
            startCoord = convertToCoord(start, data)
            # check if final vertex visited can connect back to start
            if edgeInDict(currentCoord[0], currentCoord[1], startCoord[0], \
                startCoord[1], data.allEdges):
                edges.append((current, start))
                return (visited, edges)
            else:
                return None
        for move in Hamilton.hamiltonMoves(self, graph, current, visited,data):
            visited.append(move)
            edges.append((current, move))
            newCurrent = move
            tempSol = Hamilton.hamilton(self,graph,start,data,newCurrent,\
                visited,edges)
            if tempSol != None:
                return tempSol
            # undo move
            visited.pop()
            edges.pop()
            newCurrent = current
        return None
        
    def mousePressedHamilton(self, event, data):
        rx = 80
        ry = 20
        if (data.width//8-rx) <= event.x <= (data.width//8+rx):
            if (data.height//8+(data.height*6)//10-ry) <= event.y <= \
                (data.height//8+(data.height*6)//10+ry):
                data.build.mode = "hamilton"
                
    def convertToCoord(self, num, data):
        for node in data.nodes:
            if num == node:
                return (data.nodes[node][0], data.nodes[node][1])
                
    def chooseStartNode(self, event, data):
        if data.build.mode == "hamilton" and self.start == None:
            self.choose = True
            for node in data.nodes:
                (x, y) = (data.nodes[node][0], data.nodes[node][1])
                if ((x-data.nodeR) <= event.x <= (x+data.nodeR)) and \
                    (y-data.nodeR) <= event.y <= (y+data.nodeR):
                    self.start = node
                    self.choose = False
                
    def drawHamilton(self, canvas, data):
        if data.build.mode == "hamilton" and self.choose == True:
            canvas.create_text(data.width//2, data.height//5-data.height//20, 
                text = "Choose a starting vertex")
        if data.build.mode == "hamilton" and Hamilton.hamilton != None and \
            self.choose == False:
            nodeMap = mapNodes(data.allEdges)
            self.graph = convertToNode(nodeMap, data.nodes)
            if Hamilton.hamilton(self, self.graph, self.start, data) == None:
                canvas.create_text(data.width//2, data.height//5-data.height//20, 
                    text = "No cycle!")
            else:
                (self.visited, self.edges)= Hamilton.hamilton(self, \
                    self.graph, self.start, data)
                for node in self.visited:
                    nodeR = data.build.bigNodeR
                    (nodeX, nodeY) = Hamilton.convertToCoord(self, node, data)
                    canvas.create_oval(nodeX-nodeR, nodeY-nodeR, nodeX+nodeR,
                        nodeY+nodeR, fill = "yellow")
                for edge in self.edges:
                    startPoint = Hamilton.convertToCoord(self, edge[0], data)
                    endPoint = Hamilton.convertToCoord(self, edge[1], data)
                    canvas.create_line(startPoint, endPoint, fill = "yellow",
                        width = 7)
            
 