from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^index/', views.index, name='index'),

    url(r'^login/', views.loginpage, name='login'),

    url(r'^loginresult', views.loginresult, name='loginresult'),

    url(r'^logout/', views.logoutpage, name='logoutpage'),

    url(r'^register/', views.register, name='register'),

    url(r'^registerresult', views.registerresult, name='registerresult'),

    url(r'^(?P<home_id>[0-9]+)/homepage/', views.personalhomepage, name='personalhomepage'),

    url(r'^information/', views.personalinformation, name='personalinformation'),

    url(r'^writeblog/', views.writeblogpage, name='writeblogpage'),

    url(r'^writeblog', views.writeblog, name='writeblog'),

    url(r'^(?P<b_id>[0-9]+)/viewblog/', views.viewblog, name='viewblog'),
]
