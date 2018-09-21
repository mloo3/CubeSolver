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
def move_F(orient, perm):
    # edges
    orient[0],orient[8],orient[4],orient[9] = orient[9]^1,orient[0]^1,orient[8]^1,orient[4]^1
    perm[0],perm[8],perm[4],perm[9] = perm[9],perm[0],perm[8],perm[4]
    # corner
    orient[12],orient[16],orient[17],orient[15] = (orient[15] - 1)%3,(orient[12] + 1)%3,(orient[16] - 1)%3,(orient[17] + 1)%3
    perm[12],perm[16],perm[17],perm[15] = perm[15],perm[12],perm[16],perm[17]
def move_B(orient, perm):
    # edges
    orient[2],orient[11],orient[6],orient[10] = orient[10]^1,orient[2]^1,orient[11]^1,orient[6]^1
    perm[2],perm[11],perm[6],perm[10] = perm[10],perm[2],perm[11],perm[6]
    # corner
    orient[13],orient[14],orient[18],orient[19]=(orient[19]+1)%3,(orient[13]-1)%3,(orient[14]+1)%3,(orient[18]-1)%3
    perm[13],perm[14],perm[18],perm[19]=perm[19],perm[13],perm[14],perm[18]
def move_R(orient, perm):
    # edges
    orient[1],orient[10],orient[5],orient[8]=orient[8],orient[1],orient[10],orient[5]
    perm[1],perm[10],perm[5],perm[8]=perm[8],perm[1],perm[10],perm[5]
    # corner
    orient[12],orient[13],orient[19],orient[16] =(orient[16]+1)%3,(orient[12]-1)%3,(orient[13]+1)%3,(orient[19]-1)%3
    perm[12],perm[13],perm[19],perm[16] =perm[16],perm[12],perm[13],perm[19]
def move_L(orient, perm):
    # edges
    orient[3],orient[9],orient[7],orient[11]=orient[11],orient[3],orient[9],orient[7]
    perm[3],perm[9],perm[7],perm[11]=perm[11],perm[3],perm[9],perm[7]
    # corner
    orient[15],orient[17],orient[18],orient[14]=(orient[14]-1)%3,(orient[15]+1)%3,(orient[17]-1)%3,(orient[18]+1)%3
    perm[15],perm[17],perm[18],perm[14] = perm[14],perm[15],perm[17],perm[18]
def move_U(orient, perm):
    # edges
    orient[0],orient[3],orient[2],orient[1]=orient[1],orient[0],orient[3],orient[2]
    perm[0],perm[3],perm[2],perm[1]=perm[1],perm[0],perm[3],perm[2]
    #corners
    orient[12],orient[15],orient[14],orient[13]=orient[13],orient[12],orient[15],orient[14]
    perm[12],perm[15],perm[14],perm[13]=perm[13],perm[12],perm[15],perm[14]
def move_D(orient, perm):
    # edges
    orient[4],orient[5],orient[6],orient[7] = orient[7],orient[4],orient[5],orient[6]
    perm[4],perm[5],perm[6],perm[7] = perm[7],perm[4],perm[5],perm[6]
    # corners
    orient[16],orient[19],orient[18],orient[17]=orient[17],orient[16],orient[19],orient[18]
    perm[16],perm[19],perm[18],perm[17]=perm[17],perm[16],perm[19],perm[18]
def move(orientation, permutation, move):
    if move == 0:
        move_F(orientation,permutation)
    elif move == 1:
        move_B(orientation,permutation)
    elif move ==2:
        move_R(orientation,permutation)
    elif move==3:
        move_L(orientation,permutation)
    elif move==4:
        move_U(orientation,permutation)
    elif move==5:
        move_D(orientation,permutation)

Cube = [0] * 20
scramble= "FL RD BR UB UR DF BL UL FU BD DL RF ULF UBL FRU URB DRF BRD FLD DLB".split()
orientation = getOrientation(scramble)
permutation = getPermutation(scramble)
