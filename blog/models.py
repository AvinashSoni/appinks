from django.db import models

class Category(models.Model):
	category = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.category

	def get_posts(self):
	    return Post.objects.filter(category=Tech)
# Create your models here.
class Post(models.Model):
	category = models.ForeignKey(Category)
	author = models.CharField(max_length = 100)
	title = models.CharField(max_length = 140)
	body = models.TextField()
	date = models.DateTimeField()

	def __unicode__(self):
		return self.title