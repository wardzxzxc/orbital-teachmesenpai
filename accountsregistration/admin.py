from django.contrib import admin

# Register your models here.
# from .forms import SignUpForm
from .models import AccountsProfile
from modulerequest.models import ModuleRequest
from django.contrib.auth.models import User

class AccountsProfileAdmin(admin.ModelAdmin):
	list_display = ["user", "points", "full_name", "contact_number", "tuition_cost", "course", "faculty", "module_to_offer_1", "module_to_offer_2", "module_to_offer_3", "place_of_convenience" ]
	class Meta:
		model = AccountsProfile

admin.site.register(AccountsProfile, AccountsProfileAdmin)




#Example:
# class SignUpAdmin(admin.ModelAdmin):
# 	list_display = ["__str__", "timestamp", "updated"]
# 	form = SignUpForm
# 	#class Meta:
# 		#model = SignUp