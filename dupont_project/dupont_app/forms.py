from django import forms
from .models import Contact, ImagePred

class ContactForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['question'].label = 'Have a Question?'
		self.fields['contact_prefer'].label = 'How do you prefer to be contacted?'
		self.fields['contact_prefer'].widget = forms.RadioSelect()
		self.fields['receive_alerts'].label = "I would like to receive news, events and industry insights from DuPont Electronic Solutions and other related DuPont businesses."
	class Meta:
		model = Contact
		fields = '__all__'		

class ImageForm(forms.ModelForm):
	class Meta:
		model = ImagePred
		fields = ('image','created_by')