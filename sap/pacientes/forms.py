from django.forms import ModelForm, EmailInput
from .models import Paciente

class PacienteFormulario(ModelForm):
    class Meta:
        model = Paciente
        fields = ('nombre', 'apellido', 'sexo', 'email', 'activo', 'especialidad')
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }  # Agregar cierre de llave al final del diccionario widgets
    # Agregar el cierre de llave para la clase Meta y la clase del formulario PacienteFormulario


