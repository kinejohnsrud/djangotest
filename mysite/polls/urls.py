from django.conf.urls import url
#from django.contrib import admin
from . import views

#add app_name to set application namespace
app_name = 'polls'

urlpatterns = [
	# /polls/
	#change views from views.detail to views.DetailView.as_view() in order to use generic django views
	#question_id --> pk
	#url(r'^$', views.index, name='index'),
	url(r'^$', views.IndexView.as_view(), name='index'),
	# /polls/5
	#url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	# /polls/5/results
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	# /polls/5/results/vote
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]