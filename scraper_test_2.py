import urllib.request
from bs4 import BeautifulSoup


if __name__ == "__main__":
	counter = int(input("Enter number: "))
	
	# Do for given number of times
	for n in range(counter):
		# Save url as string and parse webpage with BeautifulSoup
		url = "https://www.vocabulary.com/dictionary/randomword"
		htmlfile = urllib.request.urlopen(url)
		soup = BeautifulSoup(htmlfile, 'lxml')
		
		# Find specific word
		area_finder_in_html = soup.find("div", class_="word-area")
		specific_word = area_finder_in_html.find("h1")
		
		# Conver word into string
		word_into_string_maker = specific_word.get_text().split()
		word_as_string = ' '.join([str(elem) for elem in word_into_string_maker])
		
		print(word_as_string)
