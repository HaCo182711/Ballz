import math
import random

def randint(l,u):
	return random.randint(l,u)

class vec2:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __str__(self):
		return f"{self.x}, {self.y}"
	def __add__(self, b):
		return vec2(self.x+b.x, self.y+b.y)
	def __sub__(self, b):
		return vec2(self.x-b.x, self.y-b.y)
	def __mul__(self, b):
		return vec2(self.x*b, self.y*b)
	def __truediv__(self, b):
		return vec2(self.x/b, self.y/b)
	def len(self):
		return math.sqrt(self.x**2+self.y**2)
	def normalized(self):
		return vec2(self.x/self.len(), self.y/self.len())
	def tuple(self):
		return (self.x, self.y)

def dis(x,y):
	return math.sqrt((x.x-y.x)**2+(x.y-y.y)**2)