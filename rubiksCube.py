import render3D
import math
camera = render3D._3D(500)

class rubiksCube:
    def __init__(self,x,y,z):
        self.cubes = []
        self.x = x
        self.y = y
        self.z = z
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    self.cubes.append(camera.returnCube((x-1)*100,(y-1)*100,(z-1)*100,20))
        for i in self.cubes:
            i = camera.project(i)

    def rotateAroundCubeX(self,angle):
        sin = math.sin(angle)
        cos = math.cos(angle)
        y = camera.camPos[1]
        z = camera.camPos[2]
        camera.camPos[1] = (y*cos)-(z*sin)
        camera.camPos[2] = (z*cos)+(y*sin)

    def rotateAroundCubeY(self,angle):
        sin = math.sin(angle)
        cos = math.cos(angle)
        x = camera.camPos[0]
        z = camera.camPos[2]
        camera.camPos[0] = (x*cos)+(z*sin)
        camera.camPos[2] = (z*cos)-(x*sin)
        #camera.camRot[1] += angle
    def rotateAroundCubeZ(self,angle):
        sin = math.sin(angle)
        cos = math.cos(angle)
        x = camera.camPos[0]
        y = camera.camPos[1]
        camera.camPos[0] = (x*cos)-(y*sin)
        camera.camPos[1] = (y*cos)+(x*sin)
    def rotateX(self,angle):
        sin = math.sin(angle)
        cos = math.cos(angle)
        for i in self.cubes:
            for l in i:
                l[1] = (l[1]*cos)+(l[2]*sin)
                l[2] = (l[2]*cos)-(l[1]*sin)
    def rotateY(self,angle):
        sin = math.sin(angle)
        cos = math.cos(angle)
        for i in self.cubes:
            for l in i:
                l[0] = (l[0]*cos)+(l[2]*sin)
                l[2] = (l[2]*cos)-(l[0]*sin)
    def rotateZ(self,angle):
        sin = math.sin(angle)
        cos = math.cos(angle)
        for i in self.cubes:
            for l in i:
                l[1] = (l[1]*cos)+(l[0]*sin)
                l[0] = (l[0]*cos)-(l[1]*sin)
    def rotateSide(self,side,angle):
        if side == 1:
            list = []
            for z in self.cubes:
                if z[0][2] < 0:
                    list.append(z)
            for l in list:
                for z in list:
                    if not z is l and z[0][1] == l[0][1] and z[0][0] == l[0][0]:
                        if l > z:
                            del(l)
            for z in list:
                for i in z:
                    sin = math.sin(angle)
                    cos = math.cos(angle)
                    i[0]=(i[0]*cos)-(i[1]*sin)
                    i[1]=(i[1]*cos)+(i[0]*sin)
                    dist=z[0][2]-i[2]
                    i[2]=-100-dist
        elif side == 2:
            for z in self.cubes:
                if z[0][2] > 0:
                    for i in z:
                        sin = math.sin(angle)
                        cos = math.cos(angle)
                        i[0]=(i[0]*cos)-(i[1]*sin)
                        i[1]=(i[1]*cos)+(i[0]*sin)
                        dist=z[0][2]-i[2]
                        i[2]=100-dist
        elif side == 3:
            for z in self.cubes:
                if z[0][1] > 0:
                    for i in z:
                        sin = math.sin(angle)
                        cos = math.cos(angle)
                        i[0]=(i[0]*cos)-(i[2]*sin)
                        i[2]=(i[2]*cos)+(i[0]*sin)
                        dist=z[0][1]-i[1]
                        i[1]=100-dist
        elif side == 4:
            pass
        elif side == 5:
            pass
        elif side == 6:
            pass

    def render(self):
        camera.clearScreen()
        for i in camera.visible(self.cubes):
            i = camera.project(i)
            face = camera.visibleFace(i)
            camera.draw_faces(i,face)
        camera.updateScreen()


cube = rubiksCube(0,0,0)
cube.render()
#camera.camRot[1] = math.pi
angle = 0
originalCube = list(cube.cubes[:])
print(originalCube is cube.cubes)
while camera.start:
    cube.rotateSide(1,math.pi/180)
    cube.rotateSide(3,math.pi/180)
    angle += 1
    print(originalCube is cube.cubes)
    #if angle%360 == 0:
    for i in range(len(originalCube)-1):
        for l in range(len(originalCube[i])-1):
            for z in range(len(originalCube[i][l])-1):
                print(originalCube[i][l][z] == cube.cubes[i][l][z])
                print(originalCube[i][l][z] is cube.cubes[i][l][z])
    if 'Escape' in camera.keysPressed:
        camera.start = False
    if 'w' in camera.keysPressed:
        camera.camPos[2] -= 10
    if 's' in camera.keysPressed:
        camera.camPos[2] += 10
    if 'j' in camera.keysPressed:
        cube.rotateSide(1,math.pi/90)
    if 'k' in camera.keysPressed:
        cube.rotateSide(2,math.pi/90)
    if 'h' in camera.keysPressed:
        cube.rotateSide(3,math.pi/90)
    if 'Up' in camera.keysPressed:
        cube.rotateX(math.pi/180)
    if 'Down' in camera.keysPressed:
        cube.rotateX(-math.pi/180)
    if 'Left' in camera.keysPressed:
        cube.rotateY(math.pi/180)
    if 'Right' in camera.keysPressed:
        cube.rotateY(-math.pi/180)
    cube.render()