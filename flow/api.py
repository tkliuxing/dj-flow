from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from . import serializers
from . import models


class FlowDefineViewSet(ModelViewSet):
    queryset = models.FlowDefine.objects.order_by('pk')
    serializer_class = serializers.FlowDefineSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('sys_id', 'org_id', 'biz_id', 'wf_name',)


class FlowStepDefineViewSet(ModelViewSet):
    queryset = models.FlowStepDefine.objects.order_by('pk')
    serializer_class = serializers.FlowStepDefineSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('sys_id', 'org_id', 'biz_id', 'step_name', 'step_type',)


class FlowNodeDefineViewSet(ModelViewSet):
    queryset = models.FlowNodeDefine.objects.order_by('pk')
    serializer_class = serializers.FlowNodeDefineSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('sys_id', 'org_id', 'biz_id', 'node_name', 'node_type',)
