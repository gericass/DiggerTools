from django.conf.urls import url
from keijiban import views
from keijiban import twitter


urlpatterns = [
   url(r'^$', views.kakikomi),
   url(r'^/results/$',views.results),
   url(r'^/ineeyo/$',views.inee),
]

