from django import forms
from .models import Inventory

class InventoryCreateForm(forms.ModelForm):
   class Meta:
     model = Inventory
     fields = ['genre', 'bookname', 'quantity']

   def clean_genre(self):
         genre = self.cleaned_data.get('genre')
         if not genre:
             raise forms.ValidationError('This field is required')
         for instance in Inventory.objects.all():
             if instance.genre == genre:
                 raise forms.ValidationError(str(genre) + ' is already created')
         return genre


   def clean_bookname(self):
         bookname = self.cleaned_data.get('bookname')
         if not bookname:
             raise forms.ValidationError('This field is required')
         return bookname

class InventorySearchForm(forms.ModelForm):
   class Meta:
     model = Inventory
     fields = ['genre', 'bookname']

class InventoryUpdateForm(forms.ModelForm):
	class Meta:
		model = Inventory
		fields = ['genre', 'bookname', 'quantity']