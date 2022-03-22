import PyGUIgame.PyGUIgame as pgg
import Math

win = pgg.init(width := 256, height := 256, "Ballz")

class circle:
	def __init__(self, pos, r, vel):
		self.pos = pos
		self.r = r
		self.vel = vel

run = True
circles = [circle(Math.vec2(15*x+20,15*x+20), 10, Math.vec2(10,10)) for x in range(10)]
while run:
	win.update()
	win.background(pgg.BLACK)

	for c in circles:
		win.draw_circle(pgg.RED, c.pos.tuple(), c.r)
		
		c.vel.y += 0.2
		
		c.pos = c.pos + c.vel
		c.vel = c.vel*0.99

		# walls
		if c.pos.y >= height-c.r:
			c.vel.y = -c.vel.y
			c.pos.y = height-c.r
		if c.pos.y <= c.r:
			c.vel.y = -c.vel.y
			c.pos.y = c.r
		if c.pos.x >= width-c.r:
			c.vel.x = -c.vel.x
			c.pos.x = width-c.r
		if c.pos.x <= c.r:
			c.vel.x = -c.vel.x
			c.pos.x = c.r

		# circle collision
		for col in circles:
			if col != c:
				dis = Math.dis(c.pos, col.pos) - (c.r+col.r)
				if dis <= 0:
					# still needs to update the velocity
					dir = (c.pos - col.pos).normalized()
					c.pos = c.pos - dir*(dis/2)
					col.pos = col.pos + dir*(dis/2)
					
		

	if win.isKeyPressed("Escape"):
		run = False