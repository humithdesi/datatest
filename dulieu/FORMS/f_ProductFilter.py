from django_filters.filters import ModelChoiceFilter
from ..Models.M_Product import BoSuuTap, LoaiNem, Product
from django_filters import FilterSet
class ProductFilter(FilterSet):

    class Meta:
        model=Product
        fields = ['name','loaiNem','boSuuTap','price','thuongHieu']