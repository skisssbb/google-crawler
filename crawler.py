import urllib
import re
import urlparse
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

######################################################################
#
#	Global Attributes
#
######################################################################
fileName = "output.html"

# Parse html file: "fileName" and give back a list of n links found
# n: Maximal numbers of links to return
# return: a list of the first 10 links found from that google page "filename"
def give_firstNLinks(n = 10):
	linkList = []
	file = open("output.html","r")
	htmlcontent = file.read()
	file.close()
	soup = BeautifulSoup(htmlcontent, "html.parser")
	g_data = soup.findAll("div", {"class":"g"})
	for i,item in enumerate(g_data):
		if i < n:
			for link in item.findAll("h3", {"class":"r"}):
				linkList.append(link.find("a").get("href"))
	return linkList

# receive a list of links, count the words from each links and give them back
def countWordsAllLinks(linkList):
	print linkList[0]
	print "--> %d" %countWordURL(linkList[0])

# receive a link, count it and return the words number
# return: number of words counted from link
def countWordURL(link):
	data = urllib.urlopen(link)
	if data.getcode() == 200:
		htmltext = data.read()
		soup = BeautifulSoup(htmltext, "html.parser")
		print soup.findAll("div", {"id":"mw-content-text"})
		#TODO, count weiter
		return 0


for link in give_firstNLinks(10):
	print link
countWordsAllLinks(give_firstNLinks(10))