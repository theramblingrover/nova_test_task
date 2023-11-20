import django
import pytest
from http import HTTPStatus
from unittest.mock import patch
from rest_framework.test import APIRequestFactory
from api.views import CreateDocumentView

django.setup()


@pytest.fixture(scope="module")
def factory():
    return APIRequestFactory()


@patch("api.views.create_file")
def test_create_document_view_successful(mock_create_file, factory):
    view = CreateDocumentView.as_view()
    mock_create_file.return_value = "123"
    data = {"data": "content", "name": "filename"}
    request = factory.post("/documents", data=data)
    response = view(request)
    assert response.status_code == HTTPStatus.CREATED
    assert response.data == {"id": "123"}


@patch("api.views.create_file")
def test_create_document_view_create_file_fail(mock_create_file, factory):
    view = CreateDocumentView.as_view()
    mock_create_file.return_value = None
    data = {"data": "content", "name": "filename"}
    request = factory.post("/documents", data=data)
    response = view(request)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data == {"error": "File not created"}


def test_create_document_view_invalid_data(factory):
    view = CreateDocumentView.as_view()
    data = {}  # providing invalid data
    request = factory.post("/documents", data=data)
    response = view(request)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert "error" in response.data
