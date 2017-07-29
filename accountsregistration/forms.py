from registration.forms import RegistrationForm
from django import forms
from .models import AccountsProfile

class AccountsProfileForm(forms.ModelForm):
	class Meta:
		model = AccountsProfile
		fields = ['full_name', 'contact_number', 'course' , 'faculty' , 'tuition_cost' , 'module_to_offer_1' ,  'module_to_offer_2' , 'module_to_offer_3' , 'place_of_convenience']


# class ExRegistrationForm(RegistrationForm):
# 	is_human = forms.ChoiceField(label = "Are you human?:")
# class SignUpForm(forms.ModelForm):
# 	class Meta:
# 		model = SignUp
# 		fields = ['email', 'full_name' ]

# 	def clean_email(self):
# 		email = self.cleaned_data.get('email') #separate the email out
# 		email_user, provider = email.split("@")
# 		domain, extension = provider.split(".")
# 		if not domain == "gmail":
# 			raise forms.ValidationError("please use a valid gmail address")
# 		return email