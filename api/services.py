import io
import logging
import os

from django.conf import settings
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseUpload

logger = logging.getLogger(__name__)


def create_file(request):
    creds = None
    if os.path.exists(settings.TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(
            settings.TOKEN_FILE, settings.SCOPES
        )
        logger.info("Token found")
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            logger.info("Refreshing token")
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                settings.CREDS_FILE, settings.SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open(settings.TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    data = request.data.get("data", "").encode()
    service = build("drive", "v3", credentials=creds)
    media_body = MediaIoBaseUpload(io.BytesIO(data), mimetype="text/plain")
    body = {
        "name": request.data.get("name"),
        "mimeType": "application/vnd.google-apps.document",
    }
    try:
        file = (
            service.files()
            .create(
                body=body,
                media_body=media_body,
                media_mime_type="text/plain",
                fields="id",
            )
            .execute()
        )
        file_id = file.get("id", None)
        return file_id
    except HttpError as e:
        logger.error("Error %s occurred accessing Google API" % e)
