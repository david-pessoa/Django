from django.contrib import admin
from .models import *

#ou usar admin.site.register(Model)

# Register your models here.
@admin.register(Categoria)
class Categoria(admin.ModelAdmin):
    list_display = ("pk", "nome")

@admin.register(Cor)
class Cor(admin.ModelAdmin):
    list_display = ("pk", "nome")

@admin.register(Produto)
class Produto(admin.ModelAdmin):
    list_display = ("pk", "nome", "preco", "quantidade")
    