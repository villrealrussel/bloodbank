from django.urls import path
from . import views

urlpatterns = [
	path('', views.mainpage, name="home"),
	path('firstpage', views.firstpage, name="firstpage"),
	path('secondpage', views.secondpage, name="secondpage"),
	path('Patient', views.Patient, name="Patient"),
	path('Donor', views.Donor, name="Donor"),
	path('request', views.request, name="request"),
	path('Last', views.Last, name="Last"),
	path('about', views.about, name="about"),


	path('update_blood/<str:pk>/', views.updateblood, name="update_blood"),
	path('delete_blood/<str:pk>/', views.deleteblood, name="delete_blood"),
]

