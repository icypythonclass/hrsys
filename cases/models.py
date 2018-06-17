from django.db import models

# Create your models here.


class Case(models.Model):
    BELONG_CHOICES = (
        ('J', '自社'),
        ('T', '他社'),
        ('U', '未知'),
    )
    case_name = models.CharField(verbose_name='案件名', max_length=50)
    case_place = models.CharField(verbose_name='案件場所', max_length=50)
    case_start_time = models.DateField(verbose_name='案件開始時間')
    case_end_time = models.DateField(verbose_name='案件終了時間')
    case_belongings = models.CharField(verbose_name='案件所属', max_length=1, default='U', choices=BELONG_CHOICES)
    case_industry = models.CharField(verbose_name='作業場所', max_length=20, null=True, blank=True)
    case_language = models.CharField(verbose_name='言語', max_length=20, null=True, blank=True)
    case_price = models.CharField(verbose_name='単価', max_length=10)
    case_remark = models.CharField(verbose_name='備考', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = '案件'
        verbose_name_plural = '案件'
        db_table = 'yo_cases'


