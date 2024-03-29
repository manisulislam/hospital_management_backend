from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path,include

router=DefaultRouter()
router.register('list',views.PatientViewSets)

urlpatterns = [
    path('', include(router.urls)),
    path('register/',views.RegistrationApiView.as_view(),name='register'),
    path('active/<uid64>/<token>/',views.activate, name='activate')
]