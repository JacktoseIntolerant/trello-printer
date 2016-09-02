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
	file.write("\t<link rel=\"stylesheet\" type=\"text/css\" href=\"main.css\">\n")
	file.write("</head>\n")
	file.write("<body>\n\n")
	# good stuff starts here
	file.write("<div id=\"container-wrapper\">\n")	# double-div to adjust width
	file.write("<div id=\"container\">\n")	# whole body div
	file.write("\t<div id=\"header\">\n")		# holds title and description
	file.write("\t\t<h1>" + card['name'] + "</h1>\n")
	file.write("\t\t<p id=\"description\">" + card['desc'] + "</p>\n")
	file.write("\t</div>\n")					# id=header
	file.write("\t<div id=\"content\">\n")	# holds all the checklists
	for checklist in card['checklists']:
		file.write("\t\t<div class=\"checklist\">\n")	# each checklist gets its own div
		file.write("\t\t\t<h3>" + checklist['name'] + "</h3>\n")	# checklist name
		file.write("\t\t\t<ol>\n")					# start a list
		for item in checklist['checkItems']:
			file.write("\t\t\t\t<li>")				# start a list item
			if item['state'] == 'incomplete':	# unchecked in trello
				file.write(htmlCheckbox['open'])
			elif item['state'] == 'complete':	# checked in trello
				file.write(htmlCheckbox['checked'])
			file.write("\t" + item['name']) 	# the checklist item text
			file.write("</li>\n")	# end the list item, like a good boy
		file.write("\t\t\t</ol>\n")		# end the list
		file.write("\t\t</div>\n")		# class=checklist
	file.write("\t</div>\n")			# id=content
	file.write("</div>\n")			# id=container
	file.write("</div>\n")			# id=container-wrapper
	# finish up the html page
	file.write("\n</body>\n")
	file.write("</html>\n")


# try to get the input file, or fail with message
try:
	jsonFile = open(sys.path[0] + "\card.json", 'r')
except:
	sys.exit("Error opening card.json")

# try to start the input file, or fail with message
try:
	htmlFile = open(sys.path[0] + "\card.html", 'w')
except:
	sys.exit("Error writing card.html")

inputCard = json.load(jsonFile)		# turn json text file into python list
jsonFile.close()					# now done with json text file
printCardHtml(inputCard, htmlFile)	# run the above function (writing to the html file)
htmlFile.close()					# now done with the html output file
print("card.json converted to card.html")	# hooray
sys.exit(0)							# exit successfully