from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
app_name = 'hello'

urlpatterns = [
    path('', views.hello),
]