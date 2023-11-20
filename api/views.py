import logging
from http import HTTPStatus

from rest_framework import generics
from rest_framework.response import Response

from api.serializers import CreateDocumentSerializer
from api.services import create_file

logger = logging.getLogger(__name__)


class CreateDocumentView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        """

        CreateDocumentView

        This view is responsible for creating a document. It receives a `POST` request with `request.data`
        containing the document data. It validates the data using the `CreateDocumentSerializer` and creates a file
        using the `create_file` service.

        :param request: The `POST` request object containing the document data.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.

        :return: If the serializer is valid and the file is created successfully, it returns a `Response` object
        with the file ID and `HTTPStatus.CREATED` status code. If there is an error in the serializer or
        the file is not created, it returns a `Response` object with an error message
        and `HTTPStatus.BAD_REQUEST` status code.

        """
        serializer = CreateDocumentSerializer(data=request.data)
        if serializer.is_valid():
            file_id = create_file(request)
            if file_id:
                logger.info("File %s created" % file_id)
                return Response({"id": file_id}, status=HTTPStatus.CREATED)
        logger.error("Serializer error %s" % serializer.errors or "File not created")
        return Response({"error": "File not created"}, status=HTTPStatus.BAD_REQUEST)
