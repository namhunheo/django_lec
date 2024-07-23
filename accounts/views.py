from django.contrib.auth import login
from django.shortcuts import render, redirect
from accounts.forms import SignupForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        # 이 부분에서 새로운 폼을 생성하지 않고 기존 폼을 그대로 유지합니다.
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})
