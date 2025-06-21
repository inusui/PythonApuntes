from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")  # es como un varchar en SQL
    content = models.TextField(verbose_name="Contenido")  # Permite logitud dinamica
    # Se crea automaticamente la fecha de creacion
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    # Se crea automaticamente la fecha de modificacion
    modified = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
