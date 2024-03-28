from django.urls import path, include
from rest_framework import routers

from musician import views

route = routers.DefaultRouter()
route.register("manage", views.MusicViewSet)
urlpatterns = [
    path("", include(route.urls))
]

app_name = "musician"
