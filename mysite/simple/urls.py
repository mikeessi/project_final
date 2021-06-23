from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('<int:user_id>/', views.messages, name = "messages"),
    path('send/', views.send_message, name = "send"),
    path('search/', views.search, name = "search"),
]