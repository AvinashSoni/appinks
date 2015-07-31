from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from .views import Myview, Myview1, Myview2, Myview3, Myview4
from.models import MCQuestion

urlpatterns = patterns('',
                      #url(r'^(?P<pk>\d+)$'
                       url(r'^$', Myview.as_view()),
                       #url(r'^(?P<category>.+)/(?P<sub_category>.+)', Myview0.as_view()),
                      # url(r'^Mathematics/$', Myview1.as_view()),
                       #url(r'^Mathematics/(?P<sub_category_id>)$', Myview7.as_view()),
                       #url(r'^Mathematics/list/$', Myview3.as_view()),
                       #url(r'^Chemistry/$', Myview2.as_view()),
                       #url(r'^Chemistry/list/$', Myview4.as_view()),
                       #url(r'^Physics/$', Myview5.as_view()),
                       #url(r'^Physics/list/$', Myview6.as_view()),
                       #url(r'^Mathematics/(?P<sub_category>[\w-]+)/$', Myview7.as_view()),
                       url(r'^(?P<category>\w+)/$', Myview1.as_view()),
                       url(r'^Mathematics/(?P<sub_category>.+)', Myview2.as_view()),
                       url(r'^Physics/(?P<sub_category>.+)', Myview3.as_view()),
                       url(r'^Chemistry/(?P<sub_category>.+)', Myview4.as_view()),


                       #model = MCQuestion,
                       #template_name="quiz/mathematics_subcategory_detail.html"), {'foo': sub_category}),

                       #u
                       #rl(regex=r'^category/$',
                           #view=CategoriesListView.as_view(),
                          # name='quiz_category_list_all'),

                       #url(regex=r'^category/(?P<category_name>[\w.-]+)/$',
                          # view=ViewQuizListByCategory.as_view(),
                           #name='quiz_category_list_matching'),

                       #url(regex=r'^progress/$',
                           #view=QuizUserProgressView.as_view(),
                          # name='quiz_progress'),

                       #url(regex=r'^marking/$',
                           #view=QuizMarkingList.as_view(),
                           #name='quiz_marking'),

                      # url(regex=r'^marking/(?P<pk>[\d.]+)/$',
                          # view=QuizMarkingDetail.as_view(),
                           #name='quiz_marking_detail'),

                       #  passes variable 'quiz_name' to quiz_take view
                       #url(regex=r'^(?P<slug>[\w-]+)/$',
                          # view=QuizDetailView.as_view(),
                          # name='quiz_start_page'),

                      # url(regex=r'^(?P<quiz_name>[\w-]+)/take/$',
                          # view=QuizTake.as_view(),
                          # name='quiz_question'),
)
