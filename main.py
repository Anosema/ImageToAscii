from PIL import Image
from sys import argv

def ImageToText(filename, xChar=None, yChar=None):
	image = Image.open(filename).convert('LA')
	sizeX, sizeY = image.size
	if not xChar: xChar, yChar = sizeX, sizeY
	squareX, squareY = int(sizeX/xChar), int(sizeY/yChar)
	charac = ' .:-=+*#%@'
	ttw = ''
	for y in range(yChar):
		for x in range(xChar):
			total = 0
			for i in range((x-1)*squareX, x*squareX):
				for j in range((y-1)*squareY, y*squareY):
					total += image.getpixel((i, j))[0]
			ttw += charac[round(((total/(squareX*squareY))/255)*len(charac))-1]
		ttw += '\n'
	with open(filename.split('.')[0]+'.txt', 'w') as file: file.write(ttw)

def TextToImage(filename):
	charac = ' .:-=+*#%@'
	with open(filename, 'r') as file: data = file.readlines()
	image = Image.new('L', (len(data[0]), len(data)))
	p = image.load()
	for y, row in enumerate(data):
		for x, column in enumerate(row):
			i = round(charac.find(column) * (255/len(charac)))
			p[x, y] = (i)
	image.save(filename.split('.')[0]+'.png')

if len(argv) >= 1:
	if   len(argv) == 3 and argv[1] == '-itt': ImageToText(argv[2])
	elif len(argv) == 5 and argv[1] == '-itt': ImageToText(argv[2], round(int(argv[3])), round(int(argv[4])))
	elif len(argv) == 3 and argv[1] == '-tti': TextToImage(argv[2])