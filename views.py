from django.shortcuts import render, redirect
from .models import *
from .forms import InventoryCreateForm, InventorySearchForm,InventoryUpdateForm
# Create your views here.
def home(request):
	title = 'Welcome: This is the Home Page'
	form ='Welcome: This is the Home page'
	context = {
	"title": title,
	"form":form,
	}
	return render(request, "home.html",context)
def list_items(request):
	header = 'List of list_items'
	form = InventorySearchForm(request.POST or None)
	queryset = Inventory.objects.all()
	context = {
	"header": header,
	"queryset":queryset,
    "form": form
	}
	if request.method == 'POST':
		queryset = Inventory.objects.filter(genre__icontains=form['genre'].value(),
										    bookname__icontains=form['bookname'].value()
										)
		context = {
		"form": form,
		"header": header,
		"queryset": queryset,
	}
	return render(request, "list_items.html",context)

def add_items(request):
	form = InventoryCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/list_items')
	context = {
		"form": form,
		"title": "Add Item",
	}
	return render(request, "add_items.html", context)


def update_items(request, pk):
	queryset = Inventory.objects.get(id=pk)
	form = InventoryUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = InventoryUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/list_items')

	context = {
		'form':form
	}
	return render(request, 'add_items.html', context)