from django.db import models
from datetime import datetime

# Create your models here.

class Question(models.Model):
	Question = models.TextField()
	#Option = models.ForeignKey(Option)
	#Hint = models.ForeignKey(Hint)
	#Solution = models.ForeignKey(Solution)
	date = models.DateTimeField()


	def __unicode__(self):
		return self.Question

		
class Option(models.Model):
	Question = models.ForeignKey(Question)
	Option = models.TextField()

	def assign(self):
		Alpha = 'ABCDEFGHIJKLMNOPQRSTWXYZ'
		for x in Alpha:
		    Option_Number = Alpha[0]
		    Alpha[0] = models.TextField()
	        #Option_Number = models.TextField(default = 'ABCDEFGHIJKLMNOPQRSTWXYZ')

class Hint(models.Model):
	Question = models.ForeignKey(Question)
	Hint = models.TextField()
	link = "Edit"

class Solution(models.Model):
	Question = models.ForeignKey(Question)
	Solution = models.TextField()
