from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.views import generic


class sign_up(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
