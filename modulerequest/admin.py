from django.contrib import admin

from .models import ModuleRequest
from django.contrib.auth.models import User
# Register your models here.

class ModuleRequestAdmin(admin.ModelAdmin):
	list_display= ["user", "full_name", "contact_number", "expected_tuition_cost", "module_requested"]
	class Meta:
		model = ModuleRequest

admin.site.register(ModuleRequest, ModuleRequestAdmin)