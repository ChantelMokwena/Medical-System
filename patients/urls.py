from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PatientViewSet, MedicalConditionViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'medical-conditions', MedicalConditionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]