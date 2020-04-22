from rest_framework import serializers

from baby.models import Baby

class BabySerializer(serializers.ModelSerializer):
    class Meta:
        model = Baby
        fields = (
            'id',
            'name',
            'lastname',
            'parent'
        )
