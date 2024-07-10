from django import forms
from  .models import Departamento

class DepartamentoUpdate(forms.ModelForm):

    class Meta:
        model = Departamento
        fields = (
            'name',
            'short_name',
            'funcionando'
        )
        widgets = {
            'funcionando': forms.CheckboxInput()
        }
