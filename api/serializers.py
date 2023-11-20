from rest_framework import serializers


class CreateDocumentSerializer(serializers.Serializer):
    """Serializer for creating documents.

    This serializer is used to validate and deserialize data when creating documents.

    Attributes:
        name (serializers.CharField): The name of the document.
        data (serializers.CharField): The data content of the document.

    """

    name = serializers.CharField(required=True, allow_blank=False)
    data = serializers.CharField(required=True, allow_blank=True)
