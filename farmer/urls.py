from django.urls import path
from . import views

urlpatterns = [
path('',views.dashboard,name="home"),
path('recommend/',views.home,name="recommend"),
path('before_recommendation/',views.before_recommendation,name="before_recommendation"),
path('history/',views.history,name="history"),
path('about/', views.about, name='about'),
path('delete_history/<int:id>/', views.delete_history, name='delete_history'),
path('fr/', views.fertilizer_view, name='fertilizer_recommendation'),
path('delete_fhistory/<int:id>/', views.delete_fhistory, name='delete_fhistory'),

]