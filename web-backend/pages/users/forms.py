from django import forms

from custom.user.models import CustomUser
from django.contrib.auth.hashers import (
    make_password,
)


class UserEditInfoForm(forms.ModelForm):

    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "input ",
                "value": "",
                "placeholder": "Password",
            },
        ),
    )
    confirm_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "input ",
                "value": "",
                "placeholder": "Confirm Password",
            },
        ),
    )

    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "username",
            "avatar_url",
            "password",
        ]

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "input",
                    "placeholder": "First Name",
                },
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "input",
                    "placeholder": "Last Name",
                },
            ),
            "username": forms.TextInput(
                attrs={
                    "class": "input",
                    "placeholder": "Username",
                },
            ),
            "avatar_url": forms.Select(
                attrs={
                    "class": "select-items",
                }
            ),
        }

    def clean(self):
        cleaned_data = super(UserEditInfoForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error("confirm_password", "Password does not match")

        if password == "":
            cleaned_data.pop("password")
            cleaned_data.pop("confirm_password")

        else:
            hashed_password = make_password(password)
            cleaned_data["password"] = hashed_password
            cleaned_data["confirm_password"] = hashed_password

        return cleaned_data
