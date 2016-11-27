from SimpleCV import *

cam = Camera()
threshold = 5.0 # caso a diferença seja maior que o limiar, o movimento será considerado

cont = 0
fps = 2
width = 320
height = 240

while True:
	antes = cam.getImage() #captura um frame
	time.sleep(1.0/(fps*2)) #espera uma parcela de segundo 
	depois = cam.getImage() #captura outro frame
	antesLst = []
	depoisLst = []
	difLst = []
	depois.show()
	i = 0
	j = 0
	for i in range(0,2):
		for j in range(0,2):
			antesLst.append(antes.crop(j*width, i*height, width, height, False))
			depoisLst.append(depois.crop(j*width, i*height, width, height, False))
			difLst.append(depoisLst[i*2+j] - antesLst[i*2+j])
			matrix = difLst[i*2+j].getNumpy()
			mean = matrix.mean()
			if mean >= threshold:	
				depois.drawText('Movimento detectado')
				depois.show()		
