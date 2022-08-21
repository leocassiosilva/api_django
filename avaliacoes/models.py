from django.contrib.auth.models import User
from django.db import models

class Avaliacao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(null=True, blank=True)
    nota = models.DecimalField(max_digits=15, decimal_places=3, default=0.0)
    data = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username