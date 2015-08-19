#
#	Chop segments out of Pacman.
#
from PIL import Image,ImageDraw

img = Image.open("pacman.png")
for angle in [0,90,180,270]:
	base = "pacman_"+str(angle)
	img.save(base+"_0.png")
	for gap in range(1,6):
		opimg = img.copy()
		gapAngle = gap * 8
		draw = ImageDraw.Draw(opimg)
		draw.pieslice([(0,0),opimg.size],angle-gapAngle,angle+gapAngle,fill = (0,0,0,0))
		opimg.save(base+"_"+str(gap)+".png")