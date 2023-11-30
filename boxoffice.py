import sys
from scrape import Scraper

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print('It will take a little longer...')
        BoxOffice = Scraper(year=sys.argv[1])
    else:
        print("Year of the BoxOffice wanted not given")