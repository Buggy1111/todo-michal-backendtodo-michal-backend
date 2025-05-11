
from rest_framework import serializers
from .models import TodoItemEntity, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TodoItemSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True,
        required=False  # Volitelné při zadávání
    )
    created_at = serializers.DateTimeField(read_only=True)  # Zabrání požadavku na created_at při POST

    class Meta:
        model = TodoItemEntity
        fields = ['id', 'name', 'completed', 'category_id', 'created_at']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category).data if instance.category else None
        return rep
