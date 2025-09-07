import requests
response = requests.get('https://api.themoviedb.org/3/movie/550?api_key=4ffe78b827baee19a289403b8e11b730')
print(response.status_code, response.text)
