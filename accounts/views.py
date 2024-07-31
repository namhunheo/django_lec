from django.contrib.auth import login
from django.shortcuts import render, redirect
from accounts.forms import SignupForm  # SignupForm을 정확히 임포트합니다

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # 새 사용자 객체를 저장합니다
            login(request, user)  # 새로 가입한 사용자를 로그인 상태로 만듭니다
            return redirect('/')  # 가입 후 메인 페이지로 리다이렉트합니다
        else:
            # 폼이 유효하지 않은 경우, 사용자에게 오류를 표시할 수 있습니다
            return render(request, 'accounts/signup.html', {'form': form})
    else:
        form = SignupForm()  # GET 요청 시 빈 폼을 생성합니다

    return render(request, 'accounts/signup.html', {'form': form})
