from django.conf.urls import url,include
from .views import *
urlpatterns = [
    url(r'^home/$',home , name="home" ),
    url(r'^scrap/$',scraper , name="scraper" ),

]
