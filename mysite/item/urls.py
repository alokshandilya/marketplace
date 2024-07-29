from django.urls import path
from .views import detail, new, edit, delete

app_name = "item"

urlpatterns = [
    path("new/", new, name="new"),
    path("<int:pk>/", detail, name="detail"),
    path("<int:pk>/edit/", edit, name="edit"),
    path("<int:pk>/delete/", delete, name="delete"),
]
