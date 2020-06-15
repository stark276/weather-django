from django.shortcuts import render
import requests

# Create your views here.
def index(request):
 url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=3793abe0393da66929acbd9cc350ab91'
 city = 'Los Angeles'
 r = requests.get(url.format(city)).json()

 city_weather = {
  'city' : city,
  'temperature' : r['main']['temp'],
  'description': r['weather'][0]['description'],
  'icon' : r['weather'][0]['icon']
 }
 context = {'city_weather':city_weather}
 print(city_weather)
 return render(request , 'weather/home.html', context)
