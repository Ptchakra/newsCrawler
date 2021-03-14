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
from django.contrib.auth.forms import PasswordChangeForm
from trangWeb.forms import AddTargetForm, UpdateTargetForm
from django.urls import reverse
from .models import TrangWeb
from django.utils import timezone

def index(request):
    context = {
        'trangWeb_data_active': 'true'}
    return render(request, 'trangWeb/index.html', context)

def them_trang_web_form(request):
    form = AddTargetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            TrangWeb.objects.create(
                **form.cleaned_data,
                insert_date=timezone.now(),
                trang_thai_chay = True)
            messages.add_message(
                request,
                messages.INFO,
                'Target domain ' +
                form.cleaned_data['ten_trang_web'] +
                ' added successfully')
            return http.HttpResponseRedirect(reverse('list_target'))
    context = {
        "add_target_li": "active",
        "target_data_active": "true",
        'form': form}
    return render(request, 'trangWeb/add.html', context)

def danh_sach_trang_web(request):
    context = {
        'list_target_li': 'active',
        'target_data_active': 'true'}
    return render(request, 'trangWeb/list.html', context)

def sua_trang_web_form(request, id):
   
    context = {
        'list_target_li': 'active',
        'target_data_active': 'true'}
    return render(request, 'trangWeb/update.html', context)

def xoa_trang_web(request, id):
    responseData = {'status': 'false'}
    return http.JsonResponse(responseData)