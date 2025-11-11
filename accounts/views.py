from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم موجود مسبقًا ❌")
            return redirect("signup")

        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user, phone=phone, address=address)

        messages.success(request, "تم إنشاء الحساب بنجاح ✅")
        return redirect("login")

    return render(request, "account-templates/signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")  # تعديل لاحقًا حسب رغبتك
        else:
            messages.error(request, "بيانات الدخول غير صحيحة ❌")

    return render(request, "account-templates/login.html")
