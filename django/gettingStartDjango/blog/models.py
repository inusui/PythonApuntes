from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)  # es como un varchar en SQL
    content = models.TextField()  # Permite logitud dinamica
    # Se crea automaticamente la fecha de creacion
    created = models.DateTimeField(auto_now_add=True)
    # Se crea automaticamente la fecha de modificacion
    modified = models.DateTimeField(auto_now=True)
