import PyGUIgame.PyGUIgame as pgg
import random

win = pgg.init(width := 256, height := 256, "Ballz")

class circle:
	def __init__(self, pos, r, vel):
		self.pos = pos
		self.r = r
		self.vel = vel

run = True
circles = [circle((15*x+20,15*x+20), 10, (0,0)) for x in range(10)]
while run:
	win.update()
	win.background(pgg.BLACK)

	for c in circles:
		win.draw_circle(pgg.RED, c.pos, c.r)
		c.vel = c.vel[0], c.vel[1] + 0.1
		c.pos = c.pos[0] + c.vel[0], c.pos[1] + c.vel[1]
		for col in circles:
			if col != c:
				if dis(c.pos, col.pos) - (c.r+col.r) < 0:
					pass
		

	if win.isKeyPressed("Escape"):
		run = False