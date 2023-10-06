from django import forms

class AsignaturaForm(forms.Form):
    nombre_asignatura = forms.CharField(label="Nombre Asignatura", max_length=30)
    codigo_asignatura = forms.IntegerField(label="Codigo Asignatura")