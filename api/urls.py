from django.urls import path
from api.views import add_event,api_home, SpiritualEventsView, NearbySpiritualPlacesView

urlpatterns = [
    path("", api_home, name="api-home"),
    path("add-event", add_event, name="add-event"),
    path("api/events/", SpiritualEventsView.as_view(), name="spiritual-events"),
    path("api/spiritual-places/", NearbySpiritualPlacesView.as_view(), name="spiritual-places"),
]
