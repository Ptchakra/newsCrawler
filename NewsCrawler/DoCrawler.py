from __future__ import absolute_import, unicode_literals
from asyncio.tasks import sleep
from re import findall
from django.conf import settings
from django.utils import timezone, dateformat
import os
import traceback
import yaml
import json
import bs4
import re
from datetime import datetime
import time
import requests
import validators
from urllib.request import urlopen
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

# from trangWeb.models import TrangWeb
from celery import shared_task
import time


def crawler_handler():
    print("chay crawler")
    run_crawler()
    print("end chayj crawler")

def run_crawler():
    from trangWeb.models import TrangWeb
    danh_sach_trang_web = TrangWeb.objects.filter(trang_thai_chay=True)
    print(danh_sach_trang_web)
    for trang_web in danh_sach_trang_web:
        crawlerTrangWeb(trang_web.link_trang_web, trang_web.the_vung_tin_tuc, trang_web.thu_tu_cua_the_vung_tin_tuc -1, trang_web.the_tieu_de, trang_web.thu_tu_cua_the_tieu_de -1 , trang_web.the_noi_dung, trang_web.thu_tu_the_noi_dung -1)
 
def crawlerTrangWeb(link_trang_web, the_vung_tin_tuc, thu_tu_cua_the_vung_tin_tuc, the_tieu_de, thu_tu_cua_the_tieu_de, the_noi_dung, thu_tu_the_noi_dung):
    from trangWeb.models import TrangWeb, BaiBao
    domain_web = link_trang_web.split('/')[2]
    preHref_tag = f"https://{domain_web}"
    # Lay tag cua the html bat dau cua vung tin tuc
    the_tin_tuc = the_vung_tin_tuc[1:-1].split(" ")[0]
    # Lay attrs cua phan the tin tuc
    parse_html_thiet_dat_phan_tin_tuc = BeautifulSoup(the_vung_tin_tuc, 'html.parser')
    attrs_the_tin_tuc = parse_html_thiet_dat_phan_tin_tuc.contents[0].attrs
    # Lay html cua trang web
    html_trang_web = requests.get(link_trang_web)
    # Lay html cua vung tin tuc
    html_tin_tuc = BeautifulSoup(html_trang_web.text, 'html.parser').find_all(the_tin_tuc, attrs_the_tin_tuc)[thu_tu_cua_the_vung_tin_tuc]
 
    danh_sach_tag_xoa = ['meta','nav', 'picture', 'img', 'source', 'script', 'video', 'progress', 'use', 'svg', 'noscript', 'form', 'header', 'ul']

    # Xoa tag ra khoi html
    for tag in html_tin_tuc.find_all(danh_sach_tag_xoa):
        tag.extract()

    # Lay all href
    danh_sach_tag_co_href = html_tin_tuc.find_all(href=re.compile('.+'))
    print("---------------------")
    for tag in danh_sach_tag_co_href:
        link_bai_bao = str(tag['href'])
        if link_bai_bao[0] != 'h':
            link_bai_bao= str(preHref_tag) + link_bai_bao.lstrip('.')
        link_bai_bao = link_bai_bao.split('#')[0]
        if validators.url(link_bai_bao):
            if BaiBao.objects.filter(link_bai_bao=link_bai_bao).count() == 0:
                # danh_sach_href.append(str(tag['href']))
                # print(f"{link_bai_bao} soluong {BaiBao.objects.filter(link_bai_bao=link_bai_bao).count()}")
                try :
                    crawlerBaiBao(link_trang_web, link_bai_bao, the_tieu_de, thu_tu_cua_the_tieu_de, the_noi_dung, thu_tu_the_noi_dung)
                except Exception as e: 
                    print(e)

def crawlerBaiBao(link_trang_web, link_trang_bai_viet, the_tieu_de, thu_tu_the_tieu_de, the_noi_dung, thu_tu_the_noi_dung):
    # link_trang_bai_viet = 'https://vnexpress.net/tuong-lop-cuu-nan-tren-nhung-cung-duong-deo-doc-4243437.html'
    if validators.url(link_trang_bai_viet):
        print(f"link trang web {link_trang_bai_viet}")
        # Lay attrs cua phan the tieu de
        from trangWeb.models import BaiBao, so_bai_tung_trang, tong_bai_hang_ngay, TrangWeb, top50
        tag_tieu_de = the_tieu_de[1:-1].split(" ")[0]
        parse_html_thiet_dat_phan_tieu_de = BeautifulSoup(the_tieu_de, 'html.parser')
        attrs_the_tieu_de = parse_html_thiet_dat_phan_tieu_de.contents[0].attrs
        # Lay attrs cua phan the noi dung
        tag_noi_dung = the_noi_dung[1:-1].split(" ")[0]
        parse_html_thiet_dat_phan_noi_dung = BeautifulSoup(the_noi_dung, 'html.parser')
        attrs_the_noi_dung = parse_html_thiet_dat_phan_noi_dung.contents[0].attrs
        # Lay attrs cua phan the tac gia
        # tag_tac_gia = the_tac_gia[1:-1].split(" ")[0]
        # parse_html_thiet_dat_phan_tac_gia = BeautifulSoup(the_tac_gia, 'html.parser')
        # attrs_the_tac_gia = parse_html_thiet_dat_phan_tac_gia.contents[0].attrs
        # tag_tac_gia = parse_html_thiet_dat_phan_tac_gia.name

        # Lay html cua trang bai bao
        html_trang_bai_bao = requests.get(link_trang_bai_viet)

        html_trang_bai_bao = BeautifulSoup(html_trang_bai_bao.text, 'html.parser')

        #Lay tac gia
        # try:
        #     ten_tac_gia = html_trang_bai_bao.find_all(tag_tac_gia, attrs_the_tac_gia)[thu_tu_the_tac_gia]
        #     ten_tac_gia = str(ten_tac_gia.text)
        # except:
        #     ten_tac_gia = ''

        # Lay tieu de
        try:
            print(the_tieu_de)
            tieu_de_bai_bao = html_trang_bai_bao.find_all(tag_tieu_de, attrs_the_tieu_de)[thu_tu_the_tieu_de]
            tieu_de_bai_bao = str(tieu_de_bai_bao.text)
            print(tieu_de_bai_bao)
            print("=============================")
        except:
            tieu_de_bai_bao = link_trang_bai_viet
            print("deco co ==============================")

        # Lay noi dung bai bao
        noi_dung_bai_bao = html_trang_bai_bao.find_all(tag_noi_dung, attrs_the_noi_dung)[thu_tu_the_noi_dung]
        
        danh_sach_tag_xoa = ['meta','nav', 'picture', 'img', 'source', 'script', 'video', 'progress', 'use', 'svg', 'noscript', 'form', 'ul', 'a', 'header']
        # Xoa tag ra khoi html
        for tag in noi_dung_bai_bao.find_all(danh_sach_tag_xoa):
            tag.extract()

        for tag in noi_dung_bai_bao.find_all('p'):
            new_string = '\n\n' + str(tag.text)
            tag.string = new_string
        noi_dung_bai_bao = str(noi_dung_bai_bao.text)
        noi_dung_bai_bao = noi_dung_bai_bao.split('\n')
        noi_dung_bai_bao = list(filter(('').__ne__, noi_dung_bai_bao))
        noi_dung_bai_bao = '\n'.join(noi_dung_bai_bao)
        if noi_dung_bai_bao != '':
            bai_moi = BaiBao.objects.create(ten_trang_web= TrangWeb.objects.filter(link_trang_web=link_trang_web)[0], link_bai_bao=link_trang_bai_viet, tieu_de= tieu_de_bai_bao, ngay_them=datetime.now(), noi_dung=noi_dung_bai_bao)
            bai_moi.save()
            try:
                so_bai_moi_trang = so_bai_tung_trang.objects.filter(trang_web=link_trang_web)[0]
            except:
                so_bai_moi_trang = so_bai_tung_trang.objects.create(trang_web=link_trang_web, so_bai_viet=0)
            # so_bai_moi_trang.so_bai_viet.values
            so_bai_moi_trang.so_bai_viet = so_bai_moi_trang.so_bai_viet + 1
            so_bai_moi_trang.save()
            try:
                tong_bai  = tong_bai_hang_ngay.objects.filter(ngay_them= datetime.now().strftime('%Y-%m-%d'))[0]
            except:
                tong_bai  = tong_bai_hang_ngay.objects.create(so_bai_viet=0,ngay_them=datetime.now().strftime('%Y-%m-%d'))
            tong_bai.so_bai_viet = tong_bai.so_bai_viet + 1 
            tong_bai.save()

            if top50.objects.all().count() < 50:
                print(tieu_de_bai_bao)
                top50.objects.create(ten_trang_web= TrangWeb.objects.filter(link_trang_web=link_trang_web)[0], link_bai_bao=link_trang_bai_viet, tieu_de= tieu_de_bai_bao, ngay_them=datetime.now(), noi_dung=noi_dung_bai_bao)
            else:
                top50.objects.first().delete()
                top50.objects.create(ten_trang_web= TrangWeb.objects.filter(link_trang_web=link_trang_web)[0], link_bai_bao=link_trang_bai_viet, tieu_de= tieu_de_bai_bao, ngay_them=datetime.now(), noi_dung=noi_dung_bai_bao)
                # print(f"{tieu_de_bai_bao} top 50 {top50.objects.last().tieu_de}")