from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import KyuskUserCreationForm


class SignUpView(CreateView):
    form_class = KyuskUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
