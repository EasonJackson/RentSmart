import rental_crawler as client
import Queue
import time

i = 1

q = Queue.Queue()

#START = '''http://www.rentals.com/Massachusetts/Framingham/lv27395835/'''
START = '''http://www.rentals.com/Massachusetts/Worcester/2874/'''

result = client.getInfo(START)

while i < 1:
	i = i + 1
	search_param = client.getURL(q.get())
	result = client.getInfo(search_param)
	#print result
	#time.sleep(5)