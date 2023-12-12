from django.contrib import admin

from .models import Paciente, Especialidad, Doctor, Direccion

admin.site.register(Paciente)
admin.site.register(Especialidad)
admin.site.register(Doctor)
admin.site.register(Direccion)


# Register your models here.
