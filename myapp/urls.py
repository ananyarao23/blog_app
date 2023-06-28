from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.index, name='home'),
    path('explore', views.explore, name='explore'),
    path('contact', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login', views.login, name='login'),
    path('add_blog/', views.add_blog, name="add_blog")
]
