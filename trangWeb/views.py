import io
import os
from django.shortcuts import render, get_object_or_404
from django import http
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, response
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
import validators
from trangWeb.forms import AddTargetForm, UpdateTargetForm
from django.urls import reverse
from .models import TrangWeb, top50, so_bai_tung_trang, tong_bai_hang_ngay, BaiBao
from django.utils import timezone
from datetime import datetime
import json

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

def search_bai_bao(request):
    # tat_ca_trang_web  = TrangWeb.objects.filter().order_by("")
    context = {}
    if request.method == 'POST':
        key_word = request.POST.get('keyWord', None)
        bai_bao = BaiBao.objects.filter().order_by("-ngay_them")[:10]
        danh_sach_ten = []
        for bai in bai_bao:
            danh_sach_ten.append(bai.tieu_de)
        context = {
            'danh_sach_ten': danh_sach_ten,
            'target_data_active': 'true'}
    print(json.dumps({'context': context}))
    return HttpResponse(json.dumps({'context': context}), content_type="application/json")

def load_noi_dung(request):
    # tat_ca_trang_web  = TrangWeb.objects.filter().order_by("")
    context = {}
    if request.method == 'POST':
        link = request.POST.get('link', None)
        bai_bao = BaiBao.objects.filter(link_bai_bao=link)[0]
        context = {
            'tieu_de': bai_bao.tieu_de,
            'noi_dung': bai_bao.noi_dung}
    print(json.dumps({'context': context}))
    return HttpResponse(json.dumps({'context': context}), content_type="application/json")

def danh_sach_bai_bao(request):
    baibao  = BaiBao.objects.filter().order_by("-ngay_them")[:10]
    so_bai_bao = BaiBao.objects.count()
    so_page =  int(int(so_bai_bao + 9)/10)
    tu_bai = 10
    now_page = 1   
    den_bai = 20
    context = {
        'list_target_li': 'active',
        'target_data_active': 'true',
        'bai_bao':baibao,
        'so_bai_bao': so_bai_bao,
        'so_page': so_page,
        'now_page': now_page,
        'tu_bai': tu_bai,
        'den_bai': den_bai}
    return render(request, 'baiBao/list.html', context)

def sua_trang_web_form(request, id):
   
    context = {
        'list_target_li': 'active',
        'target_data_active': 'true'}
    return render(request, 'trangWeb/update.html', context)

def xoa_trang_web(request, id):
    responseData = {'status': 'false'}
    return http.JsonResponse(responseData)