from django.conf.urls import url

from . import views

urlpatterns = [
  path('/contact/new', views.contact_create, name='contact_new'),
  path('/contact/edit/<int:pk>', views.contact_update, name='contact_edit'),
  path('/contact/delete/<int:pk>', views.contact_delete, name='contact_delete'),
  path('/contacts', views.contact_list, name='contact_list'),
  path('/contact', views.contact_view, name='contact_view'),
]