from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from .models import Question, Option
from django.views import generic
from django.contrib.flatpages.models import FlatPage

# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'question': question})

def submit(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_option = p.option_set.get(pk=request.POST['option'])
    except (KeyError, Option.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        #selected_option.options += 1
        answer = selected_option.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('mathematics:results', args=(p.id,)),{
            'question': p,
            'error_message': "You didn't select a choice."
        })

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,
        	'results.html', {'question': question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'results.html'

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        questions = Question.objects.filter(Question__icontains=q)
        return render(request, 'search_results.html',
            {'questions': questions, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')


def detail1(request):
    return render(request, 'flatpages/about.html')