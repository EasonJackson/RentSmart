import condo_crawler as client
import Queue
import time

i = 0

q = Queue.Queue()

#START = '''http://www.rentals.com/Massachusetts/Framingham/lv27395835/'''
START = '''http://www.condo.com/property/45-Grand-Street-2-Bed-1-Bath-Worcester-MA-01610-150465875'''

result = client.getInfo(START)
for item in result['Similar']:
	q.put(item)

print "Crawler finished collecting info. Count" + i

while i < 1:
	i = i + 1
	if ~q.empty():
		search_param = client.getURL(q.get())
	else:
		break
	result = client.getInfo(search_param)
	for item in result['Similar']:
		q.put(item)
	print "Crawler finished collecting info. Count" + i
	#print result
	time.sleep(3)