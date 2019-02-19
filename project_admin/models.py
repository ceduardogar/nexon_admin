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



class Contact(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	role = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Supplier(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	phone = models.PositiveIntegerField()
	email = models.EmailField()
	contact = models.ForeignKey(Contact, models.SET_NULL, blank=False, null=True)
	#items = models.ManyToManyField(Item, through='Cost')

	def __str__(self):
		return self.name

class Item(models.Model):
	id = models.AutoField(primary_key=True)
	part_number = models.CharField(max_length=50, unique=True)
	brand = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	category = models.PositiveIntegerField()
	#supplier = models.ForeignKey(Supplier, models.SET_NULL,null=True)
	#price = models.ForeignKey(Price,models.SET_NULL,null=True)

	def __str__(self):
		return self.part_number

class Price(models.Model):
	id = models.AutoField(primary_key=True)
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	date_created = models.DateTimeField('date created')


class Kit(models.Model):
	id = models.AutoField(primary_key=True)