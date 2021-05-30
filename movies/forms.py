"""module that deals with forms"""

from django import forms


class ProductSearch(forms.Form):
    """class for the searching form"""
    search = forms.CharField(label="", max_length=100,
                             widget=forms.TextInput(attrs={'placeholder':
                                                    "Entrez votre recherche"}))
