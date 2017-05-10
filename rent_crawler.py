import requests
import re
import lxml

from lxml import html
from re import sub
from urllib import pathname2url

URL = '''http://www.rent.com'''

PRICE = '''//td[@class='floorplan-rent']'''
BEDS_BATH = '''//td[@class='floorplan-beed-bath']'''
ADDRESS = '''//div[@class='pdp-heading-address']'''
CONTACTS = '''//td[@class='floorplan-call']/a[@class='tel-default attributed-click hidden-xs js-campaign-phone-number js-phone']/strong[@class='tel']'''

SIMILAR = '''//div[@class='img-table-cell']/a[@class='slide-img']/@href'''

def search_rent(url):
	req_session = requests.session()
	response = req_session.get(url, headers=getHeaders())
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
	try:
		price = tree.xpath(PRICE)
	except Exception:
		price = 0

	try:
		beds_bath = tree.xpath(BEDS_BATH)
	except Exception:
		beds_bath = "0 beds/0 bath"
	beds = beds_bath.split("/")[0]
	bath = beds_bath.split("/")[1]

	try:
		address = tree.xpath(ADDRESS)
	except Exception:
		address = "Not available"

	try:
		contacts = tree.xpath(CONTACTS)
	except Exception:
		contacts = "Not available"

	try:
		similar = tree.xpath(SIMILAR)
	except Exception:
		similar = {}

	return {
			"Price" : price,
			"Beds" : beds,
			"Bath" : bath,
			"Address" : address,
			"Contacts" : contacts,
			"Similar" : similar
			}


def getURL(search_param):
	return '%s/%s' %(URL, search_param)