# solved cube: UF UR UB UL DF DR DB DL FR FL BR BL UFR URB UBL ULF DRF DFL DLB DBR
#              A  B  C  D  E  F  G  H  I  J  K  L  M   N   O   P   Q   R   S   T
#              0  1  2  3  4  5  6  7  8  9  10 11 12  13  14  15  16  17  18  19
# test cases http://tomas.rokicki.com/cubecontest/testdata.txt

# reduction of moves
# <L,R,F,B,U,D> → <L,R,F2,B2,U,D> → <L2,R2,F2,B2,U,D> → <L2,R2,F2,B2,U2,D2>

faces='FBRLUD'
order = 'ABCDEFGHIJKLMNOPQRST'
solved = 'UF UR UB UL DF DR DB DL FR FL BR BL UFR URB UBL ULF DRF DFL DLB DBR'.split()
orderDict = {sum(1<<faces.find(f) for f in v):i for i,v in enumerate(solved)}
S = [0]*20, order, 0

def getOrientation(state):
    orientation = []
    for piece in state:
        if len(piece) == 2:
            if piece[0] in 'RL' or piece[1] in 'UD':
                orientation.append(1)
            else:
                orientation.append(0)
        else:
            if piece[2] in 'UD':
                orientation.append(2)
            elif piece[1] in 'UD':
                orientation.append(1)
            else:
                orientation.append(0)
    return orientation
def getPermutation(state):
    permutation = [order[orderDict[sum(1 << faces.find(f) for f in piece)]] for piece in state]
    return permutation
# def move(orientation, permutation, move):
    # if move == 1:
def move_F(orient, perm):
    # edges
    orient[0],orient[8],orient[4],orient[9] = orient[9]^1,orient[0]^1,orient[8]^1,orient[4]^1
    perm[0],perm[8],perm[4],perm[9] = perm[9],perm[0],perm[8],perm[4]
    # corner
    orient[12],orient[16],orient[17],orient[15] = orient[15],orient[12],orient[16],orient[17]
    perm[12],perm[16],perm[17],perm[15] = perm[15] - 1,perm[12] + 1,perm[16] - 1,perm[17] + 1



# def checkEdges(edges):
#     for edge in edges:
#         if edge != 0:
#             return False
#     return True
def getGoodEdges():
    cube=[0]*20,0
    y = dict()
    x = [cube]
    for i,j in x:
        n = 0
        for k in i[:11]:
            n += k % 2# + n
        for k in range(y.get(n,6)):
            y[n] = j
            u = i[:]
            for l in 0,0,0:
                print("@")
Cube = [0] * 20
scramble= "LF UR UB UL RF DR DB DL FU FD BR BL LFU URB UBL LDF RUF RFD DLB DBR".split()
# scramble= "FL RD BR UB UR DF BL UL FU BD DL RF ULF UBL FRU URB DRF BRD FLD DLB".split()
orientation = getOrientation(scramble)
permutation = getPermutation(scramble)
print(orientation)
print(permutation)
move_F(orientation, permutation)
move_F(orientation, permutation)
move_F(orientation, permutation)
print(orientation)
print(permutation)
