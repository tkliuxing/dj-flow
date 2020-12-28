import uuid

from django.utils import timezone
from django.db import models


# 流程定义
class FlowDefine(models.Model):
    """流程定义"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sys_id = models.IntegerField('系统ID', default=1, db_index=True)
    org_id = models.IntegerField('组织ID', default=1, db_index=True)
    biz_id = models.IntegerField('业务ID', default=1, db_index=True)
    wf_name = models.CharField('流程名称', max_length=64, help_text='流程名称')
    form_template = models.ForeignKey(
        'formtemplate.FormTemplate', on_delete=models.CASCADE, related_name='flows', verbose_name='表单模版')
    create_user = models.ForeignKey(
        'usercenter.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='+', verbose_name='创建者')
    create_time = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = '流程定义'
        verbose_name_plural = verbose_name


# 流程步骤定义
class FlowStepDefine(models.Model):
    """流程步骤定义"""
    STEP_TYPE = (
        (1, '顺序'),
        (2, '分支'),
        (3, '选择'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sys_id = models.IntegerField('系统ID', default=1, db_index=True)
    org_id = models.IntegerField('组织ID', default=1, db_index=True)
    biz_id = models.IntegerField('业务ID', default=1, db_index=True)
    step_no = models.IntegerField('步骤序号')
    flow_define = models.ForeignKey(
        'FlowDefine', on_delete=models.CASCADE, related_name='flow_define', verbose_name='流程定义')
    step_name = models.CharField('步骤名称', max_length=64, help_text='步骤名称')
    step_type = models.IntegerField('步骤类型', choices=STEP_TYPE, default=1)
    form_template = models.ForeignKey('formtemplate.FormTemplate', on_delete=models.SET_NULL, null=True, blank=True,
                                      related_name='+', verbose_name='表单模版')
    approve_percentage = models.IntegerField('审批通过占比', default=100)
    pass_option = models.CharField('审批通过选项', max_length=64)
    unpass_option = models.CharField('审批不通过选项', max_length=64)
    passed_status = models.CharField('审批通过后状态', max_length=64)

    class Meta:
        verbose_name = '流程步骤定义'
        verbose_name_plural = verbose_name


# 流程节点定义
class FlowNodeDefine(models.Model):
    """流程节点定义"""
    NODE_TYPE = (
        (1, '行为节点'),
        (2, '动态节点'),
        (3, '子流程节点'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sys_id = models.IntegerField('系统ID', default=1, db_index=True)
    org_id = models.IntegerField('组织ID', default=1, db_index=True)
    biz_id = models.IntegerField('业务ID', default=1, db_index=True)
    flow_step_id = models.ForeignKey(
        'FlowStepDefine', on_delete=models.CASCADE, related_name='flow_step', verbose_name='流程步骤')
    node_name = models.CharField('节点名称', max_length=64, help_text='节点名称')
    node_type = models.IntegerField('节点类型', choices=NODE_TYPE, default=1, help_text='节点名称')
    sub_flow_id = models.UUIDField(editable=False, null=True, blank=True)

    class Meta:
        verbose_name = '流程节点定义'
        verbose_name_plural = verbose_name
