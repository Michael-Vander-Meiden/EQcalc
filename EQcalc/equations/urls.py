from django.urls import path
from . import views

urlpatterns = [
	path('<int:eq>/', views.index, name = 'index'),
	path('<int:eq>/<int:inv>/', views.index, name = 'index'),
	path('', views.index, name = 'index'),
	
	]
