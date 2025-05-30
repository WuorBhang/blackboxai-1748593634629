from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, VolunteerViewSet, DonationViewSet, ContactViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'volunteers', VolunteerViewSet)
router.register(r'donations', DonationViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
