from django.contrib import admin
from django.urls import path

from . import views
from .views import templateBuilderView, indexView, profileView, idinfo, redirect_view, userinfo, displayinfo, updateinfo, loadtemplate

app_name = 'cc'
urlpatterns = [
    path('', indexView, name='index'),
    path('portal/', redirect_view),
    path('profile/', profileView, name='profile'),
    path('loadtemplate/', loadtemplate, name='loadtemplate'),
    path('userinfo/', userinfo, name='userinfo'),
    path('updateinfo/', updateinfo, name='updateinfo'),
    path('displayinfo/', displayinfo, name='displayinfo'),
    path('template_builder/', templateBuilderView, name='templateBuilder')
]