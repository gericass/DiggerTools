from django.conf.urls import url
from keijiban import views
from keijiban import twitter


urlpatterns = [
   url(r'^idinput/$', views.kakikomi),
   url(r'^idinput/results/$',views.results),
   url(r'^idinput/ineeyo/$',views.inee),
]

