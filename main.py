from PIL import Image
from sys import argv

def main(filename, xChar, yChar):
	image = Image.open(filename).convert('LA')
	sizeX, sizeY = image.size
	squareX, squareY = int(sizeX/xChar), int(sizeY/yChar)
	charac = ' .:-=+*#%@'
	ttw = ''
	for y in range(yChar):
		for x in range(xChar):
			total = 0
			for i in range((x-1)*squareX, x*squareX):
				for j in range((y-1)*squareY, y*squareY):
					total += image.getpixel((i, j))[0]
			ttw += charac[round(((total/(squareX*squareY))/255)*10)-1]
		ttw += '\n'
	with open(filename.split('.')[0]+'.txt', 'w') as file: file.write(ttw)

if len(argv)==4: main(argv[1], round(int(argv[2])), round(int(argv[3])))