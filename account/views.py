
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.
def profile_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        profile = Profile.objects.create(user=request.user)
        profile.save()

    username = request.user.username
    context = {
        'profile': profile,
    }
    return render(request, 'account/profile.html', context=context)


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    user = User.objects.get(username=profile.user)

    if request.method == 'POST':
        user.username = request.POST.get('username')
        profile.name = request.POST.get('name')
        profile.surname = request.POST.get('surname')
        profile.bio = request.POST.get('bio')
        profile.img = request.POST.get('img')
        profile.birth_date = request.POST.get('birth_date')
        profile.save()
        user.save()
        return redirect('profile')

    return render(request, 'account/profile_edit.html', context={'profile': profile,
                                                                 'user': user})