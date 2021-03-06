from django.db import models
from django.utils import timezone



class TrangWeb(models.Model):
    ten_trang_web = models.CharField(max_length=300)
    vung_tin_tuc = models.TextField()
    insert_date = models.DateTimeField()
    last_scan_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.domain_name