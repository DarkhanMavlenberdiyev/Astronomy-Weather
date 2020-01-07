from django.shortcuts import render
from .models import City
import requests
from django.http import HttpResponseRedirect
from django.http import HttpResponse

'''
http://api.worldweatheronline.com/premium/v1/weather.ashx?q=Taraz&format=json&key=84272b8662fc4036a9e162005192711
'''


from .forms import CityForm
def index(request):
	appid= '2a27f8c8e6ddfe668c64b4e79f49b2c5'
	appid2= '84272b8662fc4036a9e162005192711'
	appidIP= '50968345a72c49a7a754cdce0c284b80'
	url  = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="+appid 
	mapid = '2a27f8c8e6ddfe668c64b4e79f49b2c5';
	url2 = "http://api.openweathermap.org/data/2.5/forecast?id=1526384&appid=2a27f8c8e6ddfe668c64b4e79f49b2c5"#5day
	
	if(request.method == "POST"):
		form = CityForm(request.POST)
		form.save()


	

	form = CityForm()


	

	for city in City.objects.all():
		if City.objects.filter(name=city.name).count()>1:
			city.delete()
	


	cities = list(City.objects.all())

	
	while(len(cities)>3):
		cities.pop(0)

	all_cities = []

	for city in cities[::-1]:

		try:
			res = requests.get(url.format(city.name)).json()
	
			city_info = {
			'city':city.name,
			'temp':res['main']['temp'],
			"icon":res['weather'][0]['icon']
			}
			all_cities.append(city_info)
		except KeyError:
			city.delete()
	
	kask = requests.get(url.format("Kaskelen")).json()
	
	kask_info = {
			'city':'Kaskelen',
			'temp':kask['main']['temp'],
			"icon":kask['weather'][0]['icon'],
			'country':kask['sys']['country'],
			'pressure':kask['main']['pressure'],
			'humidity':kask['main']['humidity'],
			'maxTemp':kask['main']['temp_max'],
			'minTemp':kask['main']['temp_min'],
			'windspeed':kask['wind']['speed'],
			'winddeg':kask['wind']['deg'],
			'description':kask['weather'][0]['description'],
			}

	context = {'all_info': all_cities ,'form':form,'kask':kask_info}

	return render(request,'weather/index.html',context)

def delete_city(request,name):
	city = City.objects.get(name=name)
	city.delete()
	return HttpResponseRedirect('/weather')

def check_city(request):
	appid= '2a27f8c8e6ddfe668c64b4e79f49b2c5'
	url  = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="+appid 
	name = request.GET['name']
	print(name)
	cities = list(City.objects.all())
	city = City(name=name)
	try:
		res = requests.get(url.format(name)).json()
		city_info = {
			'city':name,
			'temp':res['main']['temp'],
			"icon":res['weather'][0]['icon']
			}
		return HttpResponse('Такой город существует')
	except KeyError:
		return HttpResponse('Такой город не существует')

		 