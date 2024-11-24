from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list),
    path('postread/<slug:slug>', views.posts_read),
]
