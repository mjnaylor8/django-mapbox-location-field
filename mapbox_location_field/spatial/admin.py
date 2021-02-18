from .models import SpatialLocationField

from ..admin import MapAdmin
from ..models import LocationField, AddressAutoHiddenField, AddressCountryField, \
    AddressDistrictField, AddressRegionField, AddressLocalityField, \
    AddressPlaceField, AddressPostcodeField, AddressLineField
from ..widgets import MapAdminInput, AddressHiddenAdminInput, \
    AddressCountryAdmin, AddressDistrictAdmin, AddressRegionAdmin, \
    AddressLocalityAdmin, AddressPlaceAdmin, AddressPostcodeAdmin, AddressLineAdmin


class SpatialMapAdmin(MapAdmin):
    formfield_overrides = {
        LocationField: {'widget': MapAdminInput},
        SpatialLocationField: {'widget': MapAdminInput},
        AddressAutoHiddenField: {"widget": AddressHiddenAdminInput, },
        AddressCountryField: {"widget": AddressCountryAdmin, },
        AddressDistrictField: {"widget": AddressDistrictAdmin, },
        AddressRegionField: {"widget": AddressRegionAdmin, },
        AddressLocalityField: {"widget": AddressLocalityAdmin, },
        AddressPlaceField: {"widget": AddressPlaceAdmin, },
        AddressPostcodeField: {"widget": AddressPostcodeAdmin, },
        AddressLineField: {"widget": AddressLineAdmin, },
    }
