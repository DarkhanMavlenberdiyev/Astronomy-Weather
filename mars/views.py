from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect
from django.http import HttpResponse
def index(request):
	nasaid = '13JhcAALadUOjtoDFagOndelGkKHqRX6aOXD7xwx'
	apodrequest = 'https://api.nasa.gov/planetary/apod?&api_key='+nasaid


	if(request.method == "POST"):
		apodrequest = 'https://api.nasa.gov/planetary/apod?date={}&api_key='+nasaid
		res = requests.get(apodrequest.format(str(request.POST.get('date')))).json()
		infs = {
		'date':res['date'],
		'explanation':res['explanation'],
		'media_type':res['media_type'],
		'url':res['url'],
		'title':res['title'],
		
		}
		if res['media_type']=='video':
			infs['playlist']=res['url'].split('/')[-1].split('?')[0]

		context = {
			'apod':infs
		}
		return render(request,'mars/index.html',context)
	res = requests.get(apodrequest).json()
	
	infs = {
		'date':res['date'],
		'explanation':res['explanation'],
		'media_type':res['media_type'],
		'url':res['url'],
		'title':res['title'],
		
	}
	if res['media_type']=='video':
		infs['playlist']=res['url'].split('/')[-1].split('?')[0]

	context = {
		'apod':infs
	}

	return render(request,'mars/index.html',context)


def mars(request):
	nasaid = '13JhcAALadUOjtoDFagOndelGkKHqRX6aOXD7xwx'
	url = 'https://api.nasa.gov/insight_weather/?api_key={}&feedtype=json&ver=1.0'.format(nasaid)
	res = requests.get(url).json()
	
	lis = []

	for key in res['sol_keys']:
		
		mars = {
			'sol':key,
			'avTemp':res[key]['AT']['av'],
			'minTemp':res[key]['AT']['mn'],
			'maxTemp':res[key]['AT']['mx'],
			'avHWS':res[key]['HWS']['av'],
			'minHWS':res[key]['HWS']['mn'],
			'maxHWS':res[key]['HWS']['mx'],
			'avPres':res[key]['PRE']['av'],
			'minPres':res[key]['PRE']['mn'],
			'maxPres':res[key]['PRE']['mx'],
			'season':res[key]['Season']
		}
		lis.append(mars)

	context = {'weather':lis}

	return render(request,'mars/mars.html',context)

