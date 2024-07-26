from django.urls import path, include
from .views import detail

app_name = "item"

urlpatterns = [
    path("<int:pk>/", detail, name="detail"),
]