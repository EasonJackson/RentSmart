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
SIZE = '''//div[@class='unit-cover-text']/h2/text()'''
SIMILAR = '''//div[@class='media-box-image']/div[@class='thumbnail-overlay pointer']/div[@class='aligment']/div[@class='aligment']/a/@href'''

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
		beds_bath = tree.xpath(BEDS_BATH)
		print beds_bath
	except Exception:
		beds_bath = ["0 beds/0 bath"]

	beds = []
	bath = []
	#or item in beds_bath:
	#	beds.append(item.split("/")[0])
	#	bath.append(item.split("/")[1])

	# Get address
	try:
		address_raw = tree.xpath(ADDRESS)
		address = ''
		for i in range(0, len(address_raw) - 1):
			address = address + address_raw[i]
		address.strip(' ')
		print address
	except Exception:
		address = "Not available"

	# Get apt size
	try:
		size = tree.xpath(SIZE)
		print size
	except Exception:
		size = [0,0]


	# Get contact info
	try:
		contacts = tree.xpath(CONTACTS)
		print contacts
	except Exception:
		contacts = "Not available"


	# Get similar rental link
	try:
		similar = tree.xpath(SIMILAR)
		print similar
	except Exception:
		similar = {}

	return {
			'Price' : price,
			'Beds' : beds,
			'Bath' : bath,
			'Size' : size,
			'Address' : address,
			'Contacts' : contacts,
			'Similar' : similar
			}


def getURL(search_param):
	return '%s/%s' %(URL, search_param)