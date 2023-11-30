import requests
from config import set_query, headers

class Movie:
    name = ''
    search_result = []
    year = ''
    wanted_movie = {}
    found = False
    
    def __init__(self, name=None, year=None):
        self.name = name
        self.api_connect()
        if self.found:
            self.year = year
            self.found = self.parsing()
            
    def api_connect(self):
        endpoint=set_query(query=self.name)
        response = requests.get(endpoint, headers=headers)
        if response.status_code in range(200, 299):
            data = response.json()
            results = data['results']
            if len(results) > 0:    
                self.search_result = results
                self.found = True
            return True
        else:
            raise Exception('Can\'t connect to api')
    
    def parsing(self):
        if len(self.search_result) == 1:
            self.wanted_movie = self.search_result[0]
            return True
        else:
            for movie in self.search_result:
                if 'release_date' in movie.keys():
                    movie_date = movie['release_date']
                    movie_year = movie_date[:4]
                    if movie_year ==  self.year:
                        if movie['title'] == self.name:
                            self.wanted_movie = movie
                            return True
            return False
    
    def selector(self):
        selected_movie = {}
        if self.found:
            selected_movie['Original Language'] = self.wanted_movie['original_language']
            selected_movie['Overview'] = self.wanted_movie['overview']
            selected_movie['Popularity'] = self.wanted_movie['popularity']
            selected_movie['Release Date'] = self.wanted_movie['release_date']
            selected_movie['Vote Average'] = self.wanted_movie['vote_average']
            selected_movie['Vote Count'] = self.wanted_movie['vote_count']
        else:
            selected_movie['Original Language'] = '-'
            selected_movie['Overview'] = '-'
            selected_movie['Popularity'] = '-'
            selected_movie['Release Date'] = '-'
            selected_movie['Vote Average'] = '-'
            selected_movie['Vote Count'] = '-'
        return selected_movie
