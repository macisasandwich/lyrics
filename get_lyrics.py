from grab import Grab
from bs4 import BeautifulSoup

g = Grab()

resp = g.go('https://www.azlyrics.com/lyrics/eminem/tragicendings.html')
soup = BeautifulSoup(resp.body, 'html.parser')

# print(soup.body.contents)

with open('out', 'w') as f:
	f.write(str(soup.find("div", class_=False, id=False).get_text()))
