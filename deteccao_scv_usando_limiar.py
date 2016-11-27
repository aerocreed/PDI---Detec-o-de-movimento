from SimpleCV import *

cam = Camera()
threshold = 5.0 # if mean exceeds this amount do something

cont = 0
fps = 15

while True:
	previous = cam.getImage() #grab a frame
	time.sleep(1.0/fps) #wait for half a second
	current = cam.getImage() #grab another frame
	diff = current - previous
	matrix = diff.getNumpy()
	mean = matrix.mean()	
	if mean >= threshold:
		print (diff)
		cont = cont + 1
		pathAtual = 'atual%d.jpg' % (cont,)
		pathAnterior = 'anterior%d.jpg' % (cont,)
		previous.save(pathAnterior)
		current.save(pathAtual)
		print 'Motion Detected'

