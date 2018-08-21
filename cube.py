class Faces(object):
    UP = (4,1)
    LEFT = (1,4)
    FRONT = (4,4)
    RIGHT = (7,4)
    DOWN = (4,7)
    BACK = (10,4)
class Cube(Faces):
    def __init__(self, cube):
        self.cube = cube
        self.height = len(cube)
        self.width = len(cube[0])

    def _shift_right(self, arr):
        return arr[-1:] + arr[:-1]

    def _shift_left(self, arr):
        return arr[1:] + arr[:1]

    def _set_face(self, center, shifted):
        count = 0
        x,y = (i - 1 for i in center)
        for i in range(2):
            self.cube[y][x] = shifted[count]
            count += 1
            x += 1
        for i in range(2):
            self.cube[y][x] = shifted[count]
            count += 1
            y += 1
        for i in range(2):
            self.cube[y][x] = shifted[count]
            count += 1
            x -= 1
        for i in range(2):
            self.cube[y][x] = shifted[count]
            count += 1
            y -= 1

    def _set_f_edge(self, center, shifted):
        count = 0
        x,y = (i - 2 for i in center)
        x += 1
        for i in range(3):
            self.cube[y][x] = shifted[count]
            count += 1
            x += 1
        y += 1
        for i in range(3):
            self.cube[y][x] = shifted[count]
            count += 1
            y += 1
        x -= 1
        for i in range(3):
            self.cube[y][x] = shifted[count]
            count += 1
            x -= 1
        y -= 1
        for i in range(3):
            self.cube[y][x] = shifted[count]
            count += 1
            y -= 1

    def _set_b_edge(self, center, shifted):
        count = 0
        x,y = 3,0
        for i in range(3):
            self.cube[y][x] = shifted[count]
            count += 1
            x += 1
        x,y = 8,3
        for i in range(3):
            self.cube[y][x] = shifted[count]
            count += 1
            y += 1
        x,y = 5,8
        for i in range(3):
            self.cube[y][x] = shifted[count]
            count += 1
            x -= 1
        x,y = 0,5
        for i in range(3):
            self.cube[y][x] = shifted[count]
            count += 1
            y -= 1

    def _get_face(self, center):
        x,y = (i - 1 for i in center)
        face = []
        for i in range(2):
            face.append(self.cube[y][x])
            # face.append((x,y))
            x += 1
        for i in range(2):
            face.append(self.cube[y][x])
            # face.append((x,y))
            y += 1
        for i in range(2):
            face.append(self.cube[y][x])
            # face.append((x,y))
            x -= 1
        for i in range(2):
            face.append(self.cube[y][x])
            # face.append((x,y))
            y -= 1
        return face

    def _get_f_edge(self, center):
        x,y = (i - 2 for i in center)
        face = []
        x += 1
        for i in range(3):
            face.append(self.cube[y][x])
            x += 1
        y += 1
        for i in range(3):
            face.append(self.cube[y][x])
            y += 1
        x -= 1
        for i in range(3):
            face.append(self.cube[y][x])
            x -= 1
        y -= 1
        for i in range(3):
            face.append(self.cube[y][x])
            y -= 1
        return face

    def _get_b_edge(self, center):
        x,y = 3,0
        face = []
        for i in range(3):
            face.append(self.cube[y][x])
            x += 1
        x,y = 8,3
        for i in range(3):
            face.append(self.cube[y][x])
            y += 1
        x,y = 5,8
        for i in range(3):
            face.append(self.cube[y][x])
            x -= 1
        x,y = 0,5
        for i in range(3):
            face.append(self.cube[y][x])
            y -= 1
        return face
    def turn_u(self):
        # top face
        faceList = self._get_face(Faces.UP)
        faceList = self._shift_right(self._shift_right(faceList))
        self._set_face(Faces.UP, faceList)
        # side face
        sideList = [self.cube[3][i] for i in range(self.width)]
        sideList = self._shift_left(self._shift_left(self._shift_left(sideList)))
        for i, side in enumerate(sideList):
            self.cube[3][i] = side

    def turn_u_prime(self):
        # top face
        faceList = self._get_face(Faces.UP)
        faceList = self._shift_left(self._shift_left(faceList))
        self._set_face(Faces.UP, faceList)
        # side face
        sideList = [self.cube[3][i] for i in range(self.width)]
        sideList = self._shift_right(self._shift_right(self._shift_right(sideList)))
        for i, side in enumerate(sideList):
            self.cube[3][i] = side

    def turn_d(self):
        # top face
        faceList = self._get_face(Faces.DOWN)
        faceList = self._shift_right(self._shift_right(faceList))
        self._set_face(Faces.DOWN, faceList)
        # side face
        sideList = [self.cube[5][i] for i in range(self.width)]
        sideList = self._shift_right(self._shift_right(self._shift_right(sideList)))
        for i, side in enumerate(sideList):
            self.cube[5][i] = side

    def turn_d_prime(self):
        # top face
        faceList = self._get_face(Faces.DOWN)
        faceList = self._shift_left(self._shift_left(faceList))
        self._set_face(Faces.DOWN, faceList)
        # side face
        sideList = [self.cube[5][i] for i in range(self.width)]
        sideList = self._shift_left(self._shift_left(self._shift_left(sideList)))
        for i, side in enumerate(sideList):
            self.cube[5][i] = side

    def turn_f(self):
        # top face
        faceList = self._get_face(Faces.FRONT)
        faceList = self._shift_right(self._shift_right(faceList))
        self._set_face(Faces.FRONT, faceList)
        # side face
        sideList = self._get_f_edge(Faces.FRONT)
        sideList = self._shift_right(self._shift_right(self._shift_right(sideList)))
        self._set_f_edge(Faces.FRONT, sideList)

    def turn_f_prime(self):
        # top face
        faceList = self._get_face(Faces.FRONT)
        faceList = self._shift_left(self._shift_left(faceList))
        self._set_face(Faces.FRONT, faceList)
        # side face
        sideList = self._get_f_edge(Faces.FRONT)
        sideList = self._shift_left(self._shift_left(self._shift_left(sideList)))
        self._set_f_edge(Faces.FRONT, sideList)

    def turn_r(self):
        # top face
        faceList = self._get_face(Faces.RIGHT)
        faceList = self._shift_right(self._shift_right(faceList))
        self._set_face(Faces.RIGHT, faceList)
        # side face
        sideList = [self.cube[i][5] for i in range(self.height)]
        sideList += [self.cube[self.height - 3 - i - 1][9] for i in range(3)]
        sideList = self._shift_left(self._shift_left(self._shift_left(sideList)))
        for i, side in enumerate(sideList[:-3]):
            self.cube[i][5] = side
        for i, side in enumerate(sideList[-3:]):
            self.cube[self.height - 3 - i - 1][9] = side

    def turn_r_prime(self):
        # top face
        faceList = self._get_face(Faces.RIGHT)
        faceList = self._shift_left(self._shift_left(faceList))
        self._set_face(Faces.RIGHT, faceList)
        # side face
        sideList = [self.cube[i][5] for i in range(self.height)]
        sideList += [self.cube[self.height - 3 - i - 1][9] for i in range(3)]
        sideList = self._shift_right(self._shift_right(self._shift_right(sideList)))
        for i, side in enumerate(sideList[:-3]):
            self.cube[i][5] = side
        for i, side in enumerate(sideList[-3:]):
            self.cube[self.height - 3 - i - 1][9] = side

    def turn_l(self):
        # top face
        faceList = self._get_face(Faces.LEFT)
        faceList = self._shift_right(self._shift_right(faceList))
        self._set_face(Faces.LEFT, faceList)
        # side face
        sideList = [self.cube[i][3] for i in range(self.height)]
        sideList += [self.cube[self.height - 3 - i - 1][11] for i in range(3)]
        sideList = self._shift_right(self._shift_right(self._shift_right(sideList)))
        for i, side in enumerate(sideList[:-3]):
            self.cube[i][3] = side
        for i, side in enumerate(sideList[-3:]):
            self.cube[self.height - 3 - i - 1][11] = side

    def turn_l_prime(self):
        # top face
        faceList = self._get_face(Faces.LEFT)
        faceList = self._shift_left(self._shift_left(faceList))
        self._set_face(Faces.LEFT, faceList)
        # side face
        sideList = [self.cube[i][3] for i in range(self.height)]
        sideList += [self.cube[self.height - 3 - i - 1][11] for i in range(3)]
        sideList = self._shift_left(self._shift_left(self._shift_left(sideList)))
        for i, side in enumerate(sideList[:-3]):
            self.cube[i][3] = side
        for i, side in enumerate(sideList[-3:]):
            self.cube[self.height - 3 - i - 1][11] = side

    def turn_b(self):
        # top face
        faceList = self._get_face(Faces.BACK)
        faceList = self._shift_right(self._shift_right(faceList))
        self._set_face(Faces.BACK, faceList)
        # side face
        sideList = self._get_b_edge(Faces.BACK)
        sideList = self._shift_left(self._shift_left(self._shift_left(sideList)))
        self._set_b_edge(Faces.BACK, sideList)

    def turn_b_prime(self):
        # top face
        faceList = self._get_face(Faces.BACK)
        faceList = self._shift_left(self._shift_left(faceList))
        self._set_face(Faces.BACK, faceList)
        # side face
        sideList = self._get_b_edge(Faces.BACK)
        sideList = self._shift_right(self._shift_right(self._shift_right(sideList)))
        self._set_b_edge(Faces.BACK, sideList)


    def get_cube(self):
        # return self.cube
        return "\n".join(map(str,self.cube))

if __name__ == '__main__':
    # testCube = Cube([
    #     [' ',' ',' ','w','w','w',' ',' ',' '],
    #     [' ',' ',' ','w','w','w',' ',' ',' '],
    #     [' ',' ',' ','w','w','w',' ',' ',' '],
    #     ['o','o','o','g','g','g','r','r','r'],
    #     ['o','o','o','g','g','g','r','r','r'],
    #     ['o','o','o','g','g','g','r','r','r'],
    #     [' ',' ',' ','y','y','y',' ',' ',' '],
    #     [' ',' ',' ','y','y','y',' ',' ',' '],
    #     [' ',' ',' ','y','y','y',' ',' ',' '],
    #     [' ',' ',' ','b','b','b',' ',' ',' '],
    #     [' ',' ',' ','b','b','b',' ',' ',' '],
    #     [' ',' ',' ','b','b','b',' ',' ',' ']
    #     ])
    testCube = Cube([
        [' ',' ',' ','w','w','w',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ','w','w','w',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ','w','w','w',' ',' ',' ',' ',' ',' '],
        ['o','o','o','g','g','g','r','r','r','b','b','b'],
        ['o','o','o','g','g','g','r','r','r','b','b','b'],
        ['o','o','o','g','g','g','r','r','r','b','b','b'],
        [' ',' ',' ','y','y','y',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ','y','y','y',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ','y','y','y',' ',' ',' ',' ',' ',' ']
        ])
    print(testCube.get_cube())
    print()
    # testCube.turn_u()
    # print(testCube.get_cube())
    # testCube.turn_u_prime()
    # print(testCube.get_cube())
    # testCube.turn_d()
    # print(testCube.get_cube())
    # testCube.turn_d_prime()
    # print(testCube.get_cube())
    # testCube.turn_f()
    # print(testCube.get_cube())
    # testCube.turn_f_prime()
    # print(testCube.get_cube())
    # testCube.turn_r()
    # print(testCube.get_cube())
    # testCube.turn_r_prime()
    # print(testCube.get_cube())
    # testCube.turn_l()
    # print(testCube.get_cube())
    # testCube.turn_l_prime()
    # print(testCube.get_cube())
    # testCube.turn_b()
    # print(testCube.get_cube())
    testCube.turn_b_prime()
    print(testCube.get_cube())