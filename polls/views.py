from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.http import Http404
# from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404
from .models import *
from django.views import generic
from django.utils import timezone


# Create your views here.


# http://python.usyiyi.cn/translate/django_182/intro/tutorial04.html

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        # Question.objects.filter(pub_date__lte=timezone.now()) 返回一个查询集，包含pub_date小于等于timezone.now的Question。


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
        # Question.objects.filter(pub_date__lte=timezone.now())
        # 返回一个查询集，包含pub_date小于等于timezone.now的Question。


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
        print(selected_choice, type(selected_choice))
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
        # return HttpResponse("You're voting on question %s." % question_id)


'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {'latest_question_list': latest_question_list})
    # output = ', '.join([p.question_text for p in latest_question_list])
    context = {'latest_question_list': latest_question_list}

    return render(request, 'polls/index.html', locals())
    # return HttpResponse(template.render(context))
    # return HttpResponse(output)
    # return HttpResponse("Hello, world. You're at the polls index.")


def detail1(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')

    question = get_object_or_404(Question, pk=question_id)

    # return HttpResponse("You're looking at question %s." % question_id)
    return render(request, 'polls/detail.html', {'question': question})

#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id
    return render(request, 'polls/results.html', {"question": question})

'''
