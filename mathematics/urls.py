from django.conf.urls import patterns, include, url
from django.contrib.flatpages import views
from django.views.generic import ListView, DetailView
from mathematics.models import Question
from.import views
from django.contrib.flatpages.models import FlatPage

#from django.contrib.flatpages import views

urlpatterns = patterns('',
	                   url(r'^$', ListView.as_view(
	                   queryset=Question.objects.all().order_by("-date")[:10],
	                   template_name="blog.html")),

	                   url(r'^(?P<question_id>\d+)$', views.detail, name = 'detail'),
	                   #template_name="detail.html")),
                       url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
                       url(r'^(?P<question_id>[0-9]+)/submit/$', views.submit, name='submit'),
                       url(r'^search-form/$', views.search_form),
                       url(r'^about/$', views.detail1, name = 'detail1'),
                       url(r'^search/$', views.search),
                       url(r'^about-us/$', 'django.contrib.flatpages.views.flatpage', {'url': '/about/'}, name='detail1'),
                       #url(r'^license/$', views.flatpage, {'url': '/license/'}, name='license'),

	                )

# Create your views here.
