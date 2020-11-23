import requests
from bs4 import BeautifulSoup
import pprint

path_1 = 'https://news.ycombinator.com/news'
path_2 = 'https://news.ycombinator.com/news?p=2'
paths = [path_1, path_2]


def get_response(paths):
	links = []
	subtext = []
	for path in paths:
		res = requests.get(path)
		soup = BeautifulSoup(res.text, 'html.parser')
		links += soup.select('.storylink')
		subtext += soup.select('.subtext')
	return create_custom_hn(links, subtext)


def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = item.get_text()
		href = item.get('href', None)
		vote = subtext[idx].select('.score')
		# After print vote, we see vote is a list with 1 element, not a tag
		# To use method get_text. we get the first element in the vote
		if vote:
			points = int(vote[0].get_text().split(' ')[0])
			if points >99:
				hn.append({'title':title, 'link': href, 'votes': points})
	return sort_stories_by_votes(hn)

if __name__ == '__main__':
	pprint.pprint(get_response(paths))



