import requests
import os
import sys
import datetime
import pandas as pd
from requests_html import HTML

FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
URL_FILE = os.path.join(BASE_DIR, 'url.html')
CSV_DIR = os.path.join(BASE_DIR, 'BoxOffice')
os.makedirs(CSV_DIR, exist_ok=True)

url = "https://www.boxofficemojo.com/year/world"
now = datetime.datetime.now()

class Parser:
    data = []
    year = now.year
    url = ''
    def __init__(self, year=str(now.year)):
        if year != now.year:
            self.year = str(year)
        self.url = url + f'/{self.year}'
        self.url_to_txt()
        self.parsing()
        
    #### saving url content to html file for future parsing ####
    def url_to_txt(self, filename=URL_FILE):
        r = requests.get(self.url)
        if r.status_code == 200:
            html_text = r.text
            with open(filename, 'w', encoding="utf-8") as file:
                file.write(html_text)   
            return html_text
        else:
            raise Exception("Can't connect to url")

    def parsing(self):
        html_text = self.url_to_txt()
        r_html = HTML(html=html_text)
        table_class = '.imdb-scroll-table-inner'
        table = r_html.find(table_class)    ### finding table ###
        
        if len(table) == 1:
            parsed_table = table[0]
            rows = parsed_table.find('tr')  ### parsing by rows ###
            header_row = rows[0]
            header_cols = header_row.find('th')
            columns_name = [x.text for x in header_cols]    ### saving first row as columns names ###
            table_data = []
            table_data.append(columns_name)
            for row in rows[1:]:
                columns = row.find('td')    ### parsing  by columns ###
                row_data = []
                for column in columns:
                    row_data.append(column.text)
                table_data.append(row_data)          
        self.data = table_data  ### saving data as class atribute ###
    
    def store_to_csv(self):
        df = pd.DataFrame(self.data[1:], columns=self.data[0])
        csv_file = os.path.join(CSV_DIR, f'{self.year}.csv')
        if os.path.isfile(csv_file):  
            print("CSV file already exists")
        else:
            df.to_csv(csv_file, index=False)
            print(f'Box Office {self.year} saved as csv file')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        BoxOffice = Parser(year=sys.argv[1])
        BoxOffice.store_to_csv()
    else:
        BoxOffice = Parser()
        BoxOffice.store_to_csv()
    