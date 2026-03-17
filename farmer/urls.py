from django.urls import path
from . import views

urlpatterns = [
path('',views.dashboard,name="home"),
path('recommend/',views.home,name="recommend"),
path('before_recommendation/',views.before_recommendation,name="before_recommendation"),
path('history/',views.history,name="history"),
path('about/', views.about, name='about'),
]