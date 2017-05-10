import rent_crawler as client
import Queue

i = 0

q = Queue.Queue()

START = '''http://www.rent.com/massachusetts/worcester-apartments/sutton-apartments-4-489927'''

result = client.getInfo(START)
print result

for item in result.Similar:
	q.put(item)

while i < 1:
	i = i + 1
	search = client.getURL(q.get())
	result = client.getInfo(search)
	print result
