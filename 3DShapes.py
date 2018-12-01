try:
    from Tkinter import *
except:
    from tkinter import *
import random
import math

root = Tk()
canvas = Canvas(root,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
canvas.pack()

class _3D:
    def __init__(self,fl):
        self.fl = fl
        self.radius = 1000
        self.centerZ = 1000
        self.mouseX = 0
        self.mouseY = 0
        root.bind('<Motion>',self.mouseSet)
    def mouseSet(self,event):
        self.mouseX = event.x
        self.mouseY = event.y
    def zsort(self,num,smallest=False):
        olen = len(num)

        ans = []

        added = False

        if smallest:
            i = 0
            while len(num) > 0:
                added = False
                if len(num) == olen:
                    ans.append(num[0])
                    num.remove(num[0])
                    added = True
                elif num[0][2] < ans[0][2]:
                    ans.insert(0,num[0])
                    num.remove(num[0])
                    added = True
                else:
                    i = 0
                    while i < len(ans):
                        if num[0][2] < ans[i][2]:
                            ans.insert(i,num[0])
                            num.remove(num[0])
                            added = True
                            break
                        i += 1

                if not added:
                    ans.append(num[0])
                    num.remove(num[0])
        else:
            i = 0
            while len(num) > 0:
                added = False
                if len(num) == olen:
                    ans.append(num[0])
                    num.remove(num[0])
                    added = True
                elif num[0][2] > ans[0][2]:
                    ans.insert(0,num[0])
                    num.remove(num[0])
                    added = True
                else:
                    i = 0
                    while i < len(ans):
                        if num[0][2] > ans[i][2]:
                            ans.insert(i,num[0])
                            num.remove(num[0])
                            added = True
                            break
                        i += 1

                if not added:
                    ans.append(num[0])
                    num.remove(num[0])
        return ans

    def perspectify(self,shape,color='black',xRad=2,yRad=2):
        perspective = self.fl/(self.fl+shape[2])
        radiusX = xRad * perspective
        radiusY = yRad * perspective
        shapeMod = [shape[0]*perspective + root.winfo_screenwidth()/2,shape[1]*perspective+root.winfo_screenheight()/2]
        #canvas.create_oval(shapeMod[0]-radiusX,shapeMod[1]-radiusY,shapeMod[0]+radiusX,shapeMod[1]+radiusY,fill = color)
        return shapeMod
    def project(self,points):
        for i in range(len(points)-1):
            p = points[i]
            scale = self.fl/(self.fl + p[2])
            p[3] = p[0] * scale + root.winfo_screenwidth()/2
            p[4] = p[1] * scale + root.winfo_screenheight()/2
        return points
    def drawLines(self,points,indexes):
        for i in range(len(indexes)-2):
            p = points[indexes[i]]
            nextP = points[indexes[i+1]]
            canvas.create_line(p[3],p[4],nextP[3],nextP[4])


_3d = _3D(300)

points = []
points.append([-500,-500,1000,0,0])
points.append([500,-500,1000,0,0])
points.append([500,-500,500,0,0])
points.append([-500,-500,500,0,0])
points.append([-500,500,1000,0,0])
points.append([500,500,1000,0,0])
points.append([500,500,500,0,0])
points.append([-500,500,500,0,0])

rotationSpeed = 1
baseAngle = 0

points = _3d.project(points)
while   True:
    for i in points:
        canvas.create_rectangle(i[3]-5,i[4]-5,i[3]+5,i[3]+5,fill = 'black')
    canvas.delete(ALL)

    points = _3d.project(points)

    '''_3d.drawLines(points,[0,1,2,3,0])
    _3d.drawLines(points,[4,5,6,7,4])
    _3d.drawLines(points,[0,4])
    _3d.drawLines(points,[1,5])
    _3d.drawLines(points,[2,6])
    _3d.drawLines(points,[3,7])'''

    root.update()