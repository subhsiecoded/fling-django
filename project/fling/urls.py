from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.fling_list,
          name= 'fling_list'),
    path('create/', views.fling_create, 
         name= 'fling_create'),
    path('<int:fling_id>/edit/', views.fling_edit,
          name= 'fling_edit'), #take id inside <> brackets, then mention the data type and the variable (primary key id here)
    path('<int:fling_id>/delete/', views.fling_delete, 
         name= 'fling_delete'),
      path('register/', views.register, 
            name= 'register'), #also you need to set the urls in the settings.py file to redirect the user for login and register 
] 

#let's make a view to test a web page 