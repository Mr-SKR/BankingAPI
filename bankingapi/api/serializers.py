from rest_framework import serializers
from .models import Banks, Branches


class BanksSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Banks
        fields = ('id', 'name')


class BranchSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Branches
        fields = ('ifsc', 'bank', 'branch', 'address', 'city', 'district',
                  'state')
