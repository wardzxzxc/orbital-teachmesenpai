from django import forms
from .models import ModuleRequest

class ModuleRequestForm(forms.ModelForm):
	class Meta:
		model = ModuleRequest
		fields = ["full_name", "contact_number", "expected_tuition_cost", "module_requested"]
