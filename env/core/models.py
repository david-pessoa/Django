from django.db import models
from django.core.exceptions import ValidationError


class Categoria(models.Model):
    nome = models.CharField("Nome", max_length=45)

    def __str__(self):
        return self.nome
    
    def clean(self):
        if Categoria.objects.filter(nome=self.nome).exists():
            raise ValidationError(f"Uma categoria com o nome '{self.nome}' já existe.")

class Cor(models.Model):
    nome = models.CharField("Nome", max_length=45)

    def __str__(self):
        return self.nome
    
    def clean(self):
        # Verifica se já existe um objeto com o mesmo nome
        if Cor.objects.filter(nome=self.nome).exists():
            raise ValidationError(f"Um item com o nome '{self.nome}' já existe.")


class Produto(models.Model):
    nome = models.CharField("Nome", max_length= 45)
    preco = models.DecimalField("Preço", decimal_places=2, max_digits=6)
    descricao = models.CharField("Descição", max_length=45)
    cod_barras = models.CharField("Código", max_length=45)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    cor_id = models.ManyToManyField(Cor)
    quantidade = models.IntegerField(default=1)
    tamanho = models.CharField("Tamanho", max_length=45)

    def __str__(self):
        return self.nome