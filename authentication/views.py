from django.shortcuts import render
from .forms import SignupForm
from django.http import HttpResponseRedirect


def signup(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            u = form.save(commit=False)   # ❗ don't save yet
            u.set_password(form.cleaned_data['password'])  # ✅ hash password properly
            u.save()
            return HttpResponseRedirect('/accounts/login/')

    return render(request, 'signup.html', {'form': form})