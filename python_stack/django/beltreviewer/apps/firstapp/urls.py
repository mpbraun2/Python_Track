from django.conf.urls import url
from . import views
# from views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register', views.register, name='register'),
    url(r'^success$', views.success, name='success'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^add_book$', views.add_book, name='add_book'),
    url(r'^show_book$', views.show_book, name='show_book'),
    url(r'^show_users$', views.show_users, name='show_users'),
    url(r'^delete_user/(?P<user_id>\d+)$', views.delete_user, name='delete_user'),
    url(r'^user_profile/(?P<user_id>\d+)$', views.user_profile, name="user_profile"),
    url(r'^update_user/(?P<user_id>\d+)$', views.update_user, name='update_user'),
    url(r'^edit_user/(?P<user_id>\d+)$', views.edit_user, name="edit_user")
]
