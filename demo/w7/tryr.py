from warnings import warn
warn('testing of different return positions')

def test_return():
	try:
		print('in try')
		#raise Exception
		#return 'return from try'#
	except Exception:
		print('in except')
		#return 'return from except'#
	else:
		print('in else')
		#return 'return from else'#
	finally:
		print('in finally')
		#return 'return from finally'#

	return 'return from the last line'

print(test_return())