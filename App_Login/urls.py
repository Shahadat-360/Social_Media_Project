from . import views
from django.urls import path

app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.signup, name='signup')
]
