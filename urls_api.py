from django.urls import path,include
from .views import *
urlpatterns = [
    path('todo/' , TodoView.as_view())
]