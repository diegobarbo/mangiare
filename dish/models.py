from django.db import models


class Item(models.Model):

    def __str__(self):
        return self.nome

    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    preco = models.IntegerField()
    image = models.CharField(max_length=500, default="https://nolabelatthetable.com/wp-content/uploads/2018/01/IMAGE-COMING-SOON-300x300.png")
