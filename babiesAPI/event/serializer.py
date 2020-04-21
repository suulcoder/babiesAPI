from rest_framework import serializers

from event.models import Event


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = (
            'id',
            'eventType'
            'datetime'
            'info'
            'baby' 
        )
