from re import findall
from django.conf import settings
from django.utils import timezone, dateformat
from datetime import datetime
import os
import traceback
import yaml
import json
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


'''
crawler html trang web lay link bai viet trong vung tin tuc
'''
def crawlerTrangWeb():
    domain_trang_Web = 'https://vnexpress.net/thoi-su'
    phan_tin_tuc = '<body class="page-folder " data-source="Folder">'
    thu_tu_the_tin_tuc = 0
    # Lay tag cua the html bat dau cua vung tin tuc
    the_tin_tuc = phan_tin_tuc[1:-1].split(" ")[0]
    # Lay attrs cua phan the tin tuc
    parse_html_thiet_dat_phan_tin_tuc = BeautifulSoup(phan_tin_tuc, 'html.parser')
    attrs_the_tin_tuc = parse_html_thiet_dat_phan_tin_tuc.contents[0].attrs
    # Lay html cua trang web
    html_trang_web = requests.get(domain_trang_Web)
    # Lay html cua vung tin tuc
    html_tin_tuc = BeautifulSoup(html_trang_web.text, 'html.parser').find_all(the_tin_tuc, attrs_the_tin_tuc)[thu_tu_the_tin_tuc]
    # print(html_tin_tuc)

    # write html
    # html_output_path = './crawler_results/temp1.html'
    # with open(html_output_path,'w',encoding="utf-8") as temp:
    #     temp.write(str(html_tin_tuc))

    danh_sach_tag_xoa = ['meta','nav', 'picture', 'img', 'source', 'script', 'video', 'progress', 'use', 'svg', 'noscript', 'form', 'header', 'ul']

    # Xoa tag ra khoi html
    for tag in html_tin_tuc.find_all(danh_sach_tag_xoa):
        tag.extract()

    # write html
    html_output_path = './crawler_results/temp2.html'
    with open(html_output_path,'w',encoding="utf-8") as temp:
        temp.write(str(html_tin_tuc))

    # Lay all href
    danh_sach_tag_co_href = html_tin_tuc.find_all(href=re.compile('.+'))
    danh_sach_href = []
    try:
        with open('./crawler_results/danh_sach_href.txt','r',encoding="utf-8") as file_href:
            noi_dung_file = file_href.read()
            danh_sach_href = noi_dung_file.split("\n")
    except:
        print("chua co file href thoi")
    print(danh_sach_href)

    print("---------------------")
    for tag in danh_sach_tag_co_href:
        if validators.url(str(tag['href'])):
            if str(tag['href']).split('#')[0] not in danh_sach_href:
                # print("0: ",str(tag['href']))
                danh_sach_href.append(str(tag['href']))
                crawlerBaiBao(str(tag['href']))

    chuoi_href = '\n'.join(danh_sach_href)
    # print(danh_sach_href)
    # write html
    html_output_path = './crawler_results/danh_sach_href.txt'
    with open(html_output_path,'w',encoding="utf-8") as temp:
        temp.write(str(chuoi_href))
        


def crawlerBaiBao(link_trang_bai_viet):
    # link_trang_bai_viet = 'https://vnexpress.net/tuong-lop-cuu-nan-tren-nhung-cung-duong-deo-doc-4243437.html'
    if validators.url(link_trang_bai_viet):
        the_tieu_de = '<h1 class="title-detail">'
        thu_tu_the_tieu_de = 0
        the_noi_dung = '<div class="sidebar-1">'
        thu_tu_the_noi_dung = 0
        the_tac_gia = '<strong>'
        thu_tu_the_tac_gia = -1

        # Lay attrs cua phan the tieu de
        tag_tieu_de = the_tieu_de[1:-1].split(" ")[0]
        parse_html_thiet_dat_phan_tieu_de = BeautifulSoup(the_tieu_de, 'html.parser')
        attrs_the_tieu_de = parse_html_thiet_dat_phan_tieu_de.contents[0].attrs
        # Lay attrs cua phan the noi dung
        tag_noi_dung = the_noi_dung[1:-1].split(" ")[0]
        parse_html_thiet_dat_phan_noi_dung = BeautifulSoup(the_noi_dung, 'html.parser')
        attrs_the_noi_dung = parse_html_thiet_dat_phan_noi_dung.contents[0].attrs
        # Lay attrs cua phan the tac gia
        tag_tac_gia = the_tac_gia[1:-1].split(" ")[0]
        parse_html_thiet_dat_phan_tac_gia = BeautifulSoup(the_tac_gia, 'html.parser')
        attrs_the_tac_gia = parse_html_thiet_dat_phan_tac_gia.contents[0].attrs
        # tag_tac_gia = parse_html_thiet_dat_phan_tac_gia.name

        # Lay html cua trang bai bao
        html_trang_bai_bao = requests.get(link_trang_bai_viet)

        html_trang_bai_bao = BeautifulSoup(html_trang_bai_bao.text, 'html.parser')

        #Lay tac gia
        print(link_trang_bai_viet)
        print(html_trang_bai_bao.find_all(tag_tac_gia, attrs_the_tac_gia))
        try:
            ten_tac_gia = html_trang_bai_bao.find_all(tag_tac_gia, attrs_the_tac_gia)[thu_tu_the_tac_gia]
            ten_tac_gia = str(ten_tac_gia.text)
        except:
            ten_tac_gia = ''
        # write html
        # html_output_path = './crawler_results/temp1.txt'
        # with open(html_output_path,'w',encoding="utf-8") as temp:
        #     temp.write(str(ten_tac_gia))
        # Lay tieu de
        try:
            tieu_de_bai_bao = html_trang_bai_bao.find_all(tag_tieu_de, attrs_the_tieu_de)[thu_tu_the_tieu_de]
            tieu_de_bai_bao = str(tieu_de_bai_bao.text)
        except:
            tieu_de_bai_bao = 'dinh danh tieu de khong dung cho trang: '+link_trang_bai_viet
        # write html
        # html_output_path = './crawler_results/temp2.txt'
        # with open(html_output_path,'w',encoding="utf-8") as temp:
        #     temp.write(str(tieu_de_bai_bao))

        # Lay noi dung bai bao
        try:
            noi_dung_bai_bao = html_trang_bai_bao.find_all(tag_noi_dung, attrs_the_noi_dung)[thu_tu_the_noi_dung]
            
            danh_sach_tag_xoa = ['meta','nav', 'picture', 'img', 'source', 'script', 'video', 'progress', 'use', 'svg', 'noscript', 'form', 'ul', 'figure', 'a', 'header', 'span']
            # Xoa tag ra khoi html
            for tag in noi_dung_bai_bao.find_all(danh_sach_tag_xoa):
                tag.extract()

            html_output_path = './crawler_results/temp1.html'
            with open(html_output_path,'w',encoding="utf-8") as temp:
                temp.write(str(noi_dung_bai_bao))
            noi_dung_bai_bao = str(noi_dung_bai_bao.text)
        except:
            noi_dung_bai_bao = 'dinh dang noi dung khong dung cho trang: '+link_trang_bai_viet
        # print(noi_dung_bai_bao)

        now = datetime.now()
        time = now.strftime("%H%M%S%f")
        print("time:", time)
        # write html
        html_output_path = './crawler_results/'+time+'.txt'
        with open(html_output_path,'w',encoding="utf-8") as temp:
            temp.write(str(noi_dung_bai_bao))

if __name__ == '__main__':
    crawlerTrangWeb()