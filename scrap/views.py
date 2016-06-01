from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.
def home(request):
	context = {}
	return render(request,'home.html',context)



def scraper(request):
	if request.method == 'POST':
		url = "http://kevin.schaul.io/2011/11/07/tutorial-web-scraping-with-django/"
		html_code = requests.get(url)
		print html_code.content
