import requests
import re
import lxml

from lxml import html
from re import sub
from urllib import pathname2url

URL = '''http://www.condo.com'''

PRICE = '''//div[@class='unit-cover-text']/h4/text()'''
BEDS_BATH = '''//div[@class='unit-cover-text']/h2/text()'''
ADDRESS = '''//div[@class='col-xs-8 col-sm-6 map-thumb']/h2/text()'''
#SIMILAR = '''//div[@class='thumbnail-overlay pointer']/div[@class='aligment']/div[@class='aligment']/a//@href'''
SIMILAR = '''//a/@href'''

SIMILAR_REGEX = '\/property\/.*'

def search_rent(url):
	req_session = requests.session()
	response = req_session.get(url, headers=getHeaders())
	#print response.content
	try:
		tree = html.fromstring(response.content)
	except Exception:
		return {}
	return tree

def getHeaders():
	headers = {
		"Connection" : "close",
		"User-Agent" : "Chrome"
	}
	return headers

def getInfo(url):
	tree = search_rent(url)
	# Get price
	try:
		price = tree.xpath(PRICE)
		print price
	except Exception:
		price = 0

	# Get beds and bath
	try:
		beds_bath_size = tree.xpath(BEDS_BATH)
		print beds_bath_size
	except Exception:
		beds_bath_size = ["0 beds~0 bath"]

	beds = {}
	bath = {}
	size = {}

	beds = beds_bath_size[0].split('~')[0]
	bath = beds_bath_size[0].split('~')[1]
	if len(beds_bath_size) > 2:
		size = beds_bath_size[0].split('~')[2]
	else:
		size = "Not available"

	print "beds: " + beds + ", bath: " + bath + ", size: " + size

	# Get address
	try:
		address_raw = tree.xpath(ADDRESS)
		address = address_raw[0] + ", " + address_raw[1]
		print address
	except Exception:
		address = "Not available"

	# Get similar rental link
	try:
		similar = tree.xpath(SIMILAR)
		#print similar
		for x in similar:
			#print x + '\t'
			try:
				m = re.search(SIMIARL_REGEX, '\''+ x +'\'')
				print m.group(0)
			except Exception:
				pass
			
	except Exception:
		similar = {}

	return {
			'Price' : price,
			'Beds' : beds,
			'Bath' : bath,
			'Size' : size,
			'Address' : address,
			'Similar' : similar
			}


def getURL(search_param):
	return '%s/%s' %(URL, search_param)