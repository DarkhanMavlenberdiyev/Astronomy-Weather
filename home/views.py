from django.shortcuts import render

import requests
from django.http import HttpResponseRedirect


def home(requests):
	return render(requests,'home/index.html')