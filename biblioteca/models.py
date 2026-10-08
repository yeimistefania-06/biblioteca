from django.db import models

class autor(models.Model):
    nombre = models.CharField(max_length=500)
    lugar_nacimiento = models.CharField(max_length=100)
    fecha_nacimiento = models.DateTimeField()

    def __str__(self):
        return self.nombre

class libro(models.Model):
    titulo = models.CharField()
    descripcion = models.TextField()
    autor_id = models.ForeignKey(autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo