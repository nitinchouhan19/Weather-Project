from django.shortcuts import render , redirect
import requests

# Create your views here.
def index(request):
  if request.method == 'POST':
    city = request.POST['city']
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=6631a107841d533f37a21bf209b1e5d3&units=metric'
    data = requests.get(url).json()
    try:
      weatherdata = { 
        'city' : data['name'] ,  
        'weather':data['weather'][0]['icon'],
        'temperature':data['main']['temp'],
        'pressure':data['main']['pressure'],
        'humidity':data['main']['humidity'],
        'latitude':data['coord']['lat'],
        'longitude':data['coord']['lon'],
        'description':data['weather'][0]['description'],
        'icon': data['weather'][0]['icon']
      }
    except:
      return redirect('index')
      
    context  = { 'weatherdata' : weatherdata }
    return render(request , 'index.html',context) 
  context  = {}
  return render(request , 'index.html',context) 