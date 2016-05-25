from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question, Choice 
from django.core.urlresolvers import reverse
from django.views import generic

#display the 5 latest polls questions on the index page, separated by commas, according to publication date
#loads the template called polls/index.html and passes it a context
#the context is a dictionary mapping template variable names to Python objects
#def index(request):
	#latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#context = {'latest_question_list': latest_question_list,}

	#return render(request, 'polls/index.html', context)		#removes need for HttpResponse and loader

#Raising a 404-error if question does not exist
#Use the get_object_or_404 shortcut that Django provides
#def detail(request, question_id):
	#try:
	#	question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exist")
	#question = get_object_or_404(Question, pk=question_id)	#takes Django model as first argument, and arbitrary number of keyword arguments, which it passes to the get() function of the model's manager
	#return render(request, 'polls/detail.html', {'question': question})

#def results(request, question_id):
	#question = get_object_or_404(Question, pk=question_id)
	#return render(request, 'polls/results.html', {'question': question})
	#return HttpResponse("You're looking at the result of question %s." % question_id)

# --------------------------- Changing to use generic Django views ----------------------- #

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'


def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	#request.POST raises KeyError if choice data is not provided. If error: Redisplay question with error-message
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		#HttpResponseRedirect takes a single argument, which is the URL the user is to be redirected to
		#The reverse function will return a string like 'polls/3/results'
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) 

