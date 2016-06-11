from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import json
from django.http import JsonResponse
# Create your views here.
def home(request):
	context = {}
	return render(request,'home.html',context)



def scraper(request):
	if request.method == 'POST':
		amazon_url = "http://www.amazon.in/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords="

		try:
			query = json.loads(request.body).get('query')
		except:
			query = ""

		if query:
			if " " in query :
				query = query.replace(" " , "+")
			print query
			amazon_url = amazon_url + query
			amazon_html = requests.get(amazon_url)
			amazon_data = BeautifulSoup(amazon_html.content, "html.parser")
			x = amazon_data.find_all("li", {"class":"s-result-item celwidget"})
			models = []
			price = []
			for i in x:
				models.append(i.contents[0].find_all("a", {"class":"a-link-normal s-access-detail-page  a-text-normal"})[0].text)
				# print i.contents[0].find_all("a", {"class":"a-link-normal s-access-detail-page  a-text-normal"})[0].text		
				# print i.contents[0].find_all("span", {"class":"a-size-base a-color-price s-price a-text-bold"})[0].text
				try:
					price.append(i.contents[0].find_all("span", {"class":"a-size-base a-color-price s-price a-text-bold"})[0].text)
				except:
					price.append("Price not mentioned")

			amazon = {"models" : models , "price" : price}

			return JsonResponse({'amazon':amazon})



