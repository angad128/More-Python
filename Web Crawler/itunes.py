

class AppCrwawler(object):
	"""docstring for AppCrwawler"""
	def __init__(self, starting_url, depth):
		self.starting_url = starting_url
		self.depth = depth
		self.apps = []
		
	def crawl(self):
		return 

	def get_app_from_link(self, link):
		return


class App(object):
	"""docstring for App"""
	def __init__(self, developer, price, link):
		self.name = name
		self.developer = developer
		self.price = price
		self.link = link

	def __str__(self):
		return("Name: "+ self.name.encode('UTF-8') + 
			"\r\nDeveloper: " + self.developer.encode('UTF-8') +
			"\r\Price: " + self.price.encode('UTF-8') + "\r\n")

		
crawler = AppCrwawler('https://itunes.apple.com/us/app/candy-crush-saga/id553834731?mt=8', 0)
crawler.crawl()

for app in crawler.apps:
	print("app")
