from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .widgets import MapInput, AddressAutoHiddenInput


def reverse_tuple_string(location_string):
    if location_string == "":
        return location_string
    args = location_string.split(",")
    return args[1] + "," + args[0]


def parse_location(location_string, first_in_order="lng"):
    """parse and convert coordinates from string to tuple"""

    args = location_string.split(",")
    if len(args) != 2:
        raise ValidationError(_("Invalid input for a Location instance"))

    if first_in_order == "lat":
        lng = args[1]
        lat = args[0]
    elif first_in_order == 'lng':
        lng = args[0]
        lat = args[1]
    else:
        raise ValidationError(_("Invalid first letter for parsing location."))
    try:
        lat = float(lat)
    except ValueError:
        raise ValidationError(_("Invalid input for a Location instance. Latitude must be convertible to float "))
    try:
        lng = float(lng)
    except ValueError:
        raise ValidationError(_("Invalid input for a Location instance. Longitude must be convertible to float "))

    return lng, lat


class LocationField(forms.CharField):
    """custom form field for picking location"""

    def __init__(self, *args, **kwargs):
        map_attrs = kwargs.pop("map_attrs", None)
        
        super().__init__(*args, **kwargs)
        self.widget = MapInput(map_attrs=map_attrs, )
        self.error_messages = {"required": "Please pick a location, it's required", }

    def to_python(self, value):
        return super().to_python(reverse_tuple_string(value))


class AddressAutoHiddenField(forms.CharField):
    """custom form field which uses AddressAutoHiddenInput"""
    widget = AddressAutoHiddenInput()

    def __init__(self, *args, **kwargs):
        map_id = kwargs.pop("map_id", "map")
        self.widget = AddressAutoHiddenInput(map_id=map_id)
        
class AddressCountryField(forms.CharField):
    """custom form field which uses AddressCountry"""
    widget = AddressCountry()

    def __init__(self, *args, **kwargs):
        map_id = kwargs.pop("map_id", "map")
        self.widget = AddressCountry(map_id=map_id)
        super().__init__(*args, **kwargs)
        self.label = ""

class AddressRegionField(forms.CharField):
    """custom form field which uses AddressRegion"""
    widget = AddressRegion()

    def __init__(self, *args, **kwargs):
        map_id = kwargs.pop("map_id", "map")
        self.widget = AddressRegion(map_id=map_id)
        super().__init__(*args, **kwargs)
        self.label = ""

class AddressDistrictField(forms.CharField):
    """custom form field which uses AddressDistrict"""
    widget = AddressDistrict()

    def __init__(self, *args, **kwargs):
        map_id = kwargs.pop("map_id", "map")
        self.widget = AddressDistrict(map_id=map_id)
        super().__init__(*args, **kwargs)
        self.label = ""

class AddressPlaceField(forms.CharField):
    """custom form field which uses AddressPlace"""
    widget = AddressPlace()

    def __init__(self, *args, **kwargs):
        map_id = kwargs.pop("map_id", "map")
        self.widget = AddressPlace(map_id=map_id)
        super().__init__(*args, **kwargs)
        self.label = ""

class AddressLocalityField(forms.CharField):
    """custom form field which uses AddressLocality"""
    widget = AddressLocality()

    def __init__(self, *args, **kwargs):
        map_id = kwargs.pop("map_id", "map")
        self.widget = AddressLocality(map_id=map_id)
        super().__init__(*args, **kwargs)
        self.label = ""

class AddressPostcodeField(forms.CharField):
    """custom form field which uses AddressPostcode"""
    widget = AddressPostcode()

    def __init__(self, *args, **kwargs):
        map_id = kwargs.pop("map_id", "map")
        self.widget = AddressPostcode(map_id=map_id)
        super().__init__(*args, **kwargs)
        self.label = ""

class AddressLineField(forms.CharField):
    """custom form field which uses AddressLine"""
    widget = AddressLine()

    def __init__(self, *args, **kwargs):
        map_id = kwargs.pop("map_id", "map")
        self.widget = AddressLine(map_id=map_id)
        super().__init__(*args, **kwargs)
        self.label = ""
        super().__init__(*args, **kwargs)
        self.label = ""
