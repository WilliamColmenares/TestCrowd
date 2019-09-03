from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Pet
from .forms import LoginForm, PetForm


@login_required
def pet_list(request):
    context = {
        'pets': Pet.objects.filter(owner=request.user),
    }
    return render(request, 'dashboard.html', context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard')
    context = {
        'form': LoginForm
    }
    return render(request, 'login.html', context)


@login_required
def create_pet(request):
    context = {
        'form': PetForm()
    }
    if request.method == "POST":
        form = PetForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            return redirect('/dashboard')
    return render(request, 'create.html', context)


@login_required
def update_pet(request, id=None):
    instance = get_object_or_404(Pet, id=id)
    if instance.owner != request.user:  # Just to make sure its the pet owner
        return redirect('/dashboard')
    form = PetForm(request.POST or None, instance=instance)
    context = {
        'form': form,
        'instance': instance
    }
    if form.is_valid():
        form.save()
        return redirect('/dashboard')
    return render(request, 'edit.html', context)


@login_required
def delete_pet(request, id=None):
    instance = get_object_or_404(Pet, id=id)
    if instance.owner != request.user:  # Just to make sure its the pet owner
        return redirect('/dashboard')
    instance.delete()
    return redirect('/dashboard')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
