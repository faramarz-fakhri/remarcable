from django import forms
from .models import Category, Tag

class ItemFilterForm(forms.Form):
    q = forms.CharField(required=False, label='Search', widget=forms.TextInput(attrs={'placeholder': 'Search description...'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, empty_label="All categories")
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
