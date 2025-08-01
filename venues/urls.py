from django.urls import path
from venues import views
urlpatterns = [
    path('',views.Home,name='home')
]