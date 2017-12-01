import urllib

def read_text():
	path = 'C:\Users\User\Desktop\Jesus Bibieca\profanity_checker\movie quotes.txt'
	quotes = open(path)
	content_of_file = quotes.read()
	# print content_of_file
	quotes.close()
	check_profanity(content_of_file)

def check_profanity(text_to_check):
	url = 'http://www.wdylike.appspot.com/?q=' 
	connection = urllib.urlopen(url + text_to_check)
	output = connection.read()
	# print output
	if "true" in output: print "Profanity Alert!"
	elif "false" in output: print "The document has no curse words."
	else: print "Could not scan the document properly" 
	connection.close()

read_text()