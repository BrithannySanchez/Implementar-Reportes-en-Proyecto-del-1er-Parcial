from django.db import models

class Especialidad(models.Model):
    nombre = models.CharField(max_length=30, null=True)
    # Renombramos el campo "doctor" en "Especialidad" a algo diferente, por ejemplo, "nombre_doctor"
    nombre_doctor = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre if self.nombre else "Especialidad sin nombre"

class Doctor(models.Model):
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre if self.nombre else "Doctor sin nombre"

class Direccion(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    sucursal = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    SEXO = [
        ("M", "Masculino"),
        ("F", "Femenino"),
    ]

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1, choices=SEXO, null=True)
    email = models.CharField(max_length=50)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id} - {self.apellido} {self.nombre}"

