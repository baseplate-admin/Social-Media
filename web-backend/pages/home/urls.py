from django.urls import path
from .views import *

# urlpatterns = []
urlpatterns = [
    path("", home_page, name="home_page"),
]
