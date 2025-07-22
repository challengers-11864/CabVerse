from rest_framework import serializers
from .models import Rider, Driver, Ride, RiderRating, DriverRating

class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class RideSerializer(serializers.ModelSerializer):
    rider = serializers.SlugRelatedField(
        queryset=Rider.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Ride
        fields = '__all__'


class RiderRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiderRating
        fields = '__all__'

class DriverRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverRating
        fields = '__all__'

# ### CabVerse/views.py
# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from .models import Rider, Driver, Ride, RiderRating, DriverRating
# from .serializers import RiderSerializer, DriverSerializer, RideSerializer, RiderRatingSerializer, DriverRatingSerializer
# from rest_framework.views import APIView
# from django.shortcuts import get_object_or_404
# from rest_framework.generics import CreateAPIView

# class RiderViewSet(viewsets.ModelViewSet):
#     queryset = Rider.objects.all()
#     serializer_class = RiderSerializer

# class DriverViewSet(viewsets.ModelViewSet):
#     queryset = Driver.objects.all()
#     serializer_class = DriverSerializer

# class RideViewSet(viewsets.ModelViewSet):
#     queryset = Ride.objects.all()
#     serializer_class = RideSerializer

# class CancelRideView(APIView):
#     def post(self, request, pk):
#         ride = get_object_or_404(Ride, pk=pk)
#         ride.status = 'cancelled'
#         ride.save()
#         return Response({'status': 'ride cancelled'})

# class AcceptRideView(APIView):
#     def post(self, request, pk):
#         ride = get_object_or_404(Ride, pk=pk)
#         ride.status = 'accepted'
#         ride.save()
#         return Response({'status': 'ride accepted'})

# class RejectRideView(APIView):
#     def post(self, request, pk):
#         ride = get_object_or_404(Ride, pk=pk)
#         ride.status = 'rejected'
#         ride.save()
#         return Response({'status': 'ride rejected'})

# class UpdateRideStatusView(APIView):
#     def patch(self, request, pk):
#         ride = get_object_or_404(Ride, pk=pk)
#         ride.status = request.data.get('status')
#         ride.save()
#         return Response({'status': f'updated to {ride.status}'})

# class RiderRatingViewSet(viewsets.ModelViewSet):
#     queryset = RiderRating.objects.all()
#     serializer_class = RiderRatingSerializer

# class DriverRatingViewSet(viewsets.ModelViewSet):
#     queryset = DriverRating.objects.all()
#     serializer_class = DriverRatingSerializer
