from django.urls import path

from api.views import CreateDocumentView

app_name = "api"

urlpatterns = [path("touch/", CreateDocumentView.as_view())]
