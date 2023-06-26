from django.forms import ModelForm
from app.models import Colaboradores

# Create the form class.
class ColaboradoresForm(ModelForm):
    class Meta:
        model = Colaboradores
        fields = ['Nomes','Equipamento', 'Setor', 'Grupo']