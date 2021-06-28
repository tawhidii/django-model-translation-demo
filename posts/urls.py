from django.urls import path
from .views import post_index
urlpatterns = [
    path('',post_index,name='post-index')
]