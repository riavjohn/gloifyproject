from django import forms
from .models import Inventory

class InventoryCreateForm(forms.ModelForm):
   class Meta:
     model = Inventory
     fields = ['genre', 'bookname', 'quantity']



class InventorySearchForm(forms.ModelForm):
   class Meta:
     model = Inventory
     fields = ['genre', 'bookname']

class InventoryUpdateForm(forms.ModelForm):
	class Meta:
		model = Inventory
		fields = ['genre', 'bookname', 'quantity']