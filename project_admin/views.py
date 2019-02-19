from django.shortcuts import render
from .models import Price

# Create your views here.
def index(request):
	price_list = Price.objects.all()[:10]
	return render(request, 'project_admin/index.html', {'price_list':price_list})
