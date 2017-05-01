import requests
import re
import urlparse

re = requests.get("http://www.spiegel.de/politik/ausland/venezuela-vier-szenarien-fuer-die-zukunft-des-krisenlandes-a-1145434.html")
print re.