from django.urls import re_path,include
from notesapp.views import *
urlpatterns = [
    re_path(r'^$',LoginView.as_view(),name="login"),
    re_path(r'^menu/(?P<username>\w+)/$',MainView.as_view(),name="menu"),
    re_path(r'^menu/(?P<username>\w+)/logout/$',LogoutView.as_view(),name="logout"),
    re_path(r'^menu/(?P<username>\w+)/insert/$',InsertView.as_view(),name="insert"),
    re_path(r'^menu/(?P<username>\w+)/display/$',DisplayView.as_view(),name="display"),    
    re_path(r'^menu/(?P<username>\w+)/delete/$',DeleteView.as_view(),name="delete"),
    re_path(r'^menu/(?P<username>\w+)/update/$',UpdateView.as_view(),name="update"),        
    
]
