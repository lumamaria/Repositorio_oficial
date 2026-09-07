from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Tag(models.Model):
    titulo = models.CharField(max_length=150)

    def __str__(self):
        return self.titulo


class Noticia(models.Model):
    titulo = models.CharField(max_length=300)
    texto = models.TextField()

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='noticias'
    )

    tags = models.ManyToManyField(
        Tag,
        related_name='noticias'
    )

    def __str__(self):
        return self.titulo


class Perfil(models.Model):
    bio = models.TextField()

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.usuario.username
    