import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
from datetime import *
from .forms import ContactForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=04cb974bea3726672dd112ff79e5e94b'
    city='San Francisco'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()
        f=r['main']['temp']
        cel=(f-32)*(5/9)
        
        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
            'c':cel  
        }
        #print(city_weather)
        
        #f=city_weather['temperature']
        
        #c=(f-32)*(5/9)
        #print(f)
        weather_data.append(city_weather)
        
    #print(weather_data)
    context = {'weather_data' : weather_data,'form' : form}
    return render(request, 'weather/weather.html',context)

today = datetime.now().date()

def about(request):
    return render(request,"weather/about.html",{'today':today})

def contact(request):
	form_class=ContactForm
	return render(request,"weather/contact.html",{'form':form_class})
    