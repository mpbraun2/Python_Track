from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register$', views.register, name="register"),
    url(r'^success$', views.success, name="success"),
    url(r'^login$', views.login, name="login"),
    url(r'^add_appointment$', views.add_appointment, name="add_appointment"),
    url(r'^delete_appointment$', views.delete_appointment, name="delete_appointment"),
    url(r'^update_appointment/(?P<id>\d+)$', views.update_appointment, name="update_appointment"),
]
