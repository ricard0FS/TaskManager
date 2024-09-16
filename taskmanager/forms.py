from django import forms 

class cliente(forms.form):
    nome = forms.CharField(max_length=100)
    idade = forms.IntegerField()
    