from accountapp.views import AccountCreateView
from django.urls import path
from accountapp.views import hello_world
from django.contrib.auth.views import LoginView, LogoutView

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name='create'),
    
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]