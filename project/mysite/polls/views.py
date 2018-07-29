from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    
    # or shortcut render()
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'polls/index.html', context)
    # Here The render() function takes the request object as its first argument,
    # a template name as its second argument and a dictionary as its optional third argument.
    # It returns an HttpResponse object of the given template rendered with the given context

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does Not Exist")
    return render (request, 'polls/detail.html', {'question':question})
    
    # or a shortcut get_object_or_404() 
    # def detail (request, question_id)
    # question = get_object_or_404(Question, pk=question_id)
    # return render (request, 'polls/detail.html',{'question':question })
    # The get_object_or_404() function takes a Django model as its first argument 
    # and an arbitrary number of keyword arguments, which it passes to the 
    # get() function of the model’s manager. It raises Http404 if the object doesn’t exist.


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)