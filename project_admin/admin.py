from django.contrib import admin
from .models import Client, Project, Item, Supplier, Contact, Price, Kit

# Register your models here.
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Item)
admin.site.register(Supplier)
admin.site.register(Contact)
admin.site.register(Price)
admin.site.register(Kit)