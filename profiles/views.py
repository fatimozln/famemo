from django.shortcuts import render, redirect, HttpResponse
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser, AbstractBaseUser, User
from django.views.generic import DetailView
# Create your views here.


@login_required(login_url='/accounts/login')
def profile_show(request, user_id):
    profile = models.Profile.objects.get(user_id=user_id)
    return render(request, 'profiles/profile_page.html', {'profile': profile})


""" @login_required(login_url='/accounts/login')
def profile_show(request, user):
    profile = models.Profile.objects.get(id=user)
    try:
        return render(request, 'templates/articles_detail.html', {'profile': profile})
    except profile.DoesNotExist:
        raise HttpResponse("No MyModel matches the given query.")
 """

""" class Profile(DetailView):
    models = models.Profile
    template_name = "profile/profile_page.html"
 """

""" @login_required(login_url='/accounts/login')
def profile_show(request):
    profile = models.Profile.objects.all()
    user = request.user
    if request.method == 'POST':
        form = forms.Showprofile(request.POST)
        if profile.user == request.user:
            if form.is_valid():
                return redirect('profile:show')
        form = forms.Showprofile()
    return render(request, 'profile/profile_page.html', {'form': form}) """
