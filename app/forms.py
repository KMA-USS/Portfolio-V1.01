from django import forms
from django.utils.translation import gettext_lazy as _

class Contactme(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email address'}))
    subject = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}))

    email.widget.attrs.update(
        {'class': 'text-lg bg-white p-2 shadow-sm hover:shadow-lg border border-gray-300 focus:border-2 focus:border-blue-500 placeholder-black'}
    )
    subject.widget.attrs.update(
        {'class': 'text-lg bg-white p-2 shadow-sm hover:shadow-lg border border-gray-300 focus:border-2 focus:border-blue-500 placeholder-black'}
    )
    message.widget.attrs.update(
        {'class': 'text-lg bg-white p-2 resize-none shadow-sm hover:shadow-lg border border-gray-300 focus:border-2 focus:border-blue-500 placeholder-black'}
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        email_server = email[email.find('@'):]
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError(
            _('Email server %(value)s is not supported'),
            code='UnsupportedEmailServer',
            params={'value': email_server}
        )
        return email
