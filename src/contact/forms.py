from django import forms

# make sure this is at the top if it isn't already
from django import *


# our new form
class ContactForm(forms.Form):
    name = forms.CharField(required=False, max_length=100, help_text='100 charaters max' )
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)

    #def __init__(self, *args, **kwargs):
       # super(ContactForm, self).__init__(*args, **kwargs)
      #  self.fields['name'].label = "Your name:"
      #  self.fields['email'].label = "Your email:"
      #  self.fields['comment'].label = "What do you want to say?"