from grab import Grab 
from bs4 import BeautifulSoup

g = Grab() 

resp = g.go('https://www.azlyrics.com/e/eminem.html')
soup = BeautifulSoup(resp.body, 'html.parser')

with open('out', 'w') as f:
    f.write(str(soup.body.prettify()))
