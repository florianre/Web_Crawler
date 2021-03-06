import requests
from bs4 import BeautifulSoup

class WebSpider:

    def __init__(self, prohibited_domains=[]):
        self.visited = []
        self.prohibited_domains = prohibited_domains

    def crawl(self, start_url):
        source_code = requests.get(start_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        for link in soup.findAll('a'):
            href = link.get('href')
            # TODO: do domain
            if href not in self.visited:
                self.visited.append(href)
        return self.visited
