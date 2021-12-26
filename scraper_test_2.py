import urllib.request
from bs4 import BeautifulSoup


if __name__ == "__main__":
	for i in range(2):
		url = "https://www.vocabulary.com/dictionary/randomword"

		htmlfile = urllib.request.urlopen(url)
		soup = BeautifulSoup(htmlfile, 'lxml')
		area_finder_in_html = soup.find("div", class_="word-area")
		specific_word = area_finder_in_html.find("h1")
		word_into_string_maker = specific_word.get_text().split()
		print(word_into_string_maker)
