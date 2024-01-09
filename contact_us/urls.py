from rest_framework.routers import DefaultRouter
from .views import ContactUsViewSets
from django.urls import path,include

router=DefaultRouter()
router.register('contact_us',ContactUsViewSets)

urlpatterns = [
    path('', include(router.urls)),
]