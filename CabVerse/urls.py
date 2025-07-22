from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RiderViewSet, DriverViewSet, RideViewSet,
    CancelRideView, AcceptRideView, RejectRideView, UpdateRideStatusView,
    RiderRatingViewSet, DriverRatingViewSet
)

router = DefaultRouter()
router.register('riders', RiderViewSet)
router.register('drivers', DriverViewSet)
router.register('rides', RideViewSet, basename='ride')
router.register('rider-ratings', RiderRatingViewSet)
router.register('driver-ratings', DriverRatingViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('rides/<int:pk>/cancel/', CancelRideView.as_view(), name='cancel_ride'),
    path('rides/<int:pk>/accept/', AcceptRideView.as_view(), name='accept_ride'),
    path('rides/<int:pk>/reject/', RejectRideView.as_view(), name='reject_ride'),
    path('rides/<int:pk>/update_status/', UpdateRideStatusView.as_view(), name='update_status'),
    path('rides/user/<str:username>/', RideViewSet.as_view({'get': 'list'}), name='user_rides'),
]

