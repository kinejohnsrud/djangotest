from django.conf.urls import url
#from django.contrib import admin
from . import views

#add app_name to set application namespace
app_name = 'polls'

urlpatterns = [
	# /polls/
	url(r'^$', views.index, name='index'),
	# /polls/5
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	# /polls/5/results
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	# /polls/5/results/vote
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]