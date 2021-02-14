import copy
import math
# from checkRamsey import *
from convertNodes import *
from dfs import *
from removeEdges import *
from createEdges import *
from visualDFS import *
from visualBFS import *
from cycles import *
from dijkstra import *

class Build(object):
    def __init__(self, data):
        self.eraseX = (data.width*9)//10+data.width//50
        self.nodeR = data.width//80
        self.mode = "eraser"
        self.nodeX = data.width//2-data.width//8+data.width//25
        self.bigNodeR = data.width//60
        self.edgeX = data.width//2
        self.redEdgeY = data.height//20-data.height//30
        self.blueEdgeY = data.height//20+data.height//30
        self.edgeR = data.width//25
        self.eraserX = data.width//2+data.width//8-data.width//25
        self.eraserR = data.width//60
        # dimensions for highlighting the tool
        self.lightNode = self.bigNodeR+5
        self.lightEdge = self.edgeR+5
        self.lightEraser = self.eraserR+5
        self.grid = False
        self.checkboxX = data.width//2-data.width//25
        self.checkboxR = 10
        self.displayWeights = False
        self.enterWeight = False
        self.dfsBoxR = data.width//20
        
    def clearAll(data): # resets everything
        data.numNodes = 0
        data.nextNode = 0
        data.nodes = dict()
        data.degrees = dict()
        data.edges = [ ]
        data.redEdges = dict()
        data.blueEdges = dict()
        data.highlight = [ ]
        data.removedRedEdges = dict()
        data.removedBlueEdges = dict()
        data.allEdges = dict()
        data.build.mode = "eraser"
        data.hamilton.__init__(data)
        Hamilton.mode = None
        
    def drawBackButton(canvas, data):
        canvas.create_rectangle(data.backX-data.backRX, data.backY-data.backRY,
            data.backX+data.backRX, data.backY+data.backRY, outline = "black",
            fill = "azure1")
        canvas.create_text(data.backX, data.backY, text = "Back", 
            anchor = "center", font = "Georgia 25")
            
    def drawEraseButton(canvas, data):
        canvas.create_rectangle(data.build.eraseX-data.backRX, 
            data.backY-data.backRY, data.build.eraseX+data.backRX, 
            data.backY+data.backRY, outline = "black", fill = "azure1")
        canvas.create_text(data.build.eraseX, data.backY, text = "Erase All", 
            anchor = "center", font = "Georgia 23")
            
    def drawResetButton(canvas, data):
        canvas.create_rectangle(data.build.eraseX-data.backRX,
            data.height-data.backY-data.backRY+10, data.build.eraseX+data.backRX,
            data.height-data.backY+data.backRY+10, outline = "black", 
            fill = "azure1")
        canvas.create_text(data.build.eraseX, data.height-data.backY+10,
            text = "Reset", anchor = "center", font = "Georgia 28")
        
    def drawStatBox(canvas, data):
        canvas.create_rectangle(0, data.height//8+data.height//20, 
            data.width//4, (data.height*7)//8+data.height//20, fill = "azure1")
        if data.numNodes == 0:
            canvas.create_text(data.width//8, data.height//8+data.height//10,
            text = "Nodes: 0", font = "Georgia 20")
        elif data.numNodes > 0:
            canvas.create_text(data.width//8, data.height//8+data.height//10,
                text = "Nodes: "+str(data.numNodes), font = "Georgia 20")
        canvas.create_text(data.width//8, data.height//8+data.height//5,
            text = "Red edges: "+str((countMaps(data.redEdges))//2), 
            font = "Georgia 20")
        canvas.create_text(data.width//8, data.height//8+(data.height*3)//10,
            text = "Blue edges: "+str((countMaps(data.blueEdges))//2), 
            font = "Georgia 20") 
            
    def highlightTool(canvas, data):
        if data.build.mode == "node":
            canvas.create_oval(data.build.nodeX-data.build.lightNode, 
                data.backY-data.build.lightNode,
                data.build.nodeX+data.build.lightNode,
                data.backY+data.build.lightNode, fill = "yellow")
                
        elif data.build.mode == "red edge":
            canvas.create_line(data.build.edgeX-data.build.lightEdge, 
                data.backY-data.backRY//2, 
                data.build.edgeX+data.build.lightEdge,
                data.backY-data.backRY//2, fill = "yellow",width = 10)
                
        elif data.build.mode == "blue edge":
            canvas.create_line(data.build.edgeX-data.build.lightEdge, 
                data.backY+data.backRY//2, 
                data.build.edgeX+data.build.lightEdge,
                data.backY+data.backRY//2, fill = "yellow", width = 10)
                
        elif data.build.mode == "eraser":
            canvas.create_rectangle(data.build.eraserX-data.build.lightEraser, 
                data.backY-data.build.lightEraser, 
                data.build.eraserX+data.build.lightEraser, 
                data.backY+data.build.lightEraser, fill = "yellow")
                
    def drawOptions(canvas, data):
        # grid option
        canvas.create_text(data.width//2-data.width//15, 2*data.backY, 
            text = "Grid", font = "Georgia 16")
        canvas.create_rectangle(data.build.checkboxX-data.build.checkboxR- \
            data.width//15, 2*data.backY-data.build.checkboxR, 
            data.build.checkboxX+data.build.checkboxR-data.width//15,
            2*data.backY+data.build.checkboxR)
        # edge weights option
        canvas.create_text(data.width//2+data.width//15, 2*data.backY,
            text = "Edge Weights", font = "Georgia 16")
        canvas.create_rectangle(data.build.checkboxX-data.build.checkboxR+\
            data.width//35, 2*data.backY-data.build.checkboxR, 
            data.build.checkboxX+data.build.checkboxR+data.width//35,
            2*data.backY+data.build.checkboxR)
        
    def drawTools(canvas, data):
        # node
        canvas.create_oval(data.build.nodeX-data.build.bigNodeR, 
            data.backY-data.build.bigNodeR,
            data.build.nodeX+data.build.bigNodeR, 
            data.backY+data.build.bigNodeR, fill = "black")
        # red edge
        canvas.create_line(data.build.edgeX-data.build.edgeR, 
            data.backY-data.backRY//2, 
            data.build.edgeX+data.build.edgeR, 
            data.backY-data.backRY//2, fill = "red", width = 5)
        # blue edge    
        canvas.create_line(data.build.edgeX-data.build.edgeR, 
            data.backY+data.backRY//2,
            data.build.edgeX+data.build.edgeR, 
            data.backY+data.backRY//2, fill = "blue", width = 5)
        # eraser
        canvas.create_rectangle(data.build.eraserX-data.build.eraserR, 
            data.backY-data.build.eraserR, 
            data.build.eraserX+data.build.eraserR, 
            data.backY+data.build.eraserR, fill = "pink")
        
    def drawDFS(canvas, data):  # draws DFS button
        rx = 80
        ry = 20
        canvas.create_rectangle(data.width//8-rx,
            data.height//8+(data.height*4)//10-ry, 
            data.width//8+rx, data.height//8+(data.height*4)//10+ry)
        canvas.create_text(data.width//8, data.height//8+(data.height*4)//10,
            text = "DFS", font = "Georgia 20")
            
    def drawBFS(canvas, data): # draws BFS button
        rx = 80
        ry = 20
        canvas.create_rectangle(data.width//8-rx,
            data.height//8+(data.height*5)//10-ry, 
            data.width//8+rx, data.height//8+(data.height*5)//10+ry)
        canvas.create_text(data.width//8, data.height//8+(data.height*5)//10,
            text = "BFS", font = "Georgia 20")
            
    def drawHamilton(canvas, data): # draws Hamilton button
        rx = 80
        ry = 20
        canvas.create_rectangle(data.width//8-rx,
            data.height//8+(data.height*6)//10-ry, 
            data.width//8+rx, data.height//8+(data.height*6)//10+ry)
        canvas.create_text(data.width//8, data.height//8+(data.height*6)//10,
            text = "Hamilton", font = "Georgia 20")
            
    def drawDijkstra(canvas, data): # draws Dijkstra button
        rx = 80
        ry = 20
        canvas.create_rectangle(data.width//8-rx,
            data.height//8+(data.height*7)//10-ry, 
            data.width//8+rx, data.height//8+(data.height*7)//10+ry)
        canvas.create_text(data.width//8, data.height//8+(data.height*7)//10,
            text = "Dijkstra", font = "Georgia 20")
        
    def drawGrid(canvas, data):
        #draws grid
        dim = 50
        numCols = (data.width-data.width//4)//dim
        numRows = (data.height-(data.height//8+data.height//20))//dim
        for i in range(numCols):
            for j in range(numRows-1):
                canvas.create_rectangle(i*dim+data.width//4, 
                    j*dim+data.height//8+data.height//20, 
                    (i+1)*dim+data.width//4, 
                    (j+1)*dim+data.height//8+data.height//20)
                    
    def drawCheckmark(self, canvas, x, y, r, data):
        # checks box if grid is displayed
        width = 2*r
        height = 2*r
        p1 = (0+x-r, (height*2)//3+y-r)
        p2 = (width//3+x-r, height+y-r)
        p3 = (width+x-r, height//4-(height*0.5)//4+y-r)
        p4 = ((width*3.5)//4+x-r, 0+y-r)
        p5 = (width//3+x-r, (height*3)//4+y-r)
        p6 = (width//6+x-r, (height*3)//4 - height//4+y-r)
        canvas.create_polygon(p1, p2, p3, p4, p5, p6, fill = "green")

    def draw(self, canvas, data):
        # print (data.allEdges)
        canvas.create_rectangle(0,0,data.width, data.height, fill = "sky blue")
        Build.drawBackButton(canvas, data)
        Build.drawEraseButton(canvas, data)
        Build.drawStatBox(canvas, data)
        Build.highlightTool(canvas, data)
        Build.drawTools(canvas, data)
        Build.drawOptions(canvas, data)
        if data.build.grid == True:
            Build.drawGrid(canvas, data)
            Build.drawCheckmark(self,canvas, data.build.checkboxX-data.width//15, 
                2*data.backY, data.build.checkboxR, data)
        if data.build.displayWeights == True:
            Build.drawCheckmark(self,canvas, data.build.checkboxX+data.width//35,
                2*data.backY, data.build.checkboxR, data)
            
def mousePressedGrid(event, data): 
    if (data.build.checkboxX-data.build.checkboxR-data.width//15) <=event.x<= \
        (data.build.checkboxX+data.build.checkboxR-data.width//15):
        if (2*data.backY-data.build.checkboxR) <= event.y <= \
            (2*data.backY+data.build.checkboxR):
            data.build.grid = not (data.build.grid)
            
def mousePressedWeight(event, data):
    if (data.build.checkboxX-data.build.checkboxR+data.width//35) <=event.x<= \
        (data.build.checkboxX+data.build.checkboxR+data.width//35):
        if (2*data.backY-data.build.checkboxR) <= event.y <= \
            (2*data.backY+data.build.checkboxR):
            data.build.displayWeights = not (data.build.displayWeights)
            data.build.enterWeight = not (data.build.enterWeight)
        
def mousePressedToolbox(event, data): # selects current tool
    if (data.build.nodeX-data.build.bigNodeR) <= event.x <= \
        (data.build.nodeX+data.build.bigNodeR):
        if (data.backY-data.build.bigNodeR) <= event.y <= \
            (data.backY+data.build.bigNodeR):
            data.build.mode = "node"
    elif (data.build.edgeX-data.build.edgeR) <= event.x <= \
        (data.build.edgeX+data.build.edgeR):
        if (data.backY-data.backRY) <= event.y <= (data.backY):
            data.build.mode = "red edge"
    if (data.build.edgeX-data.build.edgeR) <= event.x <= \
        (data.build.edgeX+data.build.edgeR):
        if (data.backY) <= event.y <= (data.backY+data.backRY):
            data.build.mode = "blue edge"
    elif (data.build.eraserX-data.build.eraserR) <= event.x <= \
        (data.build.eraserX+data.build.eraserR):
        if (data.backY-data.build.bigNodeR) <= event.y <= \
            (data.backY+data.build.bigNodeR):
            data.build.mode = "eraser"
            
def mousePressedBack(event, data): # back button
    if (data.backX-data.backRX) <= event.x <= (data.backX+data.backRX):
        if (data.backY-data.backRY) <= event.y <= (data.backY+data.backRY):
            data.mode = "startScreen"
            data.build.mode = "eraser"
            Build.clearAll(data)
            
def mousePressedEraseAll(event, data): # erase all button
    if (data.build.eraseX-data.backRX) <= event.x <= \
        (data.build.eraseX+data.backRX):
        if (data.backY-data.backRY) <= event.y <= (data.backY+data.backRY):
            Build.clearAll(data)
            initDFS(data)
            initBFS(data)
            initDijkstra(data)
            
def mousePressedReset(event, data): # resets searching algorithms
    if (data.build.eraseX-data.backRX) <= event.x <= \
        (data.build.eraseX+data.backRX):
        if (data.height-data.backY-data.backRY) <= event.y <= \
            (data.height-data.backY+data.backRY):
            initDFS(data)
            initBFS(data)
            initDijkstra(data)
            data.hamilton.__init__(data)
            Hamilton.mode = None
            data.build.mode = "node"

def mousePressedNode(event, data): # create node where mouse clicks
    if data.width//4 < event.x < data.width:
        if data.height//8 < event.y-data.height//20 < (data.height*7)//8:
            # node number maps to x/y coordinate and degree
            data.nodes[data.nextNode] = [event.x, event.y, 0] 
            data.numNodes += 1
            data.nextNode += 1
            
def mousePressedDijkstra(event, data):
    rx = 80
    ry = 20
    if (data.width//8-rx) <=event.x<= (data.width//8+rx):
        if (data.height//8+(data.height*7)//10-ry) <= event.y <= \
            (data.height//8+(data.height*7)//10+ry):
                data.build.mode = "dijkstra"
    
def middle(x0, y0, x1, y1): #finds middle of a line given two endpoints
    middleX = (x0+x1)//2
    middleY = (y0+y1)//2
    return (middleX, middleY)
    
def clickInNode(event, data): # checks if you clicked on a node
    for node in data.nodes:
        (x, y) = (data.nodes[node][0], data.nodes[node][1])
        if (x-data.nodeR) <= event.x <= (x+data.nodeR):
            if (y-data.nodeR) <= event.y <= (y+data.nodeR):
                return True
    return False

def numDegrees(data, node):
    degrees = 0
    for edge in data.redEdges:
        if data.nodes[node][0] == edge[0] and \
            data.nodes[node][1] == edge[1]:
            for otherEnd in data.redEdges[edge]:
                degrees += 1
    for edge in data.blueEdges:
        if data.nodes[node][0] == edge[0] and \
            data.nodes[node][1] == edge[1]:
            for otherEnd in data.blueEdges[edge]:
                degrees += 1
    return degrees
    
def drawWeight(canvas, data):
    (rx, ry) = (10, 13)
    for edge in data.allEdges:
        if data.allEdges[edge][2] == None:
            (x0, y0) = data.allEdges[edge][0]
            (x1, y1) = data.allEdges[edge][1]
            (x, y) = middle(x0, y0, x1, y1)
            canvas.create_rectangle(x-rx, y-ry, x+rx, y+ry, fill = "white")
        
def findBox(event, data): # returns which edge you clicked on
    (rx, ry) = (10, 13)
    for edge in data.allEdges:
        (x0, y0) = data.allEdges[edge][0]
        (x1, y1) = data.allEdges[edge][1]
        (x, y) = middle(x0, y0, x1, y1)
        if ((x-rx) <= event.x <= (x+rx)) and ((y-ry) <= event.y <= (y+ry)):
            return edge
            
def keyPressedWeight(event, data):
    for edge in data.allEdges:
        if edge == findBox(event, data):
            if event.keysym.isdigit():
                if data.allEdges[edge][2] == None: 
                    data.allEdges[edge][2] = 0
                data.allEdges[edge][2] = \
                    data.allEdges[edge][2]*10+int(event.keysym)
            if event.keysym == "BackSpace" and data.allEdges[edge][2] != 0:
                data.allEdges[edge][2] = data.allEdges[edge][2] // 10
                
def mousePressedBuild(event, data):
    mousePressedBack(event, data)
    mousePressedEraseAll(event, data)
    mousePressedReset(event, data)
    mousePressedDijkstra(event, data)
    if data.build.mode == "node":
        mousePressedNode(event, data)
    if data.build.mode == "red edge" or data.build.mode == "blue edge":
        mousePressedEdge(event, data)
    if data.build.mode == "eraser":
        mousePressedEraseNode(event, data)
        eraseEdge(event, data)
    mousePressedToolbox(event, data)
    mousePressedGrid(event, data)
    mousePressedWeight(event, data)
    searchBFS(event, data)
    searchDFS(event, data)
    if data.build.mode == "searchBFS":
        mousePressedBFS(event, data)
    elif data.build.mode == "searchDFS":
        mousePressedDFS(event, data)
    elif data.build.mode == "dijkstra":
        setPoints(event, data)
    
    
def redrawEdges(dict1, dict2, color, canvas, data):
    for edge in dict1:
        if edge not in dict2:
            for otherEnd in dict1[edge]:
                canvas.create_line(edge, otherEnd, fill = color, 
                    width = 3)
                    
def redrawBuild(canvas, data): 
    redrawEdges(data.redEdges, data.removedRedEdges, "red", canvas, data)
    redrawEdges(data.blueEdges, data.removedBlueEdges, "blue", canvas, data)
    if data.build.mode == "searchDFS":
        drawDFS(canvas, data)
    elif data.build.mode == "searchBFS":
        drawBFS(canvas, data)
    if data.build.mode == "dijkstra":
        drawDijkstra(canvas, data)
    for node in data.highlight:
        (x,y,r) = node
        canvas.create_oval(x-(r+5), y-(r+5), x+(r+5), y+(r+5), fill = "yellow")
    for node in data.nodes:
        (x, y) = (data.nodes[node][0], data.nodes[node][1])
        canvas.create_oval(x-data.nodeR, y-data.nodeR, 
            x+data.nodeR, y+data.nodeR, fill = "black")
        # prints degree of node
        # canvas.create_text(x, y, anchor = "center", 
        #     text = str(node), fill = "white", font = "Georgia 16")
        # canvas.create_text(x, y, anchor = "center", 
        #     text = str(numDegrees(data, node)), fill = "white", 
        #     font = "Georgia 16")
    if data.build.displayWeights == True:
        drawWeight(canvas, data)
    for edge in data.allEdges:
        (x0, y0) = data.allEdges[edge][0]
        (x1, y1) = data.allEdges[edge][1]
        (mx, my) = middle(x0, y0, x1, y1)
        if data.allEdges[edge][2] != None:
            canvas.create_text(mx, my, text = str(data.allEdges[edge][2]), 
                font = "Georgia 18 bold")
