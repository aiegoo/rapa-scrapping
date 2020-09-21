from bs4 import BeautifulSoup

print('html.parser : ', BeautifulSoup("<a><b/></a>", "html.parser"))