from django.db import models


class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
        ('U', '未知'),
    )
    birth_date = models.DateField(verbose_name='生年月日')
    last_name = models.CharField(verbose_name='姓', max_length=20, null=True, blank=True)
    first_name = models.CharField(verbose_name='名', max_length=20, null=True, blank=True)
    gender = models.CharField(verbose_name='性別', max_length=1, default='U', choices=GENDER_CHOICES)
    hire_date = models.DateField(verbose_name='雇用日')

    class Meta:
        verbose_name = '社員'
        verbose_name_plural = '社員'
        db_table = 'yo_employees'

    def __str__(self):
        return "{} {}".format(self.last_name, self.first_name)


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.DateTimeField(verbose_name='出勤时间')
    end_time = models.DateTimeField(verbose_name='退勤时间')
    rest_time = models.SmallIntegerField(verbose_name='休息时间')

    class Meta:
        verbose_name = '考勤'
        verbose_name_plural = '考勤'
        db_table = 'yo_attendances'

    def __str__(self):
        return "{} {}".format(self.employee, self.start_time.date())


class Technology(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    technology_name = models.CharField(verbose_name='技術', max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = '技術'
        verbose_name_plural = '技術'
        db_table = 'yo_technology'

    def __str__(self):
        return "{}技術".format(self.employee)


class CareerHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
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