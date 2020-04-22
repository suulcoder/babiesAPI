from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from baby.models import Baby
from baby.serializer import BabySerializer
from event.serializer import EventSerializer

def evaluate(user, obj, request):
    return user.first_name == obj.parent.name

class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='EventPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': 'baby.view_baby',
                    'destroy': evaluate,
                    'update': 'baby.change_baby',
                    'partial_update': 'baby.change_baby',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        baby = serializer.save()
        user = self.request.user
        assign_perm('baby.view_baby', user, baby)
        assign_perm('baby.change_baby', user, baby)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def events(self, request, pk=None):
        baby = self.get_object()
        return (Events.objects.filter(baby=baby).data)
