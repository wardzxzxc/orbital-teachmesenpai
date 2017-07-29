from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class AccountsProfile(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1)
	full_name = models.CharField(max_length=120, blank=False)
	contact_number = models.CharField(max_length=120, blank=False)
	course = models.CharField(max_length=120, blank=False)
	faculty = models.CharField(max_length=120, blank=False)
	tuition_cost = models.IntegerField(default = 10, blank = False)
	points = models.IntegerField(default = 100)
	module_to_offer_1 = models.CharField(max_length=120, blank=True)
	module_to_offer_2 = models.CharField(max_length=120, blank=True)
	module_to_offer_3 = models.CharField(max_length=120, blank=True)
	place_of_convenience = models.CharField(max_length=120, blank=False)

	def __str__(self):
		return self.full_name

	




























# Create your models here.
# class SignUp(models.Model):
# 	full_name = models.CharField(max_length=120, blank=True)
# 	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
# 	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

# def __str__(self):
# # 		return self.email

	# def user_registered_callback(sender, user, request, **kwargs):
	# 	profile = AccountsProfile(user = user)
	# 	profile.full_name = char(request.POST["full_name"])
	# 	profile.course = char(request.POST["course"])
	# 	profile.faculty = char(request.POST["faculty"])
	# 	profile.module_to_offer_1 = char(request.POST["module_to_offer_1"])
	# 	profile.module_to_offer_2 = char(request.POST["module_to_offer_2"])
	# 	profile.module_to_offer_3 = char(request.POST["module_to_offer_3"])
	# 	profile.place_of_convenience = char(request.POST["place_of_convenience"])
	# 	profile.save()

	# user_registered.connect(user_registered_callback)
	

# class ExUserProfie(models.Model):
# 	user = models.ForeignKey(User, unique = True)
# 	is_human = models.BooleanField()

# 	def __str__(self):
# 		return self.user

# 	def user_registered_callback(sender, user, request, **kwargs):
# 		profile = ExUserProfile(user = user)
# 		profile.is_human= bool(request.POST["is_human"])
# 		profile.save()

# 	user_registered.connect(user_registered_callback)