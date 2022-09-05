from rest_framework import serializers
from person.models import Person


class PersonSerializer(serializers.ModelSerializer):
    """Serialization of class model person"""
    class Meta:
        model = Person
        fields = [
            "id",
            "document_type",
            "document",
            "name",
            "last_name",
            "hobbie",
        ]
