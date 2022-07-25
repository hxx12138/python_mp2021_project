import functools

def next_deco(func):
	@functools.wraps(func)
	def wrapper(*args,**kwargs):
		resulted_g=func(*args,**kwargs)
		next(resulted_g)
		return resulted_g
	return wrapper

@next_deco
def food_factory():
	food_list = []
	while True:
		food = yield food_list
		food_list.append(food)
		print("We have ",food_list)

fg=food_factory()
#fg.send(None)
fg.send('apple')
fg.send('banana')
fg.send('pear')
fg.send('orange')


