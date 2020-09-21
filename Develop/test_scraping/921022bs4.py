#import bs4
from bs4 import BeautifulSoup

s_html = '<html><head></head><body>Sacr&eacuter; bleu/body></html>'
soup = BeautifulSoup(markup=s_html)
print(type(soup), soup)