from django.urls import path
from . import views

urlpatterns = [
    path('rest_data', views.get_json,name="rest_data"),

]