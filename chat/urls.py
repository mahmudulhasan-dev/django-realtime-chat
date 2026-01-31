from django.urls import path
from .views import RoomListCreateView, MessageListCreateView

urlpatterns = [
    path("rooms/", RoomListCreateView.as_view(), name="room-list-create"),
    path(
        "rooms/<uuid:room_id>/messages/",
        MessageListCreateView.as_view(),
        name="message-list-create",
    ),
]
