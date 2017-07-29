from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType

from comments.models import Comment

class ModuleRequest(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1)
	full_name = models.CharField(max_length=120, blank=False)
	contact_number = models.CharField(max_length=120, blank=False)
	expected_tuition_cost = models.IntegerField(default = 10, blank = False)
	module_requested = models.CharField(max_length=120, blank=False)


	def __str__(self):
		return self.full_name

	def get_absolute_url(self):
		return reverse("detail_module_request", kwargs = {"id":self.id})

	@property
	def comments(self):
		instance = self
		qs = Comments.objects.filter_by_instance(instance)
		return qs

	@property
	def get_content_type(self):
		instance = self
		content_type = ContentType.objects.get_for_model(instance.__class__)
		return content_type


