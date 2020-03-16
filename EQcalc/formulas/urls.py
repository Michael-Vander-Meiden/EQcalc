from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('first',views.first, name = 'first'),
	path('first_db',views.first_db, name = 'first'),
	path('equations', views.equationPage, name = 'equationPage'),
	path('forms', views.formPage, name = 'formPage'),
	path('calculations', views.calcPage, name = 'calcPage')
	
] 