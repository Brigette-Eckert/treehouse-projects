from django import forms
from django.core import validators


#custom validator  - could also use max_length validator in this case
def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty')


class SuggestionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Please verify your email address")
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               label="Leave Empty",
                               validators=[must_be_empty]
                               )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        verify = cleaned_data['verify_email']

        if email != verify:
            raise forms.ValidationError("Your email and verify email do not match!")

# Clean Honeypot function used before we were introduced to validators, an alternative method.
    # def clean_honeypot(self):
    #     honeypot = self.cleaned_data['honeypot']
    #     if len(honeypot):
    #         raise forms.ValidationError('Honeypot should be empty. BAD BOT!')
    #     return honeypot
