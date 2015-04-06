from django.db import models

# Create your models here.

class News(models.Model):
	Nid = models.AutoField(primary_key=True)
	Topic = models.CharField(max_length=100)
	Content = models.TextField(blank=True, null=True)
	Link = models.CharField(max_length=100)
	DatePublish = models.DateField(null=True)

class Category(models.Model):
	Cid = models.IntegerField(primary_key=True)
	CatType = models.CharField(max_length=50)

class Subcate(models.Model):
	Sid = models.IntegerField(primary_key=True)
	SubType = models.CharField(max_length=50)
	Cid = models.ForeignKey(Category)

class News2Sub(models.Model):
	Nid = models.ForeignKey(News)
	Sid = models.ForeignKey(Subcate)
