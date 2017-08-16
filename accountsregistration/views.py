from django.shortcuts import render, get_object_or_404
from django.conf import settings #import everything from settings
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


from .forms import AccountsProfileForm
from .models import AccountsProfile


# Create your views here.

def home(request):
	title = 'Welcome' #view function variable 

	return render(request, "home.html", {})

def about(request):
	return render(request, "about.html", {})

@login_required
def accounts_profile(request):
	form = AccountsProfileForm(request.POST or None)
	title = "Profile"
	title_align_center = True
	if form.is_valid():
		instance = form.save(commit = False)
		print(form.cleaned_data.get("title"))
		instance.save()
		messages.success(request, 'Tutor profile created!')

	context = {
		"title": title,
		"form": form,

	}

	return render(request, "profile_create.html", context)

@login_required
def update_profile(request):
	try:
		instance = AccountsProfile.objects.get(user = request.user)
		form = AccountsProfileForm(request.POST or None, instance = instance)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.save()
			messages.success(request, 'Tutor profile saved!')

		context = {
			"instance": instance,
			"form": form,
			}

		return render(request, "profile_create.html", context )
	except ObjectDoesNotExist:
		return accounts_profile(request)


@login_required
def points_status(request):
	all_profiles = AccountsProfile.objects.all()
	profile = all_profiles.get(user = request.user)
	points = profile.points
	achievement = None
	if points < 100:
		achievement = 'Amateur Senpai'
	elif points < 200:
		achievement = 'Advanced Senpai'
	elif points >= 200:
		achievement = 'Master Sensei'

	context = {
	"achievement_level": achievement,
	"points": points
	}

	return render(request, "point_status.html", context)

@login_required
def profile_list(request): #list profiles
	queryset = AccountsProfile.objects.all()
	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(
			Q(module_to_offer_1__icontains=query) |
			Q(module_to_offer_2__icontains=query) |
			Q(module_to_offer_3__icontains=query) |
			Q(full_name__icontains=query) 
			)

	
	context = {
		"profiles_list": queryset,
		"title": "Search For Tutor"

	}

	return render(request, "profile_search.html", context)


