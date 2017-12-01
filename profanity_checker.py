def read_text():
	path = 'C:\Users\User\Desktop\Jesus Bibieca\profanity_checker\movie quotes.txt'
	quotes = open(path)
	content_of_file = quotes.read()
	return content_of_file
	quotes.close()


print read_text()