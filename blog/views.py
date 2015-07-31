from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView

class Myview_Tech(ListView):
	context_object_name ='post_list'
	queryset = Post.objects.filter(category__category = 'Tech')
	template_name = 'Tech.html'
	#context_object_name = 'post_list'
    #queryset = Post.objects.filter(category__category='Product')
    #template_name ='Tech.html'
# Create your views here.
class Myview_Product(ListView):
	context_object_name ='post_list'
	queryset = Post.objects.filter(category__category = 'Product')
	template_name = 'Tech.html'