from rest_framework import generics
from rest_framework.permissions import AllowAny

from devices.models import Device, Property
from devices.serializers import DeviceSerializer, PropertySerializer


class DevicesListCreate(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()


class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()


class PropertyListCreate(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PropertySerializer
    queryset = Property.objects.all()


class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
