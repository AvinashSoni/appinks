from django.db import models

# Create your models here.





class Question(models.Model):
	Question = models.TextField()
	#Option = models.ForeignKey(Option)
	#Hint = models.ForeignKey(Hint)
	#Solution = models.ForeignKey(Solution)


	def __unicode__(self):
		return self.Question
class Option(models.Model):
	Question = models.ForeignKey(Question)
	Option = models.TextField()

class Hint(models.Model):
	Question = models.ForeignKey(Question)
	Hint = models.TextField()

class Solution(models.Model):
	Question = models.ForeignKey(Question)
	Solution = models.TextField()
