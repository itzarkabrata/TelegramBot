def show_main(message):
     import requests
     W_Url = "https://api.openweathermap.org/data/2.5/weather?"
     API_KEY = '4961dfe8dac0eb120ff56f0dd8af8f0a'
     URL = W_Url + "q=" +message+ "&appid=" + API_KEY

     City=""
     response = requests.get(URL)

     #---->Condition request
     if response.status_code == 200:
          #---->formating to Json
          data = response.json()
          #---->gettingt ta dictionary
          main = data['main']
          #----->Temperature
          temp = (int(main['temp'])-273.0)
          #----->Visibilty
          visibility = (data['visibility'])
          #---->Humidity
          humid = (main['humidity'])
          #---->Status
          status = data['weather']

          City+=f"-----{c}-----"+'\n'+f"Temperature: {temp} Celsius"+'\n'+f"Humidity: {humid} g/kg"+'\n'+f"Visibility: {visibility} "+'\n'+f"Weather Condition: {status[0]['description']} "
          
          return(City)
     else:
          #Invalid City message
          return("Enter  a  Valid City")