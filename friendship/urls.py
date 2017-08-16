try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url
from friendship.views import view_friends, friendship_add_tutor, friendship_accept, \
    friendship_reject, friendship_cancel, friendship_received_list, \
    friendship_request_list_rejected, friendship_requests_detail, followers,\
    following, follower_add, follower_remove, all_users, friendship_sent_list, view_tutees, friendship_add_tutee

urlpatterns = [
    url(
        regex=r'^users/$',
        view=all_users,
        name='friendship_view_users',
    ),
    url(
        regex=r'^friends/(?P<username>[\w-]+)/$',
        view=view_friends,
        name='friendship_view_friends',
    ),
    url(
        regex=r'^friend/add_tutor/(?P<to_username>[\w-]+)/$',
        view=friendship_add_tutor,
        name='friendship_add_tutor',
    ),
      url(
        regex=r'^friend/add_tutee/(?P<to_username>[\w-]+)/$',
        view=friendship_add_tutee,
        name='friendship_add_tutee',
    ),
    url(
        regex=r'^friend/accept/(?P<friendship_request_id>\d+)/$',
        view=friendship_accept,
        name='friendship_accept',
    ),
    url(
        regex=r'^friend/reject/(?P<friendship_request_id>\d+)/$',
        view=friendship_reject,
        name='friendship_reject',
    ),
    url(
        regex=r'^friend/cancel/(?P<friendship_request_id>\d+)/$',
        view=friendship_cancel,
        name='friendship_cancel',
    ),
    url(
        regex=r'^friend/tutee_requests_received/$',
        view=friendship_received_list,
        name='tutee_request_received_list',
    ),
    url(
        regex=r'^friend/tutor_requests_sent/$',
        view=friendship_sent_list,
        name='tutor_request_sent_list',
    ),        
    url(
        regex=r'^friend/requests/rejected/$',
        view=friendship_request_list_rejected,
        name='friendship_requests_rejected',
    ),
    url(
        regex=r'^friend/request/(?P<friendship_request_id>\d+)/$',
        view=friendship_requests_detail,
        name='friendship_requests_detail',
    ),
    url(
        regex=r'^followers/(?P<username>[\w-]+)/$',
        view=followers,
        name='friendship_followers',
    ),
    url(
        regex=r'^following/(?P<username>[\w-]+)/$',
        view=following,
        name='friendship_following',
    ),
    url(
        regex=r'^follower/add/(?P<followee_username>[\w-]+)/$',
        view=follower_add,
        name='follower_add',
    ),
    url(
        regex=r'^follower/remove/(?P<followee_username>[\w-]+)/$',
        view=follower_remove,
        name='follower_remove',
    ),
      url(
        regex=r'^friend/your_tutees',
        view=view_tutees,
        name='view_tutees',
    ),
]
