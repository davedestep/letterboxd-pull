from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup
import CSVWrite
import os.path

class scraper:

#link to rotten 100
    filmweb_top500 = "https://www.rottentomatoes.com/top/bestofrt/"
