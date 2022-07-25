class Shape:
	def draw(self):
		pass

class Triangle(Shape):
	def draw(self):
		print("draw a triangle")

class Rectangle(Shape):
	def draw(self):
		print("draw a rect")

class Circle(Shape):
	def draw(self):
		print("draw a circle")

def draw(shapes=None):
	if shapes:
		for s in shapes:
			s.draw()

shapes=[Triangle(),Rectangle(),Circle()]
draw(shapes)

class OddShape(Shape):
	def draw(self):
		print("draw an odd shape")

shapes=[Triangle(),Rectangle(),Circle(),OddShape()]
draw(shapes)