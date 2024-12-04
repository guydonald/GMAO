from django import forms 
from django.forms import modelformset_factory
from .models import PieceUtilisee, Intervention


class InterventionForm(forms.ModelForm):
    class Meta:
        model = Intervention
        fields = ['actions', 'observation', 'classe_action']
        widgets = {
            'actions': forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
            'observation': forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
            'classe_action': forms.Select(attrs={'class':'form-control'}),
        }

class PieceUtiliseeForm(forms.ModelForm):
    nombre_utilisee = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(0, 10)],
        label='Nombre de pièces utilisées',
        widget=forms.Select(attrs={'class':'form-select'})
    )
    class Meta:
        model = PieceUtilisee
        fields = ['nom', 'nombre_utilisee', 'etat']
        widgets = {
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_utilisee': forms.Select(attrs={'class':'form-select'}),
            'etat': forms.Select(attrs={'class':'form-select'}),
        }

PieceUtiliseeFormSet = modelformset_factory(PieceUtilisee, form=PieceUtiliseeForm, extra=1)