from django.conf.urls import url
from . import views
# from views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^appointments$', views.appointments, name='appointments'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^edit_appointment/(?P<user_id>\d+)$', views.edit_appointment, name='edit_appointment'),
    url(r'^add_appointment/(?P<user_id>\d+)$', views.add_appointment, name='add_appointment'),
]
