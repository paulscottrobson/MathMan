#
#	Build ghosts with different eyes
#
from PIL import Image

eyeList = [ "0right","1down","2left","3up"]
ghostList = [ "blue","cyan","multi","pink","red","white","yellow","blank"]
eyeGfx = {}
eyeSize = 58

for eye in eyeList:
	eyeGfx[eye] = Image.open(eye+".png").resize((eyeSize,eyeSize),resample=Image.BICUBIC)

for baseName in ghostList:
	base = Image.open(baseName+".png")
	width = base.size[0]
	base = base.crop((0,6,width,width+6))
	print(base.size)
	for eye in eyeList:
		img = base.copy()
		x = 50
		y = 64
		img.paste(eyeGfx[eye],(x-int(eyeSize/2),y-int(eyeSize/2)),eyeGfx[eye])
		img.paste(eyeGfx[eye],(width-x-int(eyeSize/2),y-int(eyeSize/2)),eyeGfx[eye])
		img.resize((52,52),resample=Image.BICUBIC).save(baseName+"_"+eye+".png")
