from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from ..forms import LoginForm
from ..models import Notice

# ログイン
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                return redirect(to='/conspro2/top/')

    else:
        form = LoginForm()

    param = {'form': form,}

    return render(request, 'login.html', param)

# ログアウト
def logout_view(request):
    logout(request)
    return redirect(to='/conspro2/login/')

# トップ
@login_required
def top_view(request):
    user = request.user
    params = {'user': user, 'notice_list': Notice.objects.order_by('id').reverse()}
    return render(request, 'top.html', params)
