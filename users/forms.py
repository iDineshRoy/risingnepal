from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import CustomUser


class UserRegistrationForm(forms.ModelForm):
    user_type = forms.ChoiceField(
        choices=(
            ("admin", "Admin"),
            ("manager", "Manager"),
            ("operator", "Operator"),
            ("staff", "Staff"),
            ("teacher", "Teacher"),
        )
    )

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = CustomUser
        fields = ("username", "password1", "password2", "email", "user_type")

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    user_type = forms.ChoiceField(
        choices=(
            ("admin", "Admin"),
            ("manager", "Manager"),
            ("operator", "Operator"),
            ("staff", "Staff"),
            ("teacher", "Teacher"),
        )
    )
