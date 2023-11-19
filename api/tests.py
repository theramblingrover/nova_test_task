import pytest
from unittest.mock import Mock, patch
from http import HTTPStatus

from rest_framework.test import APIRequestFactory
import django

from .views import CreateDocumentView

django.setup()


@pytest.mark.django_db
@patch("api.views.create_file")
def test_create_document_file_not_created(mock_create_file):
    mock_create_file.return_value = None
    factory = APIRequestFactory()
    request = factory.post("/")

    view = CreateDocumentView.as_view()

    response = view(request)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data == {"error": "File not created"}


@pytest.mark.django_db
@patch("api.views.create_file")
def test_create_document_file_created(mock_create_file):
    mock_create_file.return_value = "12345"
    factory = APIRequestFactory()
    request = factory.post("/")

    view = CreateDocumentView.as_view()

    response = view(request)

    assert response.status_code == HTTPStatus.CREATED
    assert response.data == {"id": "12345"}
