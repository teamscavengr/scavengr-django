from django.conf.urls import url
from places import views

urlpatterns = [
    url(r'^$', views.Places.as_view()),
    url(r'^(?P<pk>[\w]+)/$', views.Places.as_view()),
]