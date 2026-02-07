from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserRegisterForm, ProfileForm


from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfileForm


class RegisterView(View):
    template_name = 'accounts/register.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('notice:notice_list')

        form = UserRegisterForm()
        profile_form = ProfileForm()
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'profile_form': profile_form,
            },
        )

    def post(self, request):
        form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if form.is_valid() and profile_form.is_valid():
            # Save user (post_save signal will create Profile)
            user = form.save(commit=False)
            if 'email' in form.cleaned_data:
                user.email = form.cleaned_data['email']
            user.save()

            # Update the auto-created profile
            profile = user.profile
            for field, value in profile_form.cleaned_data.items():
                setattr(profile, field, value)
            profile.save()

            messages.success(request, "Registration successful! You can now log in.")
            return redirect('accounts:login')

        # If we reach here, something is wrong
        messages.error(request, "Unable to register. Please fix the errors below.")
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'profile_form': profile_form,
            },
        )


class LoginView(View):
    template_name = 'accounts/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('notice:notice_list')
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('notice:notice_list')

        messages.error(request, 'Invalid username or password.')
        return render(request, self.template_name)


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have logged out successfully.")
        return redirect('accounts:login')


class ProfileView(LoginRequiredMixin, View):
    template_name = 'accounts/profile.html'
    login_url = 'accounts:login'

    def get(self, request):
        profile = request.user.profile
        profile_form = ProfileForm(instance=profile)
        return render(
            request,
            self.template_name,
            {
                'profile': profile,
                'profile_form': profile_form,
            },
        )

    def post(self, request):
        profile = request.user.profile
        profile_form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('accounts:profile')

        messages.error(request, 'Please correct the errors below.')
        return render(
            request,
            self.template_name,
            {
                'profile': profile,
                'profile_form': profile_form,
            },
        )
