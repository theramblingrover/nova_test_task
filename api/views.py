import os.path
import logging

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from rest_framework import generics
from django.conf import settings

logger = logging.getLogger(__name__)


class CreateDocumentView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        ...


def create_file():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(settings.TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(settings.TOKEN_FILE, settings.SCOPES)
        logger.info("Token found")
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            logger.info("Refreshing token")
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                settings.CREDS_FILE, settings.SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(settings.TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    try:
        service = build("drive", "v3", credentials=creds)

        # Call the Drive v3 API
        results = (
            service.files()
            .list(pageSize=10, fields="nextPageToken, files(id, name)")
            .execute()
        )
        items = results.get("files", [])

        if not items:
            print("No files found.")
            return
        print("Files:")
        for item in items:
            print(f"{item['name']} ({item['id']})")
    except HttpError as e:
        # TODO(developer) - Handle errors from drive API.
        logger.error("Error %s occurred accessing Google API" % e)
