from rest_framework.serializers import ModelSerializer
from . import models


class FlowDefineSerializer(ModelSerializer):

    class Meta:
        model = models.FlowDefine
        fields = (
            'pk',
            'sys_id',
            'org_id',
            'biz_id',
            'wf_name',
            'form_template',
            'create_user',
            'create_time',
        )


class FlowStepDefineSerializer(ModelSerializer):

    class Meta:
        model = models.FlowStepDefine
        fields = (
            'pk',
            'sys_id',
            'org_id',
            'biz_id',
            'step_no',
            'flow_define',
            'step_name',
            'step_type',
            'form_template',
            'approve_percentage',
            'pass_option',
            'unpass_option',
            'passed_status',
        )


class FlowNodeDefineSerializer(ModelSerializer):

    class Meta:
        model = models.FlowNodeDefine
        fields = (
            'pk',
            'sys_id',
            'org_id',
            'biz_id',
            'flow_step_id',
            'node_name',
            'node_type',
            'sub_flow_id',
        )
