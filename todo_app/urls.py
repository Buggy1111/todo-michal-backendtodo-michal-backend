from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoItemViewSet, CategoryViewSet  # ← přidat CategoryViewSet

router = DefaultRouter()
router.register(r'todo', TodoItemViewSet)
router.register(r'categories', CategoryViewSet)  # ← zaregistrovat cestu /categories/

urlpatterns = [
    path('', include(router.urls)),
]

