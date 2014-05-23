from display import *
from matrix import *


#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color ):
	[draw_line(screen, a[0], a[1], b[0], b[1], color) for (a,b) in zip(matrix, matrix[1:]) if matrix.index(a) % 2==0]

#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
	add_point(matrix, x0, y0, z0)
	add_point(matrix, x1, y1, z1)

#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
	matrix.append([x, y, z, 1])

#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line( screen, x0, y0, x1, y1, color ):
	if (x0 == x1): #if the points are horizontal of each other.
		y = y0
		if(y0 > y1):
			while( y >= y1):
				plot(screen, color, x0, y)
				y -= 1
		else:
			while( y <= y1):
				plot(screen, color, x0, y)
				y += 1
		return	
	if (x0 > x1): #if the first point is to the right of the other, flip the points around.
		x2 = x0
		y2 = y0
		x0 = x1
		y0 = y1
		x1 = x2
		y1 = y2
	A = y1 - y0
	B = -(x1 - x0)
	dy = y1-y0
	dx = x1-x0
	#Find the slope to determine the octants
 	if(dy > 0):
 		if(dx > dy):
 			octant = 1
 		else:
 			octant = 2
 	else:
 		if(dx > dy*-1):
 			octant = 8
 		else:
 			octant = 7
	x = x0
	y = y0
	#Plot accordingally
	if (octant == 1):
		d = 2*A + B
		while (x <= x1):
			plot(screen, color, x,y)
			if(d > 0):
				y += 1
				d += 2*B
			x += 1
			d += 2*A
	
	if (octant == 2):
		d = 2*B + A
		while (y <= y1):
			plot(screen, color, x,y)
			if(d < 0):
				x += 1
				d += 2*A
			y += 1
			d += 2*B

	if (octant == 8):
		d = 2*A - B
		while (x <= x1):
			plot(screen, color, x,y)
			if(d < 0):
				y -= 1
				d -= 2*B
			x += 1
			d += 2*A
	else: #octant 7
		d = -2*B + A
		while (y >= y1):
			plot(screen, color, x,y)
			if(d > 0):
				x += 1
				d += 2*A
			y -= 1
			d -= 2*B