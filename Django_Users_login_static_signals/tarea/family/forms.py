from django import forms

class familiaForm(forms.Form):
    equipo=forms.CharField(max_length=30)
    pais=forms.CharField(max_length=30)
    liga=forms.CharField(max_length=30)