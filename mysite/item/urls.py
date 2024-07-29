from django.urls import path, include
from .views import detail, new

app_name = "item"

urlpatterns = [
    path("new/", new, name="new"),
    path("<int:pk>/", detail, name="detail"),
]
