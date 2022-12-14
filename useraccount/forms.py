""" Forms for Useraccount """
from django import forms
from .models import UserAccount, ReviewRating


class UserAccountForm(forms.ModelForm):
    """User Account form"""

    class Meta:
        """User Account form"""

        model = UserAccount
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        """
        Override init method to allow us to customize fields
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "email": "email",
            "contact_number": "Contact Number",
            "address1": "Address Line 1",
            "address2": "Address Line 2",
            "post_code": "Post Code",
            "city": "City",
            "county": "County",
        }

        self.fields["contact_number"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs[
                "class"
            ] = "border-black rounded-0 profile-form-input"
            self.fields[field].label = False


class ReviewRatingForm(forms.ModelForm):
    """User Service Review form"""

    class Meta:
        """User Service Review form"""

        model = ReviewRating
        fields = ["subject", "review", "rating"]
