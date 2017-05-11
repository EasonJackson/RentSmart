import rent_crawler as client
import Queue
import time

i = 0

q = Queue.Queue()

START = '''http://www.rent.com/massachusetts/worcester-apartments/sutton-apartments-4-489927'''
#START = '''http://www.rent.com/massachusetts/worcester-apartments/junction-shop-lofts-4-100056594'''


result = client.getInfo(START)
#print result['Price']
#print result['Beds']
#print result['Bath']
#print result['Contacts']
#print result['Address']

for item in result['Similar']:
	q.put(item)

while i < 1:
	i = i + 1
	search_param = client.getURL(q.get())
	result = client.getInfo(search_param)
	#print result
	#time.sleep(5)
