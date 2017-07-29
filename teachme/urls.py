"""teachme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accountsregistration.views import home, accounts_profile, profile_list, update_profile, points_status
from modulerequest.views import create_module_request, search_module_requests, module_request_detail
from teachme.views import about
from django.conf.urls.static import static
from django.conf import settings
from accountsregistration.forms import AccountsProfileForm
from registration.backends.default.views import RegistrationView


urlpatterns = [
	url(r'^$', home, name='home'),
    url(r'^profile_create$', accounts_profile, name='profile'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^profile_search$', profile_list, name='profile_search'),
    url(r'^profile_edit$', update_profile, name='profile_update'),
    url(r'^friendship/', include('friendship.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^points_status$', points_status, name='point_status'),
    url(r'^module_request$', create_module_request, name='create_module_request'),
    url(r'^module_request_search$', search_module_requests, name='search_module_requests'),
    url(r'^(?P<id>\d+)$', module_request_detail, name='detail_module_request'),
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)