#from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.views import Myview_Tech, Myview_Product

from blog.models import Post
from.import views

urlpatterns = patterns('',
	                   url(r'^$', ListView.as_view(
	                   queryset=Post.objects.all().order_by("-date")[:10],
	                   template_name="blog_blog.html")),

	                   url(r'^(?P<pk>\d+)$', DetailView.as_view(
	                   model = Post,
	                   template_name="post.html")),

	                   #url(r'^category/Tech/$', views.get_posts, name = 'Category'),

	                   url(r'^category/Tech/$', Myview_Tech.as_view()),
	                   #queryset=Post.objects.all(),
	                   #template_name="Tech.html")),

	                   url(r'^category/Product/$', Myview_Product.as_view()),
	                   #queryset=Post.objects.all().order_by("-date")[:5],
	                   #template_name="Product.html")),
	                  )

# Create your views here.
