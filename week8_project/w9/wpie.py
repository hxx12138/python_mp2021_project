import itertools
import time
import sys

def spin(msg):
	for s in itertools.cycle('|/-\\'):
		status=s+' '+msg
		sys.stdout.write(status)
		sys.stdout.flush()
		sys.stdout.write('\x08'*len(status))#'\x08'是退格符，删除
		time.sleep(0.5)

spin(sys.argv[1])