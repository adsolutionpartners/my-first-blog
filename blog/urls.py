from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]