from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required,permission_required



urlpatterns=[
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('privacy/',views.privacy,name='privacy'),
    path('our_services/',views.our_services,name='our_services'),
    path('our_team',views.our_team,name='our_team'),
    path('profile/',views.profile,name='profile'),
    path('search/',views.search,name='search'),
    



]