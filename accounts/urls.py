from django.conf.urls import url

from . import views


urlpatterns = [
    url('signup/', views.sign_up.as_view(), name='signup'),
]
