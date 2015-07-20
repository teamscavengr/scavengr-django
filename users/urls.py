from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^$', views.Users.as_view()),
    url(r'^(?P<pk>[\w]+)/$', views.Users.as_view()),
]