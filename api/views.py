import logging
from http import HTTPStatus

from rest_framework import generics
from rest_framework.response import Response

from api.serializers import CreateDocumentSerializer
from api.services import create_file

logger = logging.getLogger(__name__)


class CreateDocumentView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = CreateDocumentSerializer(data=request.data)
        if serializer.is_valid():
            file_id = create_file(request)
            if file_id:
                logger.info("File %s created" % file_id)
                return Response({"id": file_id}, status=HTTPStatus.CREATED)
        logger.error("Serializer error %s" % serializer.errors or "File not created")
        return Response({"error": "File not created"}, status=HTTPStatus.BAD_REQUEST)
