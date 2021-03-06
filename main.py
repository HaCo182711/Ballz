import PyGUIgame.PyGUIgame as pgg
import Math

win = pgg.init(width := 256, height := 256, "Ballz")

class circle:
	def __init__(self, pos: tuple, r: int, vel: tuple):
		self.pos = pos
		self.r = r
		self.vel = vel

run = True
circles = [circle(Math.vec2(10*x+10,10*x+10), 10, Math.vec2(1,1)) for x in range(10)]
while run:
	win.update()
	win.background(pgg.BLACK)

	for c in circles:
		win.draw_circle(pgg.RED, c.pos.tuple(), c.r)
		
		c.vel.y -= 0.1
		
		c.pos = c.pos + c.vel
		c.vel = c.vel*0.99

		# walls
		if c.pos.y >= height/2 - c.r:
			c.vel.y = -c.vel.y
			c.pos.y = height/2-c.r
		if c.pos.y <= -height/2+c.r:
			c.vel.y = -c.vel.y
			c.pos.y = -height/2 + c.r
		if c.pos.x >= width/2-c.r:
			c.vel.x = -c.vel.x
			c.pos.x = width/2-c.r
		if c.pos.x <= -width/2 + c.r:
			c.vel.x = -c.vel.x
			c.pos.x = -width/2 + c.r

		# circle collision
		for col in circles:
			if col != c:
				dis = Math.dis(c.pos, col.pos) - (c.r+col.r)
				if dis <= 0:
					# still needs to update the velocity
					dir = (c.pos - col.pos).normalized()
					c.pos = c.pos - dir*(dis/2)
					col.pos = col.pos + dir*(dis/2)
					c.vel = c.vel - dir*dis
					col.vel = col.vel + dir*dis
					
		

	if win.isKeyPressed("Escape"):
		run = False