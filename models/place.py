#!/usr/bin/python
"""heritage place from base"""
from models.base_class import BaseModel


class Place(BaseModel):
    """Place"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids{} = ""

    def __init__(self, *args, **kwargs):
        """initisation new Place"""
        super().__init__(*args, **kwargs)
