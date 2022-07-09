"""
Serializers for Recipe API.
"""

from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for Recipe model."""

    class Meta:
        model = Recipe
        fields = (
            "id",
            "title",
            "time_minutes",
            "price",
            "link",
        )
        read_only_fields = ("id",)

    # def create(self, validated_data):
    #     """Create a new recipe."""
    #     return Recipe.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """Update an existing recipe."""
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.time_minutes = validated_data.get(
    #         "time_minutes", instance.time_minutes
    #     )
    #     instance.price = validated_data.get("price", instance.price)
    #     instance.description = validated_data.get("description", instance.description)
    #     instance.link = validated_data.get("link", instance.link)
    #     instance.save()
    #     return instance
