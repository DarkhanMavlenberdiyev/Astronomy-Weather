from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect
from django.http import HttpResponse

def index(request):
	nasaid = '13JhcAALadUOjtoDFagOndelGkKHqRX6aOXD7xwx'
	url = 'https://epic.gsfc.nasa.gov/api/images.php'

	res= requests.get(url).json()
	if(request.method=='POST'):
		
		res = requests.get('https://epic.gsfc.nasa.gov/api/images.php?date='+str(request.POST['date'])).json()
		

	alldates = requests.get('https://epic.gsfc.nasa.gov/api/natural/all').json()
	dates = []
	for i in alldates:
		dates.append(i['date'])

	epics = []

	for i in res:
		dic = {
			'date':i['date'],
			'img':'https://epic.gsfc.nasa.gov/epic-archive/jpg/'+i['image']+'.jpg',
			'caption':i['caption'],
			'id':i['identifier']
		}

		epics.append(dic)


	context = {'epics':epics,'dates':dates}
	return render(request,'epic/index.html',context)