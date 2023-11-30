import requests
import os
import pandas as pd
from api_scrape import Movie
from requests_html import HTML
from datetime import datetime
from config import BOXOFFICE_DIR, url, URL_FILE

class Scraper:
    data = []
    year = str(datetime.now().year)
    url = ''
    
    def __init__(self, year=str(datetime.now().year)):
        if year != self.year:
            self.year = str(year)
        self.url = url + f'/{self.year}'
        if self.url_to_txt():
            self.parsing()
            self.store_to_csv()
        else:
            print("Can't connect to url")
            
    def url_to_txt(self, filename=URL_FILE):
        r = requests.get(self.url)
        if r.status_code in range (200, 299):
            html_text = r.text
            with open(filename, 'w', encoding="utf-8") as file:
                file.write(html_text)   
            return html_text
        return False

    def parsing(self):
        html_text = self.url_to_txt()
        r_html = HTML(html=html_text)
        table_class = '.imdb-scroll-table-inner'
        table = r_html.find(table_class)    
        if len(table) == 1:
            parsed_table = table[0]
            rows = parsed_table.find('tr')  
            header_row = rows[0]
            header_cols = header_row.find('th')
            column_names = [x.text for x in header_cols]
            for index, name in enumerate(column_names):
                if name == "%":
                    column_names[index] = column_names[index-1] + " " + name
            table_data = []   
            for row in rows[1:]:
                columns = row.find('td')    
                row_data = {} 
                index = 0
                for column in columns:
                    row_data[column_names[index]] = column.text
                    index += 1
                movie = Movie(name=row_data['Release Group'], year=self.year) 
                row_data.update(movie.selector())
                table_data.append(row_data)    
            self.data = table_data     
                      
    def store_to_csv(self):
        df = pd.DataFrame(self.data)
        csv_file = os.path.join(BOXOFFICE_DIR, f'{self.year}.csv')  
        if os.path.isfile(csv_file):  
            print("CSV file already exists")
        else:
            df.to_csv(csv_file, index=False)
            print(f'Box Office {self.year} saved as csv file')
