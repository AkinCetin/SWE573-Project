from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUserModel


class creationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )
