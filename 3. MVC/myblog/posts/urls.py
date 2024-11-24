from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.posts_list, name='list'),
    path('read/<slug:slug>', views.posts_read, name='read'),
]
