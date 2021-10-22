from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse

from polls.models import Choice, Question

# Create your views here.
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        choice = Choice.objects.all()
    except Question.DoesNotExist:
        raise Http404("NOT FOUND")
    return render(request, 'polls/detail.html', {'question': question, 'choice': choice})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def index(request):
    last_question_list = Question.objects.order_by('pub_date')[:5]
    context = {
        'lastest_question_list': last_question_list,
    }
    return render(request, 'polls/index.html', context)