
from pygame import *

WIDTH = 1150
HEIGHT = 600
init()
screen = display.set_mode((WIDTH,HEIGHT))
clock = time.Clock()



class Pilka(object):
	def __init__(self):
		self.pic = image.load("ball.png")
		
	def go(self,x,y,trawy):
		for trawa in trawy:
			trawa.update(x,y)
		
		X = (2 * HEIGHT + (WIDTH-350)/2) / 2
		Y = (2 * HEIGHT - (WIDTH-350)/2) / 2
		
		jestPodloga = False
		for trawa in trawy:
			if -150 <= trawa.pos[0] <= -100 and 430 <= trawa.pos[1] <= 480:
				jestPodloga = True
		print(jestPodloga, X,Y,trawy[0].pos)
		'''if not jestPodloga:
			for trawa in trawy:
				trawa.update(-x,-y)'''			

			
	def draw(self):
		screen.blit(self.pic, ((WIDTH-350)//2,HEIGHT//2))

class Trawa(object):
	def __init__(self,x,y):
		self.pix = [x,y]
		self.pos = [x*50,y*50]
		self.iso = [self.pos[1]-self.pos[0], (self.pos[1]+self.pos[0])/2]
		self.pic = image.load("grass.png")
		self.cien = True
		
	def draw(self):
		screen.blit(self.pic, self.iso)
		
	def update(self,x,y):
		self.pos = [self.pos[0]+x,self.pos[1]+y]
		self.iso = [self.pos[1]-self.pos[0], (self.pos[1]+self.pos[0])/2]
		if 0 < self.iso[0] < WIDTH and 0 < self.iso[1] < HEIGHT:
			self.cien = False



plik = open("map.dat")
trawy = []
y = 0
for linia in plik:
	x = 0
	for znak in linia:
		if znak in ".S":
			trawy.append(Trawa(x,y))
		x += 1
	y += 1
	

pilka = Pilka()
ramka = image.load("mapa.png")




pilka.go(-130, 450, trawy)



end = False
time = 0
while not end:
	for z in event.get():
		if z.type == QUIT:
			end = True
			
			
	keys=key.get_pressed()
	if keys[K_RIGHT]: pilka.go(10,0,trawy)
	if keys[K_LEFT]: pilka.go(-10,0,trawy)
	if keys[K_UP]: pilka.go(0,10,trawy)
	if keys[K_DOWN]: pilka.go(0,-10,trawy)	
	#print(trawy[0].pos)
	'''
	if keys[K_d] and keys[K_s]: rycerz.go(1,1)
	elif keys[K_d] and keys[K_w]: rycerz.go(1,-1)
	elif keys[K_a] and keys[K_w]: rycerz.go(-1,-1)
	elif keys[K_a] and keys[K_s]: rycerz.go(-1,1)		
	elif keys[K_d]: rycerz.go(1,0)
	elif keys[K_a]: rycerz.go(-1,0)
	elif keys[K_w]: rycerz.go(0,-1)
	elif keys[K_s]: rycerz.go(0,1)
	if keys[K_SPACE]: rycerz.attack = True
			
	if keys[K_RIGHT] and keys[K_DOWN]: rycerz2.go(1,1)
	elif keys[K_RIGHT] and keys[K_UP]: rycerz2.go(1,-1)
	elif keys[K_LEFT] and keys[K_UP]: rycerz2.go(-1,-1)
	elif keys[K_LEFT] and keys[K_DOWN]: rycerz2.go(-1,1)		
	elif keys[K_RIGHT]: rycerz2.go(1,0)
	elif keys[K_LEFT]: rycerz2.go(-1,0)
	elif keys[K_UP]: rycerz2.go(0,-1)
	elif keys[K_DOWN]: rycerz2.go(0,1)
	'''

		
	screen.fill((135, 206, 235))
	
	for trawa in trawy:
		trawa.draw()
	pilka.draw()
	
	
	#draw.rect(screen,(0,0,0), Rect(WIDTH-300,0,300,150),0)
	screen.blit(ramka,(WIDTH-370,0))
	for trawa in trawy:
		if not trawa.cien:
			draw.rect(screen,(0,255,0), Rect(trawa.pix[0]*3+WIDTH-320,trawa.pix[1]*3+50,3,3),0)
			if (WIDTH-350)//2 - 50 < trawa.iso[0] < (WIDTH-350)//2 + 50 and HEIGHT//2 - 50 < trawa.iso[1] < HEIGHT//2 + 50:
				draw.rect(screen,(255,0,0), Rect(trawa.pix[0]*3+WIDTH-320,trawa.pix[1]*3+50,3,3),0)

	
	display.flip()
	clock.tick(25)

