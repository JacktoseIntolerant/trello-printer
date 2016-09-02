# This is a little script to print out the juicy parts of Trello cards.
# https://trello.com/ is a very nice to-do/project management app, but it is
# painfully hard to get checklists out in a sensible format.
# 
# input: "card.json" in the same folder
# output: "card.html" in the same folder
# 
# copyright Jack Enneking, 2016-09-01

import sys
import json

htmlCheckbox = {
	'open':		'&#9744;',	# Ballot box
	'checked':	'&#9745;',	# Ballot box with check
	'Xed':		'&#9746;',	# Ballot box with X
}

def printCardHtml(card, file):
# takes bits and pieces of card and writes them, wrapped in html
	# write the html top junk
	file.write("<html>\n")
	file.write("<head>\n")
	file.write("\t<title>" + card['name'] + "</title>\n")
	file.write("</head>\n\n")
	file.write("<body>\n\n")
	# good stuff starts here
	file.write("<div id=\"container\">\n")	# whole body div
	file.write("<div id=\"header\">\n")		# holds title and description
	file.write("<h1>" + card['name'] + "</h1>\n")
	file.write("<p>" + card['desc'] + "</p>\n")
	file.write("</div>\n")					# id=header
	file.write("<p></p>\n")					# replace this with div padding later
	file.write("<div id=\"content\">\n")	# holds all the checklists
	for checklist in card['checklists']:
		file.write("\n<div class=\"checklist\">\n")	# each checklist gets its own div
		file.write("\t<h3>" + checklist['name'] + "</h3>\n")	# checklist name
		file.write("\t<ol>\n")					# start a list
		for item in checklist['checkItems']:
			file.write("\t\t<li>")				# start a list item
			if item['state'] == 'incomplete':	# unchecked in trello
				file.write(htmlCheckbox['open'])
			elif item['state'] == 'complete':	# checked in trello
				file.write(htmlCheckbox['checked'])
			file.write("\t" + item['name']) 	# the checklist item text
			file.write("</li>\n")	# end the list item, like a good boy
		file.write("\t</ol>\n")		# end the list
		file.write("</div>\n")		# class=checklist
	file.write("</div>\n")			# id=content
	file.write("</div>\n")			# id=container
	# finish up the html page
	file.write("\n</body>\n")
	file.write("</html>\n")

# try to get the input file, or fail with message
try:
	jsonFile = open("card.json", 'r')
except:
	sys.exit("Error opening card.json")

# try to start the input file, or fail with message
try:
	htmlFile = open("card.html", 'w')
except:
	sys.exit("Error writing card.html")

inputCard = json.load(jsonFile)		# turn json text file into python list
jsonFile.close()					# now done with json text file
printCardHtml(inputCard, htmlFile)	# run the above function (writing to the html file)
htmlFile.close()					# now done with the html output file
print("card.json converted to card.html")	# hooray
sys.exit(0)							# exit successfully