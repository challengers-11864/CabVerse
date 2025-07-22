from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Rider, Driver, Ride, RiderRating, DriverRating
from .serializers import RiderSerializer, DriverSerializer, RideSerializer, RiderRatingSerializer, DriverRatingSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView

class RiderViewSet(viewsets.ModelViewSet):
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

    def perform_create(self, serializer):
        total_passenger = serializer.validated_data.get('total_passenger')
        if total_passenger is None:
            raise ValidationError("Missing total_passenger for driver assignment.")

        available_driver = Driver.objects.filter(
            car_capacity__gte=total_passenger
        ).first()

        if not available_driver:
            raise ValidationError("No available driver with enough capacity.")

        serializer.save(driver=available_driver)


# class RideViewSet(viewsets.ModelViewSet):
#     serializer_class = RideSerializer

#     def get_queryset(self):
#         username = self.kwargs.get('username')
#         if not username:
#             return Ride.objects.none()

#         rider = Rider.objects.filter(username=username).first()
#         if rider:
#             return Ride.objects.filter(rider=rider)

#         driver = Driver.objects.filter(username=username).first()
#         if driver:
#             return Ride.objects.filter(driver=driver)

#         return Ride.objects.all()


class CancelRideView(APIView):
    def post(self, request, pk):
        ride = get_object_or_404(Ride, pk=pk)
        ride.status = 'cancelled'
        ride.save()
        return Response({'status': 'ride cancelled'})

class AcceptRideView(APIView):
    def post(self, request, pk):
        ride = get_object_or_404(Ride, pk=pk)
        ride.status = 'accepted'
        ride.save()
        return Response({'status': 'ride accepted'})

class RejectRideView(APIView):
    def post(self, request, pk):
        ride = get_object_or_404(Ride, pk=pk)
        ride.status = 'rejected'
        ride.save()
        return Response({'status': 'ride rejected'})

class UpdateRideStatusView(APIView):
    def patch(self, request, pk):
        ride = get_object_or_404(Ride, pk=pk)
        ride.status = request.data.get('status')
        ride.save()
        return Response({'status': f'updated to {ride.status}'})

class RiderRatingViewSet(viewsets.ModelViewSet):
    queryset = RiderRating.objects.all()
    serializer_class = RiderRatingSerializer

class DriverRatingViewSet(viewsets.ModelViewSet):
    queryset = DriverRating.objects.all()
    serializer_class = DriverRatingSerializer