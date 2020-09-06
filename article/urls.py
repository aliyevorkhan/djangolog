from django.contrib import admin
from django.urls import path

from . import views

app_name = "article"

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_article/', views.add_article, name='add_article'),
    path('<int:id>/',views.detail, name='detail')
]
