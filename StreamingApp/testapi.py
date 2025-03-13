import http.client
import requests
from django.conf import settings

if __name__ == "__main__":
    '''
    import http.client

    conn = http.client.HTTPSConnection("moviesdatabase.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "5b53d4ee75msh4771856dfa5700fp12aa00jsna9dcb35afef8",
        'x-rapidapi-host': "moviesdatabase.p.rapidapi.com"
    }

    conn.request("GET", "/titles", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    '''


    url = "https://api.themoviedb.org/3/movie/latest"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    print(response.text)
    print("****************************")
    print(settings.SECRET_KEY)
    print("response.text")
