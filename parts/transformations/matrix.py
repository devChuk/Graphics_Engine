import math

def make_translate( x, y, z ):
    #creates a translation instruction based on the parameters inserted.
    transMatrix = ident(new_matrix())
    transMatrix[0][3] = x
    transMatrix[1][3] = y
    transMatrix[2][3] = z
    return transM
def make_scale( x, y, z ):
    scaleMatrix = new_matrix()
    for i in range(4):
        scaleMatrix[i][i] = [x,y,z][i]
    return scaleMatrix
    
def make_rotX( theta ):    
    rotXMatrix = ident(new_matrix())
    sin = math.sin(theta)
    cos = math.cos(theta)
    rotXMatrix[1][1] = cos
    rotXMatrix[1][2] = -sin
    rotXMatrix[2][1] = sin
    rotXMatrix[2][2] = cos
    return rotXMatrix

def make_rotY( theta ):
    rotYMatrix = ident(new_matrix())
    sin = math.sin(theta)
    cos = math.cos(theta)
    rotYMatrix[0][0] = cos
    rotYMatrix[0][2] = -sin
    rotYMatrix[2][1] = sin
    rotYMatrix[2][2] = cos
    return rotYMatrix

def make_rotZ( theta ):
    rotZMatrix = ident(new_matrix())
    sin = math.sin(theta)
    cos = math.cos(theta)
    rotZMatrix[0][0] = cos
    rotZMatrix[0][1] = -sin
    rotZMatrix[1][1] = sin
    rotZMatrix[1][2] = cos
    return rotZMatrix


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    #creates identity matrix
    columnCount = len(matrix)
    ans = new_matrix(columnCount,columnCount)
    for i in range(columnCount):
        ans[i][i] = 1
    return ans

def scalar_mult( matrix, x ):
    #multiples each element in of matrix matrix by a multiple of x
    return [[element * x for element in a] for column in matrix]

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    #multiplies matrix
    if (len(m1) == len(m2[0])
        return [ [sum( [f*g for (f,g) in zip( [x[i] for x in m1] , m2[g] )] ) for g in range(len(m2)) ] for i in range(len(m1[0])) ]
    else
        print "Error. Number of columns of the first matrix is NOT equal to the number of rows in the second matrix"
