from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path(
        '',
        views.index,
        name='trangWebIndex'),
    path(
        'add/',
        views.them_trang_web_form,
        name='them_trang_web_form'),
    path(
        'update/<int:id>',
        views.sua_trang_web_form,
        name='sua_trang_web_form'),
    path(
        'list/',
        views.danh_sach_trang_web,
        name='danh_sach_trang_web'),
    path(
        'delete/<int:id>',
        views.xoa_trang_web,
        name='xoa_trang_web'),
    path(
        'bai-bao/list/',
        views.danh_sach_bai_bao,
        name='danh_sach_bai_bao'),
]