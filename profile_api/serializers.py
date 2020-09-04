from rest_framework  import serializers

class HelloSerializer(serializers.Serializer):
    """serializer a name feild for testing our apiview"""
    name =serializers.CharField(max_length=10)
    