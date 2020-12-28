from django.contrib import admin
from . import models


@admin.register(models.FlowDefine)
class FlowDefineAdmin(admin.ModelAdmin):
    list_display = ['pk', 'sys_id', 'org_id', 'biz_id', 'wf_name', 'form_template', 'create_user', 'create_time', ]


@admin.register(models.FlowStepDefine)
class FlowStepDefineAdmin(admin.ModelAdmin):
    list_display = ['pk', 'sys_id', 'org_id', 'biz_id', 'step_no', 'flow_define', 'step_name', 'step_type', 'form_template', 'approve_percentage', 'pass_option', 'unpass_option', 'passed_status', ]


@admin.register(models.FlowNodeDefine)
class FlowNodeDefineAdmin(admin.ModelAdmin):
    list_display = ['pk', 'sys_id', 'org_id', 'biz_id', 'flow_step_id', 'node_name', 'node_type', 'sub_flow_id', ]
