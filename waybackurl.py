#!/usr/bin/env python3


#This tool is developed by bhanugoudm041
#Used libraries
import requests as re
import optparse

#Adding options
parser = optparse.OptionParser()
parser.add_option("-u","--url",help="Enter a URL",dest="url")
parser.add_option("-f","--file",help="Filename",dest="filename")
(options, args) = parser.parse_args()
#all urls list
finalUrls=[]

#Main class to get data
class myProgram:
	def __init__(self,url):
		self.url=url
	def urlParser(self):
		data = re.get('http://web.archive.org/cdx/search/cdx?url=' + self.url + '/*&output=json&collapse=urlkey')
		dataList = list(data.json())
		finalUrls.append(dataList)

fetch=myProgram(options.url)

#Handling data
try:
	if options.filename == None:
		fetch.urlParser()
		dataLength = len(finalUrls[0])
		for i in range(1,dataLength):
			url=finalUrls[0][i]
			print(url[2])

	else:
		fetch.urlParser()
		dataLength = len(finalUrls[0])
		for i in range(1,dataLength):
			url=finalUrls[0][i]
			file=open(options.filename, "a")
			file.write(url[2]+'\n')
			file.close()
			print(url[2])
except TypeError:
	print("Run ./waybackurl.py --help or ./waybackurl.py -h")
