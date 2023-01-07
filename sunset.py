def sett(x):
     # importing requests and json
     import requests, json,datetime
     x=str(x)
     # base URL
     BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
     API_KEY='4961dfe8dac0eb120ff56f0dd8af8f0a'
     URL = BASE_URL + "q=" + x + "&appid=" + API_KEY
     st=""
     # HTTP request
     response = requests.get(URL)
     # checking the status code of the request
     if response.status_code == 200:
          # getting data in the json format
          data = response.json()
          sunset = datetime.datetime.fromtimestamp(int(data['sys']['sunset']))
          return sunset
     else:
          return "ERROR"
