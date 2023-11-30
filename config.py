import os

FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
URL_FILE = os.path.join(BASE_DIR, 'url.html')
BOXOFFICE_DIR = os.path.join(BASE_DIR, 'BoxOffice')

os.makedirs(BOXOFFICE_DIR, exist_ok=True)

url = "https://www.boxofficemojo.com/year/world"

api_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ODNlNTNmNDU1Zjk2ZDYzZTUxZGE5YWNiNzE1OTQyOCIsInN1YiI6IjYzMDE2MTVkODM5ZDkzMDA3ZTRjMzVkMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Ctlf0QNlwjNRCOyzjZVnZW0A_xbEsv_0QoSfdRU_ZKI'
api_version = 3
api_base_url = f'https://api.themoviedb.org/{api_version}'
seaching_path = "/search/movie"
movie_path = "/movie/"
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_token}"
}
def set_query(query):
    return f"{api_base_url}{seaching_path}?query={query}"