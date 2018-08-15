class Faces(object):
    WHITE = (4,1)
    ORANGE = (1,4)
    GREEN = (4,4)
    RED = (7,4)
    YELLOW = (4,7)
    BLUE = (10,4)
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

    def turn_u(self):
        # top face
        faceList = self._get_face(Faces.WHITE)
        faceList = self._shift_right(self._shift_right(faceList))
        self._set_face(Faces.WHITE, faceList)
        # side face
        sideList = [self.cube[3][i] for i in range(self.width)]
        sideList = self._shift_left(self._shift_left(self._shift_left(sideList)))
        for i, side in enumerate(sideList):
            self.cube[3][i] = side

    def turn_u_prime(self):
        # top face
        faceList = self._get_face(Faces.WHITE)
        faceList = self._shift_left(self._shift_left(faceList))
        self._set_face(Faces.WHITE, faceList)
        # side face
        sideList = [self.cube[3][i] for i in range(self.width)]
        sideList = self._shift_right(self._shift_right(self._shift_right(sideList)))
        for i, side in enumerate(sideList):
            self.cube[3][i] = side

    def turn_d(self):
        # top face
        faceList = self._get_face(Faces.YELLOW)
        faceList = self._shift_right(self._shift_right(faceList))
        self._set_face(Faces.YELLOW, faceList)
        # side face
        sideList = [self.cube[5][i] for i in range(self.width)]
        sideList = self._shift_right(self._shift_right(self._shift_right(sideList)))
        for i, side in enumerate(sideList):
            self.cube[5][i] = side

    def turn_d_prime(self):
        # top face
        faceList = self._get_face(Faces.YELLOW)
        faceList = self._shift_left(self._shift_left(faceList))
        self._set_face(Faces.YELLOW, faceList)
        # side face
        sideList = [self.cube[5][i] for i in range(self.width)]
        sideList = self._shift_left(self._shift_left(self._shift_left(sideList)))
        for i, side in enumerate(sideList):
            self.cube[5][i] = side

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
    testCube.turn_u()
    print(testCube.get_cube())
    print("")
    testCube.turn_u_prime()
    print(testCube.get_cube())
    print("")
    testCube.turn_d()
    print(testCube.get_cube())
    print("")
    testCube.turn_d_prime()
    print(testCube.get_cube())