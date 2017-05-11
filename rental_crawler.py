import requests
import re
import lxml

from lxml import html
from re import sub
from urllib import pathname2url

URL = '''http://www.rentals.com'''

PRICE = '''//table[@class='floorPlanTable']/tbody/tr/td[6]/text()'''
PRICE_BACKUP = '''//h2[@id='top_heading']/text()''' # Use $ to seperate last word
BEDS = '''//table[@class='floorPlanTable']/tbody/tr/td[2]/text()'''
BATH = '''//table[@class='floorPlanTable']/tbody/tr/td[3]/text()'''
SIZE = '''//table[@class='floorPlanTable']/tbody/tr/td[5]/text()'''
BED_BATH_SIZE_BACKUP = '''//div[@class='plan_overview']/div[@id='summary_floorplan']//text()'''

ADDRESS = '''//p[@id='summary_address']//text()'''
CONTACTS = '''//a[@id='summary_phone']/text()'''

SIMILAR = ''''''

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
	#print tree
	# Get price
	try:
		price1 = tree.xpath(PRICE)
		price2 = tree.xpath(PRICE_BACKUP)
		print price1
		print price2
		if len(price1) == 0:
			price = "$" + price2.split("$")[1].strip(' ')
		else:
			price = price1
		print price
	except Exception:
		price = 0

	# Get beds and bath
	try:
		beds = tree.xpath(BEDS)
		print beds
	except Exception:
		beds = 0

	try:
		bath = tree.xpath(BATH)
		print bath
	except Exception:
		bath = 0

	try:
		bed_bath_size = tree.xpath(BED_BATH_SIZE_BACKUP)
		beds2 = bed_bath_size.split("|")[0]
		bath2 = bed_bath_size.split("|")[1]
		if len(bed_bath_size) == 3:
			size = bed_bath_size.split("|")[2]
	except Exception:
		size = 0

	# Get address
	try:
		address = tree.xpath(ADDRESS)
		print address
	except Exception:
		address = "Not available"


	# Get contact info
	try:
		contacts = tree.xpath(CONTACTS)
		print contacts
	except Exception:
		contacts = "Not available"


	return {
			'Price' : price,
			'Beds' : beds,
			'Bath' : bath,
			'Size' : size,
			'Address' : address,
			'Contacts' : contacts,
			}


def getURL(search_param):
	return '%s/%s' %(URL, search_param)