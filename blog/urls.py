from django.urls import path
from .import views #import view from views.py  
#the . before import means import from the same directory


#path er parameter e 1st parameter e web url path
#2nd parameter e view and corresponding view function
#3rd parameter e name of the view path 

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
]

