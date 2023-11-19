import logging
from http import HTTPStatus

from rest_framework import generics
from rest_framework.response import Response

from api.services import create_file

logger = logging.getLogger(__name__)


class CreateDocumentView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        file_id = create_file(request)
        if not file_id:
            logger.error("File not created")
            return Response(
                {"error": "File not created"}, status=HTTPStatus.BAD_REQUEST
            )
        logger.info("File %s created" % file_id)
        return Response({"id": file_id}, status=HTTPStatus.CREATED)
