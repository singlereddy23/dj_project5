from django.urls import path
from app1 import views
# Create your views here.
app_name="app1"

urlpatterns = [
    path('index1/',views.index,name="index"),
    path("sample1/",views.sample1,name="sample1"),
]