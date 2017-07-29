from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.conf import settings #import everything from settings
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages

from .models import ModuleRequest
from .forms import ModuleRequestForm
from comments.models import Comment
from comments.forms import CommentForm
# Create your views here.
@login_required
def create_module_request(request):
	form = ModuleRequestForm(request.POST or None)
	title = "Module Request"
	title_align_center = True
	if form.is_valid():
		instance = form.save(commit = False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Module Request Sent!")

	context = {
		"title": title,
		"form": form,

	}

	return render(request, "module_request.html", context)

@login_required
def search_module_requests(request):
	queryset = ModuleRequest.objects.all()
	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(
			Q(module_requested__icontains=query) |
			Q(full_name__icontains=query)
			)

	
	context = {
		"requests": queryset,
		"title": "Search For Tutee"

	}

	return render(request, "module_requests_search.html", context)

@login_required
def module_request_detail(request, id = None):
	instance = get_object_or_404(ModuleRequest, id = id)
	initial_data = {
		"content_type": instance.get_content_type,
		"object_id": instance.id
	}
	form = CommentForm(request.POST or None, initial = initial_data)
	
	if form.is_valid():
		c_type = form.cleaned_data.get("content_type")
		content_type = ContentType.objects.get(model="modulerequest")
		obj_id = form.cleaned_data.get('object_id')
		content_data = form.cleaned_data.get("content")
		parent_obj = None
		try:
			parent_id = int(request.POST.get("parent_id"))
		except:
			parent_id = None

		if parent_id:
			parent_qs = Comment.objects.filter(id = parent_id)
			if parent_qs.exists() and parent_qs.count() == 1:
				parent_obj = parent_qs.first()

		new_comment, created = Comment.objects.get_or_create(
									user = request.user,
									content_type = content_type,
									object_id = obj_id,
									content = content_data,
									parent = parent_obj,


							    )
		return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
	
	comments = Comment.objects.filter_by_instance(instance)
	context = {
		"instance": instance,
		"comments": comments,
		"form": form

	}
	return render(request, "module_request_detail.html", context)
