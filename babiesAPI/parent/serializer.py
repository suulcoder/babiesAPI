from rest_framework import serializers

from parent.models import Parent


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = (
            'id',
            'first_name'
        )
