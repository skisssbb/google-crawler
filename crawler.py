import requests
import re
import urlparse
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
url_ori= "https://www.google.de/search?q="
def give_firstNLinks(input, n = 10):
	modstr = input.replace(" ","+")
	url =  url_ori + modstr
	print url
	headers = {'User-Agent':ua.firefox}
	re = requests.get(url, headers = headers)
	print "Request Status:" + str(re.status_code)
	file = open("Output.html","wb")
	file.write(re.content)
	file.close()
	soup = BeautifulSoup(re.content)
	print soup.findAll("div", {"class":"g"}).text()




"""
url = "http://www.spiegel.de/politik/ausland/venezuela-vier-szenarien-fuer-die-zukunft-des-krisenlandes-a-1145434.html"
re = requests.get(url)
soup = BeautifulSoup(re.content)
file = open("Output.txt","wb")
#file.write(soup.prettify().encode('utf8'))
file.close()
"""

give_firstNLinks("donald duck", 10)