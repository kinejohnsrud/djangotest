from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader
from .models import Question #added import to access the Questions from the database/model

#display the 5 latest polls questions on the index page, separated by commas, according to publication date
#loads the template called polls/index.html and passes it a context
#the context is a dictionary mapping template variable names to Python objects
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('polls/index.html')
	context = {'latest_question_list': latest_question_list,}
	#output = ', '.join([q.question_text for q in latest_question_list])
	#return HttpResponse(output)
	#return HttpResponse(template.render(context, request))
	return render(request, 'polls/index.html', context)		#removes need for HttpResponse and loader

def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	return HttpResponse("You're looking at the result of question %s." % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)

