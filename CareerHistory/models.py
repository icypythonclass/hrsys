from django.db import models


class CareerHistory(models.Model):
    company = models.TextField(verbose_name='会社名前', max_length=200)
    start_date = models.DateField(verbose_name='開始日付')
    end_date = models.DateField(verbose_name='終了日付')
    role = models.CharField(verbose_name='役割', max_length=100)
    department = models.TextField(verbose_name='部', max_length=200)
    contribution = models.TextField(verbose_name='業務内容', max_length=200)

    class Meta:
        verbose_name = '職務経歴'
        verbose_name_plural = '職務経歴'
        db_table = 'yo_career_history'

    def __str__(self):
        return "{} ~ {}, {}".format(self.start_date, self.end_date, self.company)