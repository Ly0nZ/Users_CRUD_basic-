from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^logout$', views.logout),
	url(r'^users$', views.index),
	url(r'^users/new$', views.new),
	url(r'^create$', views.create),
	url(r'^index$', views.index),
	url(r'^delete/(?P<user_id>\d+)$', views.del_user),
	url(r'^users/(?P<user_id>\d+)$', views.show),
	url(r'^edit/(?P<user_id>\d+)$', views.edit),
	url(r'^editChange/(?P<user_id>\d+)$', views.editChange),
]
