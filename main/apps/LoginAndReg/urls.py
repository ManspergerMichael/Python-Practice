from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^home', views.index), 
    #random word
    url(r'^random_word', views.word),
    url(r'^random_word/refresh', views.refresh),
    #survey
    url(r'^survey', views.survey),
    url(r'^process', views.submit),
    url(r'^result', views.result)    
    
]
