from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^$', views.Users.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.Users.as_view()),
]