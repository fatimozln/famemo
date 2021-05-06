from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout as logout_library
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser, AbstractBaseUser
from django.views.generic import DetailView
from accounts.models import MyUser

# Create your views here.


@login_required(login_url='/accounts/login')
def profile_show(request, user_id):
    profile = models.Profile.objects.get(user_id=user_id)
    return render(request, 'profiles/profile_page.html', {'profile': profile})


""" @login_required(login_url='/accounts/login')
def delete_user(request, user_id):
    u = models.Profile.objects.get(user_id=user_id)
    u.delete()
    if u.deleted():
        return HttpResponse("The user is deleted")
    else:
        return HttpResponse("The user not found")
 """


""" @login_required(login_url='/accounts/login')
def delete_user(request, username):
    user = models.Profile.objects.get(username=username)
    user.delete()
    return redirect('accounts:signup')
    return render(request, 'profiles/profile_page.html', {'user': user})
    return HttpResponse(request, "Deleted") """


""" @login_required(login_url='/accounts/login')
def delete_user(request, user_id):
    profile = models.User.objects.get(user_id=user_id)
    profile.delete()
    return redirect('accounts:signup') """


def delete_user(request, username):
    try:
        u = models.MyUser.objects.get(username=username)
        if u.username == "superuser":
            return HttpResponse("The user is Admin becuse can not delete")
        else:
            u.delete()
            return redirect('accounts:login')
    except:
        return HttpResponse(request, "The user not found")


@login_required
def deactive_user(request):
    user = request.user
    if user.is_superuser:
        return HttpResponse("The user is Admin becuse can not deactive")
    if user.status == "active":
        user.status = "deactive"
        user.save()
        logout_library(request)
        return HttpResponse("The user is deactive", id)
    else:
        pass
