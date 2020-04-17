
from django import forms
from swiggy.models import StateModel
from swiggy.models import CityModel
from swiggy.models import AreaModel
from swiggy.models import RestaurantTypeModel

class StateForm(forms.ModelForm):
    class Meta:
        model = StateModel
        fields = ('state_name',)

class CityForm(forms.ModelForm):
    class Meta:
        model = CityModel
        fields = "__all__"
        exclude = ('city_no',)

class AreaForm(forms.ModelForm):
    class Meta:
        model = AreaModel
        fields = "__all__"
        exclude = ('area_no',)

class RestaurantTypeForm(forms.ModelForm):
    class Meta:
        model = RestaurantTypeModel
        fields = ('type_name',)