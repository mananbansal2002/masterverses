import math
import requests
from django.db import transaction
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from geopy.distance import geodesic

from api.models import SpiritualEvent
from api.serializers import SpiritualEventSerializer
from api.constants import OVERPASS_API_URL, DEFAULT_RADIUS_KM, FAITH_FILTER_MAP


class SpiritualEventsView(ListCreateAPIView):
    serializer_class = SpiritualEventSerializer

    def get_queryset(self):
        lat = self.request.query_params.get("lat")
        lng = self.request.query_params.get("lng")
        faith = self.request.query_params.get("faith")
        radius_km = float(self.request.query_params.get("radius", DEFAULT_RADIUS_KM))

        try:
            with transaction.atomic():
                queryset = SpiritualEvent.objects.all()

                if faith:
                    queryset = queryset.filter(faith__iexact=faith)

                if lat and lng:
                    lat, lng = float(lat), float(lng)
                    queryset = [
                        event for event in queryset
                        if geodesic((lat, lng), (event.latitude, event.longitude)).km <= radius_km
                    ]

                return queryset
        except Exception as e:
            print(f"Error fetching events: {e}")  
            return SpiritualEvent.objects.none()  

class NearbySpiritualPlacesView(APIView):
    def get(self, request):
        lat = request.query_params.get("lat")
        lng = request.query_params.get("lng")
        faith = request.query_params.get("faith", "").strip().lower()
        radius = request.query_params.get("radius", DEFAULT_RADIUS_KM)

        if not lat or not lng:
            return Response({"error": "Latitude and longitude are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            lat, lng, radius = float(lat), float(lng), float(radius)
        except ValueError:
            return Response({"error": "Invalid latitude, longitude, or radius."}, status=status.HTTP_400_BAD_REQUEST)

        # Convert radius from km to degrees
        km_to_deg = radius / 111
        lng_deg = radius / (111 * math.cos(math.radians(lat)))

        south, west = lat - km_to_deg, lng - lng_deg
        north, east = lat + km_to_deg, lng + lng_deg

        faith_filter = FAITH_FILTER_MAP.get(faith, "")

        overpass_query = f"""
        [out:json][timeout:20];
        (
          node["amenity"="place_of_worship"]{faith_filter}({south},{west},{north},{east});
          way["amenity"="place_of_worship"]{faith_filter}({south},{west},{north},{east});
          relation["amenity"="place_of_worship"]{faith_filter}({south},{west},{north},{east});
        );
        out center;
        """

        try:
            response = requests.get(OVERPASS_API_URL, params={"data": overpass_query}, timeout=20)
            response.raise_for_status()
            places = response.json().get("elements", [])
        except requests.RequestException as e:
            print(f"Error fetching spiritual places: {e}")  # Log for debugging
            return Response({"error": "Failed to fetch places"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        results = [
            {
                "name": place.get("tags", {}).get("name", "Unknown"),
                "latitude": place.get("lat", place.get("center", {}).get("lat")),
                "longitude": place.get("lon", place.get("center", {}).get("lon")),
                "address": place.get("tags", {}).get("addr:full", "Unknown"),
                "description": f"{faith.capitalize()} place of worship" if faith else "Place of worship",
                "image": None,
                "visiting_hours": place.get("tags", {}).get("opening_hours", "Varies by location"),
            }
            for place in places
        ]

        return Response(results, status=status.HTTP_200_OK)


def add_event(request):
    return render(request, "post_event.html")


def api_home(request):
    return render(request, "api_home.html")
