from django import forms

from .models import Member

class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ('Fname', 'Lname', 'email', 'phone', 'membership_tier', 'home_address', 'preferred_mode_of_contact')

class SearchForm(forms.Form):
    fields = ('search')