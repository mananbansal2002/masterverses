from rest_framework import serializers
from api.models import SpiritualEvent

class SpiritualEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpiritualEvent
        fields = "__all__"