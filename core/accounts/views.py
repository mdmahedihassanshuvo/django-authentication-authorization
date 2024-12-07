from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomRegistrationForm, CustomLoginForm


class RegistrationView(FormView):
    template_name = 'accounts/register.html'
    form_class = CustomRegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Registration successful.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Registration failed.')
        return super().form_invalid(form)


class CustomLoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = CustomLoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        identifier = form.cleaned_data['identifier']
        password = form.cleaned_data['password']

        user = None
        if CustomUser.objects.filter(username=identifier).exists():
            user = CustomUser.objects.get(username=identifier)
        elif CustomUser.objects.filter(email=identifier).exists():
            user = CustomUser.objects.get(email=identifier)
        elif CustomUser.objects.filter(phone_number=identifier).exists():
            user = CustomUser.objects.get(phone_number=identifier)

        if user:
            user = authenticate(
                self.request, username=user.username, password=password
            )
            if user:
                login(self.request, user)
                messages.success(self.request, 'Login successful.')
                return super().form_valid(form)
            else:
                messages.error(self.request, 'Invalid password.')
        else:
            messages.error(self.request, 'User not found.')
            return super().form_invalid()

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)
