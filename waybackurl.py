#!/usr/bin/env python3


#This tool is developed by bhanugoudm041
#Used libraries
import requests as re
import optparse


#Adding options
parser = optparse.OptionParser()
parser.add_option("-b","--banner",help="Print banner",dest="banner")
parser.add_option("-u","--url",help="Enter a URL",dest="url")
parser.add_option("-f","--file",help="Filename",dest="filename")
(options, args) = parser.parse_args()

#Complete program in one function
def myProgram():
	#Without url arguement show error
	if options.url == None:
		print("Shutting down....! Please provide a url with arguements -u or --url")

	#With url arguement
	else:
		def urlParser(uRl):
			data = re.get('http://web.archive.org/cdx/search/cdx?url=' + uRl + '/*&output=json&collapse=urlkey')
			dataList = list(data.json())
			return dataList
		global dataLength; dataLength = len(urlParser(options.url))
		global finalData; finalData = urlParser(options.url)

		#Data without file arguement
		if options.filename == None:
			for i in range(dataLength):
				if i == 0:
					pass
				else:
					print(finalData[i][2])

		#Data with file arguement
		else:
			for i in range(dataLength):
				if i == 0:
					pass
				else:
					file = open(options.filename, "a")
					file.write('\n'+ finalData[i][2])
					file.close()

#Without banner
if options.banner == None  or options.banner == "no" or options.banner == "No":
	myProgram()

#With Banner
elif options.banner == "yes" or options.banner == "Yes":
	print('''

	██     ██  █████  ██    ██ ██████   █████   ██████ ██   ██ ██    ██ ██████  ██         ██████  ██    ██ 
	██     ██ ██   ██  ██  ██  ██   ██ ██   ██ ██      ██  ██  ██    ██ ██   ██ ██         ██   ██  ██  ██  
	██  █  ██ ███████   ████   ██████  ███████ ██      █████   ██    ██ ██████  ██         ██████    ████   
	██ ███ ██ ██   ██    ██    ██   ██ ██   ██ ██      ██  ██  ██    ██ ██   ██ ██         ██         ██    
	 ███ ███  ██   ██    ██    ██████  ██   ██  ██████ ██   ██  ██████  ██   ██ ███████ ██ ██         ██    

	*************************************DEVELOPED BY BHANUGOUD*********************************************
	********************************https://github.com/bhanugoudm041****************************************
	.......................................For Ethical Hackers..............................................
	
	Please wait iam working......!
	''')
	myProgram()
else:
	print("Please choose Yes/No or else remove the --banner or -b arguement. It will output urls without banner")
