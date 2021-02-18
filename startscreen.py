class Startscreen(object):
    def __init__(self, data):
        self.buildX = (data.width*3)//4-data.width//20
        self.cy = data.height//2+data.height//10
        self.rx = data.width//6
        self.ry = data.height//18

    def draw(self, canvas, data):
        canvas.create_text(data.width//2, data.height//5+data.height//20, 
            text = "GRAPH", anchor = "s", font = "Georgia 100")
        canvas.create_text(data.width//2, (data.height*2)//5+data.height//20, 
            text = "BUILDER", anchor = "s", font = "Georgia 100")
        canvas.create_rectangle(data.width//2-self.rx, 
            (data.height*2)//3-self.ry, data.width//2+self.rx,
            (data.height*2)//3+self.ry, fill = "azure1")
        canvas.create_text(data.width//2, (data.height*2)//3, text = "Start",
            font = "Georgia 30")
            
def mousePressedStart(event, data):
    if (data.width//2-data.startscreen.rx) <= event.x <= \
        (data.width//2+data.startscreen.rx):
        if ((data.height*2)//3-data.startscreen.ry) <= event.y <= \
            ((data.height*2)//3+data.startscreen.ry):
                data.mode = "build"
                    
