PPM_FILENAME = "Brian_Chuk.ppm"
PPM_WIDTH = 1000
PPM_HEIGHT = 1000
PPM_MAX_VAL = 255

fo = open(PPM_FILENAME, "wb") #creates the file with a name. The w represents write, b represents binary mode.
hurr = ""

#creates file header. Numbers are Width, Height, and MaxVal
hurr += "P3 1000 1000 255"

for y in range(0,PPM_HEIGHT):
	for x in range(0,PPM_WIDTH):
		hurr += ((str(x % 255)) + " " + (str(y % 255)) + " " + str((x * y) % 255))

fo.write(hurr)
fo.close()

#IT'S SO SIMPLE LOL ;___;