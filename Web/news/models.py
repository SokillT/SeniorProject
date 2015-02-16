from django.db import models

# Create your models here.

class News(models.Model):
	Nid = models.AutoField(primary_key=True)
	Topic = models.CharField(max_length=100)
	Link = models.CharField(max_length=100)
	Cid = models.IntegerField(default=0)

class Category(models.Model):
	Cid = models.IntegerField(primary_key=True)
	Type = models.CharField(max_length=50)
		
