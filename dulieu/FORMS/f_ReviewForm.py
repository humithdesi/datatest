from ..Models.M_Product import Review
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model= Review
        fields= "__all__"
