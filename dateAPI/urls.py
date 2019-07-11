from django.conf.urls import url 
from . import views

urlpatterns = [
	# creating url view for app timeAPI,
	# which acess get method define in file views.py 
	url(r'^$', views.get, name = 'get'),
]