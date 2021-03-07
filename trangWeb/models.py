from django.db import models
from django.db.models.expressions import F
from django.utils import timezone
from datetime import datetime


class TrangWeb(models.Model):
    ten_trang_web = models.CharField(max_length=300,primary_key=True,unique=True,db_index=True)
    the_vung_tin_tuc = models.CharField(max_length=300)
    thu_tu_cua_the_vung_tin_tuc = models.IntegerField(default=0)
    the_tieu_de = models.CharField(max_length=300)
    thu_tu_cua_the_tieu_de = models.IntegerField(default=0)
    the_tac_gia = models.CharField(max_length=300)
    thu_tu_cua_the_tac_gia = models.IntegerField(default=0)
    ngay_them = models.DateTimeField(default=datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
    trang_thai_chay = models.BooleanField(default=True)

    def __str__(self):
        return self.ten_trang_web
    
class BaiBao(models.Model):
    ten_trang_web = models.ForeignKey(TrangWeb,on_delete=models.CASCADE, null=False)
    link_bai_bao = models.CharField(max_length=300,primary_key=True,unique=True,db_index=True)
    tieu_de = models.CharField(max_length=300)
    tac_gia = models.CharField(max_length=300)
    ngay_them = models.DateTimeField()
    noi_dung = models.TextField()
    chu_de = models.TextField()
    tu_khoa = models.TextField()
    
    def __str__(self):
        return self.link_bai_bao

class top50(models.Model):
    ten_trang_web = models.ForeignKey(TrangWeb,on_delete=models.CASCADE, null=False)
    link_bai_bao = models.CharField(max_length=300,unique=True,db_index=True)
    tieu_de = models.CharField(max_length=300)
    tac_gia = models.CharField(max_length=300)
    ngay_them = models.DateTimeField()
    noi_dung = models.TextField()
    chu_de = models.TextField()
    tu_khoa = models.TextField()
    
    def __str__(self):
        return self.link_bai_bao

class so_bai_tung_trang(models.Model):
    trang_web = models.CharField(max_length=300)
    so_bai_viet = models.IntegerField()
    
    def __str__(self):
        return self.trang_web

class tong_bai_hang_ngay(models.Model):
    so_bai_viet = models.IntegerField()
    ngay_them = models.DateTimeField(default=datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
    
    def __str__(self):
        return self.so_bai_viet