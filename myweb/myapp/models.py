from django.db import models
import pymysql

# Create your models here.
class Test(models.Model):
	name = models.CharField(max_length=20)

class Question(models.Model):
	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published')

class Choice(models.Model):
	question=models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)