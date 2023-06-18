from django.urls import path

from .views import login

urlpatterns = [
    path('login/', login.login_view, name='login'),
    path('logout/', login.logout_view, name='logout'),
    path('top/', login.top_view, name='top'),
]