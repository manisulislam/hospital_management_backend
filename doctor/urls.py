from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path,include

router=DefaultRouter()
router.register('specialization',views.SpecializationViewSets)
router.register('designation',views.DesignationViewSets)
router.register('available_time',views.AvailableTimeViewSets)
router.register('doctor',views.DoctorViewSets)
router.register('review',views.ReviewViewSets)

urlpatterns = [
    path('', include(router.urls)),
]