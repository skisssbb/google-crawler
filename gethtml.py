import requests
from fake_useragent import UserAgent

######################################################################
#
#	Global Attributes
#
######################################################################
ua = UserAgent()
url_ori= "https://www.google.de/search?q="

# Write Google Search Result of an input to a filw with "fileName"
def writeHtmlInFile(fileName, input):
	modstr = input.replace(" ","+")
	url = url_ori + modstr
	headers = {'User-Agent':ua.firefox}
	re = requests.get(url, headers = headers)
	file = open(fileName,"wb")
	file.write(re.content)
	file.close()


writeHtmlInFile("output.html","donald trump")
