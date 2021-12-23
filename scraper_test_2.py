import urllib.request
from bs4 import BeautifulSoup


def word_getter():
	for i in range(2):
		url = "https://www.vocabulary.com/dictionary/randomword"

		htmlfile = urllib.request.urlopen(url)
		soup = BeautifulSoup(htmlfile, 'lxml')

		temp = soup.find("div", class_="word-area")
		word = temp.find("h1")
		print(word.get_text())


if __name__ == "__main__":
	word_getter()
