"""
views.py
Tento soubor obsahuje view funkce nebo třídy, které obsluhují požadavky uživatelů.
Zpracovávají data, která jsou získána z modelů nebo jiných zdrojů, a vrací odpověď
uživateli (např. HTML stránku nebo JSON).
"""

from rest_framework import viewsets
from .models import TodoItemEntity, Category
from .serializers import TodoItemSerializer, CategorySerializer

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItemEntity.objects.all()
    serializer_class = TodoItemSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
