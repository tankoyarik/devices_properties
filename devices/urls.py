from django.urls import path

from devices import views

urlpatterns = [
    path("devices/", views.DevicesListCreate.as_view()),
    path("devices/<int:pk>", views.DeviceDetail.as_view()),
    path("properties/", views.PropertyListCreate.as_view()),
    path("properties/<int:pk>", views.PropertyDetail.as_view()),
]
