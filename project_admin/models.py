from django.db import models

# Create your models here.

class Client(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	#address = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Project(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	date_created = models.DateTimeField('date created', auto_now_add=True)
	#client = models.ForeignKey(Client)
	#vendor = models.ForeignKey(User,related_name='vendor')
	#administrator = models.ForeignKey(User,related_name='administrator')
	status = models.PositiveIntegerField()

	def __str__(self):
		return self.name

