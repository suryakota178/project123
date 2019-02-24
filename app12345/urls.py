from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from app12345 import views

app_name='app12345'

urlpatterns = [
    path('', views.list,name='list'),
    path('create/', views.Create.as_view(),name='create'),
    path('index/',views.index,name='index'),
    path('register/', views.register,name='register'),
    path('login/', views.login1,name='login'),
    path('logout/', views.logout1,name='logout'),
    url(r'^(?P<pk>\d+)/$',views.Detail.as_view(),name='detail'),
    url(r'^update/(?P<pk>\d+)/$',views.Update.as_view(),name='update'),

    url(r'^delete/(?P<pk>\d+)/$',views.Delete.as_view(),name='delete')

]
