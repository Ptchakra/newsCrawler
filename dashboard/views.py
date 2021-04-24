from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from trangWeb.models import TrangWeb, BaiBao, tong_bai_hang_ngay, tu_khoa, top50, so_bai_tung_trang
from datetime import timedelta
def index(request):

    bai_viet_10_ngay = tong_bai_hang_ngay.objects.filter().order_by("-ngay_them")[:10]
    # print(str(so_bai_10_ngay))
    # print(type(bai_viet_10_ngay))
    so_bai_10_ngay = []
    ten_10_ngay = []
    if(bai_viet_10_ngay.count()<10):
        lastday = 0
        for bai_viet in bai_viet_10_ngay:
            so_bai_10_ngay.append(bai_viet.so_bai_viet)
            ten_10_ngay.append(f"{bai_viet.ngay_them.astimezone().day}.{bai_viet.ngay_them.astimezone().month}")
            lastday = bai_viet.ngay_them.astimezone()
        for i in range(bai_viet_10_ngay.count(),10):
            so_bai_10_ngay.append(0)
            lastday = lastday - timedelta(days=1)
            ten_10_ngay.append(f"{lastday.day}.{lastday.month}")
            
    else:
        for bai_viet in bai_viet_10_ngay[:10]:
            so_bai_10_ngay.append(bai_viet.so_bai_viet)
            ten_10_ngay.append(f"{bai_viet.ngay_them.astimezone().day}.{bai_viet.ngay_them.astimezone().month}")
    
    so_bai_10_ngay.reverse()
    ten_10_ngay.reverse()
    print(so_bai_10_ngay)
    print(ten_10_ngay)
    

    top_10_trang_web =  so_bai_tung_trang.objects.filter().order_by("-so_bai_viet")
    if top_10_trang_web.count() > 10:
        top_10_trang_web = top_10_trang_web[0:10]
    so_bai_top_10_trang_web = []
    ten_top_10_trang_web = []
    for i in top_10_trang_web:
        so_bai_top_10_trang_web.append(i.so_bai_viet)
        ten_top_10_trang_web.append(i.trang_web)
    
    print(so_bai_top_10_trang_web)
    print(ten_top_10_trang_web)

    top_50_bai_moi = top50.objects.filter().order_by("ngay_them")
    top50_tieu_de = []
    top50_link = []
    for i in top_50_bai_moi:
        top50_tieu_de.append(i.tieu_de)
        top50_link.append(i.link_bai_bao)
    
    print(top50_tieu_de)
    print(top50_link)
    context = {
        'dashboard_data_active': 'true',
        'so_bai_10_ngay' : so_bai_10_ngay,
        'ten_10_ngay' : ten_10_ngay,
        'top_10_trang_web' : so_bai_top_10_trang_web,
        'ten_10_trang_web' : ten_top_10_trang_web,
        'top_bai_bao' : so_bai_top_10_trang_web,
        'tu_khoa' : '',
        }
    return render(request, 'dashboard/index.html', context)


def profile(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request,
                'Your password was successfully changed!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'dashboard/profile.html', {
        'form': form
    })


@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    messages.add_message(
        request,
        messages.INFO,
        'You have been successfully logged out. Thank you ' +
        'for using reNgine.')


@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    messages.add_message(
        request,
        messages.INFO,
        'Hi @' +
        request.user.username +
        ' welcome back!')
