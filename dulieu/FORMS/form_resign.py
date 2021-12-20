from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ResignForm(UserCreationForm):
    error_css_class = 'loi'
    class Meta:
        model= User
        fields= "__all__"
