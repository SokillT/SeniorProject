from django.db import models

# Create your models here.
class Category(models.Model):
	Cid = models.IntegerField(primary_key=True)
	CatType = models.CharField(max_length=50)

class UserGroup(models.Model):
	Nid = models.AutoField(primary_key=True)
	Topic = models.CharField(max_length=255)
	Content = models.TextField(blank=True, null=True)
	Link = models.CharField(max_length=255)
	Source = models.CharField(max_length=50, null=True)
	DatePublish = models.DateField(null=True)
	DateStart = models.DateField(null=True)
	Cid = models.ForeignKey(Category)

class News(models.Model):
	Nid = models.AutoField(primary_key=True)
	Topic = models.CharField(max_length=255)
	Content = models.TextField(blank=True, null=True)
	Link = models.CharField(max_length=255)
	Source = models.CharField(max_length=50, null=True)
	DatePublish = models.DateField(null=True)
	DateStart = models.DateField(null=True)
	Cid = models.ForeignKey(Category)

class Subcate(models.Model):
	Sid = models.IntegerField(primary_key=True)
	SubType = models.CharField(max_length=100)
	Cid = models.ForeignKey(Category)

class News2Sub(models.Model):
	Nid = models.ForeignKey(News)
	Sid = models.ForeignKey(Subcate)