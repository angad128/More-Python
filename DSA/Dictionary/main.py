d = {}
d[1] = "yes"
print(d[1])
d['1'] = "no"
print(d['1'])

class my_class:
	def __init__(self):
		self.data = "data"

instance = my_class()
d['object'] = instance
d['object'].data
print(d.keys())
print(d.items())
print(d)