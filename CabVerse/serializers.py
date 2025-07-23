from rest_framework import serializers
from .models import Rider, Driver, Ride, RiderRating, DriverRating
# from django.contrib.auth.hashers import check_password
# from rest_framework.authtoken.models import Token


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        # Try to find user in Rider
        rider = Rider.objects.filter(email=email, password=password).first()
        if rider:
            return {"user_type": "rider", "user": rider}

        # Try to find user in Driver
        driver = Driver.objects.filter(email=email, password=password).first()
        if driver:
            return {"user_type": "driver", "user": driver}

        raise serializers.ValidationError("Invalid email or password")

    def create(self, validated_data):
        return validated_data

    def to_representation(self, instance):
        return {
            "message": "Login successful",
            "user_type": instance["user_type"],
            "user_id": instance["user"].id,
            "redirect": "/rides/"
        }


        
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
