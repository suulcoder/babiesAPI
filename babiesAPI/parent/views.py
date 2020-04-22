from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from parent.models import Parent
from baby.models import Baby
from parent.serializer import ParentSerializer
from baby.serializer import BabySerializer

class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    @action(detail=True, methods=['get'])
    def babies(self, request, pk=None):
        parent = self.get_object()
        response = []
        for baby in Baby.objects.filter(parent=parent):
            response.append(BabySerializer(baby).data)
        return Response(response)