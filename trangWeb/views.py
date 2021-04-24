import io
import os
from django.shortcuts import render, get_object_or_404
from django import http
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
import validators
from trangWeb.forms import AddTargetForm, UpdateTargetForm
from django.urls import reverse
from .models import TrangWeb, top50, so_bai_tung_trang, tong_bai_hang_ngay
from django.utils import timezone
from datetime import datetime

def index(request):
    context = {
        'trangWeb_data_active': 'true'}
    return render(request, 'trangWeb/index.html', context)

def them_trang_web_form(request):
    form = AddTargetForm(request.POST or None)
    print("them trang web form")
    if request.method == "POST":
        if form.is_valid():
            print("form clean data ----", form.cleaned_data["link_trang_web"])
            if validators.url(form.cleaned_data["link_trang_web"]):
                if not bool(TrangWeb.objects.filter(link_trang_web=form.cleaned_data["link_trang_web"])):
                    TrangWeb.objects.create(
                        **form.cleaned_data,
                        ngay_them=datetime.now(),
                        trang_thai_chay = True)
                    so_bai_tung_trang.objects.create(trang_web=form.cleaned_data["link_trang_web"], so_bai_viet=0)

                    messages.add_message(
                        request,
                        messages.INFO,
                        'Target domain ' +
                        form.cleaned_data['link_trang_web'] +
                        ' added successfully')
                    return http.HttpResponseRedirect(reverse('danh_sach_trang_web'))
                else:
                    messages.add_message(
                        request,
                        messages.INFO,
                        'Target domain ' +
                        form.cleaned_data['link_trang_web'] +
                        ' have already exist')
                    return http.HttpResponseRedirect(reverse('danh_sach_trang_web'))
    context = {
        "add_target_li": "active",
        "target_data_active": "true",
        'form': form}
    return render(request, 'trangWeb/add.html', context)

def danh_sach_trang_web(request):
    # tat_ca_trang_web  = TrangWeb.objects.filter().order_by("")
    context = {
        'list_target_li': 'active',
        'target_data_active': 'true'}
    return render(request, 'trangWeb/list.html', context)


def danh_sach_bai_bao(request):
    print(request)
    context = {
        'list_target_li': 'active',
        'target_data_active': 'true'}
    return render(request, 'baiBao/list.html', context)

def sua_trang_web_form(request, id):
   
    context = {
        'list_target_li': 'active',
        'target_data_active': 'true'}
    return render(request, 'trangWeb/update.html', context)

def xoa_trang_web(request, id):
    responseData = {'status': 'false'}
    return http.JsonResponse(responseData)