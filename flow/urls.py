from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api


router = DefaultRouter()

router.register(r'flowdefine', api.FlowDefineViewSet)
router.register(r'flowstepdefine', api.FlowStepDefineViewSet)
router.register(r'flownodedefine', api.FlowNodeDefineViewSet)

urlpatterns = (
    path('api/v1/', include(router.urls)),
)
