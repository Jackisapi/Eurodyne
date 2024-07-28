from urllib.request import urlopen
from bs4 import BeautifulSoup


class dataFetcher:
    def __init__(self, url):
        # Later Going To use something like the duck duck go api or smthn to get a set of urls this is temp
        self.html = urlopen(url).read()
        # intilises bs4 as soup for html parsing
        self.soup = BeautifulSoup(self.html, features="html.parser")

    def txt_extractor(self):
        # opnens the html of the link and searches for the <script> and <style> tags to remove them and there contents
        for script in self.soup(["script", "style"]):
            script.extract()

        # Strips the remaining text out of the
        text = self.soup.get_text()

        # Strips white space and stuff from text to prep for returning
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = "\n".join((chunk for chunk in chunks if chunk))
        return text


print(dataFetcher("https://en.wikipedia.org/wiki/Office_Assistant").txt_extractor())
