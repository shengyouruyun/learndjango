from django import forms

class InvitationForm(forms.Form):
	email = forms.CharField(widget=forms.TextInput(attr={'size':32, 
		'placeholder':'Email address of firend to invite',
	 'class':'form-control search-query'}))

	