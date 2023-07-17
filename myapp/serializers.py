"""
from rest_framework import serializers

class ForexDataSerializer(serializers.Serializer):
    from_symbol = serializers.CharField()
    to_symbol = serializers.CharField()
    interval = serializers.CharField()
    resolution = serializers.CharField(default="1day")
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)
    source = serializers.CharField(default="YahooFinance")
    verbose = serializers.BooleanField(default=False)
    #data = serializers.DictField(child=serializers.FloatField())
"""
from rest_framework import serializers

class ForexDataSerializer(serializers.Serializer):
    from_symbol = serializers.CharField()
    to_symbol = serializers.CharField()
    interval = serializers.CharField()
    resolution = serializers.CharField(default="1 day")
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)
    source = serializers.CharField(default="YahooFinance")
    verbose = serializers.BooleanField(default=False)

