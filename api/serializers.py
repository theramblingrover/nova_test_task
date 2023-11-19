from rest_framework import serializers


class CreateDocumentSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_blank=False)
    data = serializers.CharField(required=True, allow_blank=True)
