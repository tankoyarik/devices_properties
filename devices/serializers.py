from rest_framework import serializers

from devices.models import Device, Property


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"
