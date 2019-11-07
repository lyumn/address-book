from django.conf.urls import url

from . import views

urlpatterns = [
  url('contact/new', views.contact_create, name='contact_new'),
  url('contact/edit/<int:pk>', views.contact_update, name='contact_edit'),
  url('contact/delete/<int:pk>', views.contact_delete, name='contact_delete'),
  url('contacts', views.contact_list, name='contact_list'),
  url('contact', views.contact_view, name='contact_view'),
]