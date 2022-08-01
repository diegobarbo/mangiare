from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Item(models.Model):

    def __str__(self):
        return self.nome

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    preco = models.IntegerField()
    image = models.CharField(max_length=500, default="https://nolabelatthetable.com/wp-content/uploads/2018/01/IMAGE-COMING-SOON-300x300.png")


    def get_absolute_url(self):
        return reverse("dish:detail", kwargs={"pk": self.pk})
    