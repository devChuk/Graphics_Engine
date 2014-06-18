from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         l: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 i: set the transform matrix to the identity matrix - 
	 s: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 t: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 x: create an x-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 y: create an y-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 z: create an z-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 a: apply the current transformation matrix to the 
	    edge matrix
	 v: draw the lines of the edge matrix to the screen
	    display the screen
	 g: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 q: end parsing

See the file script for an example of the file format

IMPORTANT MATH NOTE:
the trig functions in the math library use radian mesure, but us normal
humans use degrees, so the file will contain degrees for rotations,
be sure to conver those degrees to radians
"""

def deg2rad(degree):
	return ((float)(degree * math.pi / 180))

def trans(func, transform):
	return matrix_mult(func(*args), transform)

def parse_file( fname, points, transform ):
	screen = new_screen()
	with open(fname) as script:
		for line in script:
			line = line[:-1]

			if not line.replace(" ","").isdigit():	
				comm = line.strip()
				if comm == 'i':
					transform = ident(points)
				elif comm == 'a':
					points = matrix_mult(transform, points)
					transform = ident(transform)
				elif comm == 'v':
					clear_screen(screen)
					draw_lines(points, screen, [0,225,0])
					display(screen)
					sleep(0.5)
				elif comm == 'q':
					return
			else:
				args = [float(x) for x in line.split()]
				if comm == 'l':
					# params = [points].extend([x for x in args])
					add_edge(points, *[x for x in args])
				elif comm == 'i':
					transform = ident(points)
				elif comm == 's':
					transform = trans(make_scale, transform)
				elif comm == 't':
					transform = trans(make_translate, transform)
				elif comm == 'x':
					args = [deg2rad(x) for x in args]
					transform = trans(make_rotX, transform)	
				elif comm == 'y':
					args = [deg2rad(x) for x in args]
					transform = trans(make_rotY, transform)
				elif comm == 'z':
					args = [deg2rad(x) for x in args]
					transform = trans(make_rotZ, transform)
				elif comm == 'g':
					draw_lines(points, screen, [0,225,0] )
					save_ppm(screen, args[0])







points = []
transform = new_matrix()

parse_file( 'script_c', points, transform )